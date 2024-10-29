# -*- coding: utf-8 -*-
from lxml import etree as _etree
import requests as _api
import heimdall as _h
import uuid as _uuid
from heimdall.util import set_language as _set_language
from ..decorators import connector_in, connector_out


ITEM_EID = 'item'
FILE_EID = 'file'


@connector_in('api:nakala')
def getDatabase(**options):
    r"""Imports a database from a Nakala repository

    :param \**options: Keyword arguments, see below.
    :return: HERA element tree
    :rtype: lxml.ElementTree

    :Keyword arguments:
        * **url** (``str``) -- URL of a Nakala items list

    Option ``url`` can be either a Nakala collection URL, or the URL of
    a Nakala search query.

    * ``{baseurl}/collections/{identifier}`` for collections
    * ``{baseurl}/search?{query parameters}`` for search queries

    ``baseurl`` depends on the Nakala instance you are using.
    At the time of writing, there are two different instances:
    * ``https://api.nakala.fr/`` for the real Nakala
    * ``https://apitest.nakala.fr/`` for the sandbox (test) instance

    See ``{baseurl}/doc`` for details.
    """
    presets = _load_presets()

    url = options['url']
    headers = {'accept': 'application/json', }
    payload = {'page': 1, 'limit': 25, }
    response = _request(url, headers, payload)
    data = response.get('datas', None)
    if data is None:
        # NOTE: search results wrap items in key 'datas'; however,
        # collection results wrap them in 'data', that's nakala logic for ya
        data = response['data']
        last = int(response['lastPage'])
        while int(payload['page']) != last:
            # request remaining pages; depending on url, this can take time ...
            payload['page'] += 1
            print(payload['page'], '/', last, '(', payload['limit'], ')')
            response = _request(url, headers, payload)
            data += response['data']
    print(len(data))
    tree = _create_tree(data, presets)
    return tree


def _request(url, headers, payload):
    response = _api.get(url, headers=headers, params=payload)
    if response.status_code != _api.codes.ok:
        response.raise_for_status()
    # NOTE: maybe check for response.headers, too?
    return response.json()


def _create_tree(data, presets):
    root = _h.createDatabase()
    properties = root.xpath('//properties')[0]
    entities = root.xpath('//entities')[0]
    items = root.xpath('//items')[0]
    for o in data:
        (item, files) = _create_item(o, presets)
        items.append(item)
        for file in files:
            items.append(file)
    return root


def _create_item(data, properties):
    item = _etree.Element('item', {'eid': ITEM_EID, })
    files = list()
    for key, value in data.items():
        if key == 'files':
            for o in data['files']:
                file = _create_file_item(o)
                uuid = str(_uuid.uuid4())
                m = _create_metadata(file, 'id', uuid)
                m.set('pid', 'id')
                # TODO maybe use file.sha1 instead of uuid?
                _create_metadata(item, 'file', uuid)
                files.append(file)
        elif key == 'metas':
            for o in data['metas']:
                _create_meta(item, o, properties)
        elif type(value) is list:
            for v in value:
                _create_metadata(item, key, v)
        else:
            _create_metadata(item, key, value)
    return (item, files)


def _create_file_item(data):
    item = _etree.Element('item', {'eid': FILE_EID, })
    for key, value in data.items():
        _create_metadata(item, key, value)
    return item


def _create_metadata(item, key, value):
    node = _etree.SubElement(item, 'metadata', {'aid': key})
    node.text = str(value)
    return node


def _create_meta(item, meta, properties):
    value = str(meta.get('value', ''))
    if value is None or len(value.strip()) < 1:
        return None  # no value, metadata is missing, don't create it
    uri = meta['propertyUri']
    pid = properties[uri].get('id')
    node = _etree.SubElement(item, 'metadata', {'pid': pid, 'aid': pid, })
    language_code = meta.get('lang', None)
    if language_code is not None:
        _set_language(node, language_code)
    node.text = value
    return node


@connector_out('api:nakala')
def serialize(tree, url, **options):
    r"""Posts a HERA elements tree to the Nakala API

    :param tree: HERA elements tree
    :param url: Endpoint to POST to

    .. ERROR::
       This feature is not implemented yet.
       Reasons are partly a lack of resources, but mostly concerns about
       making public sharing of research data too straightforward and the
       worry that too much convenience would lead to a further decline in
       metadata quality.

       Interested readers can submit a request to further this topic.
       See the ``CONTRIBUTING`` file at the root of the repository for details.
    """
    raise NotImplementedError("TODO")


def _load_presets():
    import os
    from ..util import get_nodes as _get_nodes
    cur = os.path.dirname(os.path.realpath(__file__))
    parts = [cur, *'../../presets/properties.xml'.split('/')]
    path = os.path.join(*parts)
    tree = _h.getDatabase(format='xml:hera', url=path)
    PRESETS = dict()
    for p in _h.getProperties(tree):
        uris = _get_nodes(p, 'uri')
        for uri in uris:
            try:
                do_not_want = PRESETS[uri.text]
                raise ValueError(f"URI '{uri}' not unique")
            except KeyError:
                PRESETS[uri.text] = p
    return PRESETS
