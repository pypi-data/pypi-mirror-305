# -*- coding: utf-8 -*-
import heimdall
from ..decorators import connector_in, connector_out
from json import load, loads
from urllib.parse import urlparse
from urllib.request import urlopen
from lxml import etree


@connector_in('json:hera')
def getDatabase(**options):
    r"""Imports a database from one JSON file

    :param \**options: Keyword arguments, see below.
    :return: HERA element tree
    :rtype: lxml.ElementTree

    :Keyword arguments:
        * **url** (``str``) -- URL of a JSON file to read from
    """
    url = options['url']
    if not is_url(url):
        with open(url, 'r') as f:
            data = load(f)
    else:
        with urlopen(url) as response:
            data = loads(response.read().decode())
    return _create_tree(data)


def is_url(path):
    schemes = ('http', 'https', )
    return urlparse(path).scheme in schemes


def _create_tree(data):
    root = heimdall.createDatabase()

    # create Properties if any
    properties = data.get('properties', None)
    if properties is not None:
        elements = root.xpath('//properties')[0]
        for o in properties:
            uid = o['@id']  # @id is mandatory
            e = etree.SubElement(elements, 'property', id=uid)
            _add_xml_element_from_json(e, o, 'type')
            _add_xml_element_from_json(e, o, 'name')
            _add_xml_element_from_json(e, o, 'description')
            # _add_xml_element_from_json(e, o, 'uris')  # TODO property.uris

    # create Entities if any
    entities = data.get('entities', None)
    if entities is not None:
        elements = root.xpath('//entities')[0]
        # TODO entities

    # create Items if any
    items = data.get('items', None)
    if items is not None:
        elements = root.xpath('//items')[0]
        for o in items:
            e = etree.SubElement(elements, 'item')
            _add_attribute_from_json(e, o, 'eid')
            metadata = o.get('metadata', [])
            for m in metadata:
                pid = m['pid']  # pid is mandatory
                meta = etree.SubElement(e, 'metadata', pid=pid)
                meta.text = m['value']  # value is mandatory, too

    return etree.ElementTree(root)


def _add_xml_element_from_json(e, o, attr):
    value = o.get(attr, None)
    if value is not None:
        sub = etree.SubElement(e, attr)
        sub.text = value


def _add_attribute_from_json(e, o, attr):
    value = o.get(attr, None)
    if value is not None:
        e.set(attr, value)


@connector_out('json:hera')
def serialize(tree, url, **options):
    r"""Serializes a HERA elements tree into a JSON file

    :param tree: HERA elements tree
    :param url: Path of the JSON file to create

    .. ERROR::
       This feature is not implemented yet.
       This can be either due to lack of resources, lack of demand, because it
       wouldn't be easily maintenable, or any combination of these factors.

       Interested readers can submit a request to further this topic.
       See the ``CONTRIBUTING`` file at the root of the repository for details.
    """
    raise NotImplementedError("TODO")
