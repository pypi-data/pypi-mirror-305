# -*- coding: utf-8 -*-
from lxml import etree as _etree
import requests as _api
import heimdall as _h
from heimdall.util import set_language as _set_language
from ..decorators import connector_in, connector_out


ITEM_EID = 'item'
FILE_EID = 'file'


@connector_in('api:collectiveaccess')
def getDatabase(**options):
    r"""Imports a database from a CollectiveAccess server

    :param \**options: Keyword arguments, see below.
    :return: HERA element tree
    :rtype: lxml.ElementTree

    :Keyword arguments:
        * **url** (``str``) -- CollectiveAccess endpoint

    See the `CollectiveAccess Web Service API documentation <https://manual.collectiveaccess.org/providence/developer/web_service_api.html>`_ for more info.

    At the time of writing, there  a sandbox (test) instance at the following url:
    https://demo.collectiveaccess.org/ (username:"demo", password:"demo")
    The API seems in turn to be callable from this kind of url:
    https://demo.collectiveaccess.org/service.php/json/find/ca_objects?q=*&pretty=1
    """  # nopep8: E501
    base_url = options['url']
    auth = options['auth']
    response = _request(f'{base_url}/find/ca_objects?q=*', auth=auth)
    data = response.get('results', [])
    tree = _create_tree(data, base_url, auth)
    return tree


def _request(url, auth):
    response = _api.get(url, auth=auth)
    if response.status_code != _api.codes.ok:
        response.raise_for_status()
    # NOTE: maybe check for response.headers, too?
    return response.json()


def _create_tree(data, base_url, auth):
    root = _h.createDatabase()
    properties = root.xpath('//properties')[0]
    entities = root.xpath('//entities')[0]
    items = root.xpath('//items')[0]
    object_ids = list()
    for o in data:
        object_ids.append(o['id'])
    count = 0
    for id_ in object_ids:
        count += 1
        response = _request(f'{base_url}/item/ca_objects/id/{id_}', auth=auth)
        (item, files) = _create_item(response)
        items.append(item)
        for file in files:
            items.append(file)
    return root


def _create_item(ca_object):
    item = _etree.Element('item', {'eid': 'object', })
    files = list()
    for key, value in ca_object.items():
        if key == 'intrinsic':
            for k, v in value.items():
                metadata = _create_system_metadata(f'ca_{k}', v)
                item.append(metadata)
            continue
        elif key == 'representations':
            for k, v in value.items():
                (file, metadata) = _create_file(k, v)
                files.append(file)
                item.append(metadata)
            continue
        elif not key.startswith('ca_objects.'):
            continue
        for metadata in _create_metadata(key, value):
            item.append(metadata)
    return (item, files)


def _create_file(key, data):
    metadata = _etree.Element('metadata', {'aid': f'representation', })
    metadata.text = key
    item = _etree.Element('item', {'eid': 'file', })
    _etree.SubElement(item, 'metadata', {'aid': 'id', 'pid': 'id', }).text = key  # nopep8: E501
    item.append(_create_system_metadata('url', data['urls']['original']))
    data = data['info']['original']
    item.append(_create_system_metadata('mediatype', data['MIMETYPE']))
    item.append(_create_system_metadata('width', data['WIDTH']))
    item.append(_create_system_metadata('height', data['HEIGHT']))
    item.append(_create_system_metadata('filename', data['FILENAME']))
    value = data['PROPERTIES']['filesize']
    item.append(_create_system_metadata('filesize', value))
    value = data['PROPERTIES']['bitdepth']
    item.append(_create_system_metadata('bitdepth', value))
    value = data['PROPERTIES']['colorspace']
    item.append(_create_system_metadata('colorspace', value))
    item.append(_create_system_metadata('md5', data['MD5']))
    return (item, metadata)


def _create_system_metadata(aid, value):
    node = _etree.Element('metadata', {'aid': aid, })
    node.text = str(value)
    return node


def _create_metadata(id, ca_field):
    metadata = list()
    for key, v in ca_field.items():
        for language_code, values in v.items():
            if type(values) is list:
                continue  # values = [] means no values, so don't bother
            # else  type(values) should be dict
            for aid, value in values.items():
                node = _etree.Element('metadata', {'aid': aid, })
                _set_language(node, language_code)
                if len(values) > 1:
                    node.set('ca_id', key)
                node.text = value
                metadata.append(node)
    return metadata


@connector_out('api:collectiveaccess')
def serialize(tree, url, **options):
    r"""Posts a HERA elements tree to the CollectiveAccess API

    :param tree: HERA elements tree
    :param url: Endpoint to POST to

    .. NOTE::
       There are not plans to implement this feature in the foreseeable future.
       This can be either due to lack of resources, lack of demand, because it
       wouldn't be easily maintenable, or any combination of these factors.

       Interested readers can submit a request to further this topic.
       See the ``CONTRIBUTING`` file at the root of the repository for details.
    """
    raise NotImplementedError("TODO")
