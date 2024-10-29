# -*- coding: utf-8 -*-
import csv as _csv
import os as _os
import heimdall
from ..decorators import connector_in, connector_out


@connector_in('csv')
def getDatabase(**options):
    r"""Imports a database from one or more CSV files

    :param \**options: Keyword arguments, see below.
    :return: HERA element tree
    :rtype: lxml.ElementTree

    :Keyword arguments:
        * **url** (``str``) -- Pattern of CSV files to read from

    .. ERROR::
       This feature is not implemented yet.

       Interested readers can submit a request to further this topic.
       See the ``CONTRIBUTING`` file at the root of the repository for details.
    """
    raise NotImplementedError("TODO")


@connector_out('csv')
def serialize(tree, url, **options):
    r"""Serializes a HERA elements tree into CSV files

    :param tree: HERA elements tree
    :param url: Path to an existing directory
    :param \**options: (optional) Keyword arguments, see below.
    :Keyword arguments:
        * **header** (``bool``) -- (optional, default: ``True``)
          If ``True``, first line in each CSV is a header containing column
          names; if ``False``, first line will be the first item in ``tree``
        * **delimiter** (``str``) -- (optional, default: ``,``)
          CSV column delimiter
        * **quotechar** (``str``) -- (optional, default: ``"``)
          CSV "quoting character"; quotes will only be used if necessary
        * **multivalue** (``str``) -- (optional, default: ``|``)
          CSV multivalue delimiter

    This function can be used to export an HERA elements tree as CSV files.
    One CSV file is created per entity in ``tree``; this CSV has one column
    per attribute in this entity, and one line (excluding header if any)
    per item belonging to this entity in ``tree``.

    Each CSV file path will be ``<url>/<eid>.csv``, with ``eid`` being each
    entity's identifier in ``tree``.
    If a given entity doesn't have any attribute, the file will be empty.
    If no item belongs to this entity in ``tree``, the file will be empty,
    bar the header if any.
    """
    folder = url
    if not _os.path.isdir(folder):
        raise ValueError("Option 'path' must be a directory")

    header = options.get('header', True)
    comma = options.get('delimiter', ',')
    quote = options.get('quotechar', '"')
    pipe = options.get('multivalue', '|')

    for entity in heimdall.getEntities(tree):
        eid = entity.get('id')
        path = _os.path.join(folder, f'{eid}.csv')
        attributes = heimdall.getAttributes(entity)
        header = [_attr2col(a) for a in attributes]
        with open(path, 'w', newline='') as f:
            writer = _csv.writer(
                f,
                delimiter=comma,
                quotechar=quote,
                quoting=_csv.QUOTE_MINIMAL)
            if header:
                writer.writerow(header)
            items = heimdall.getItems(tree, lambda n: n.get('eid') == eid)
            for item in items:
                row = _item2row(item, attributes, pipe)
                writer.writerow(row)


def _attr2col(attribute):
    """Deduces column name from `attribute`

    :param attribute: HERA attribute element
    """
    name = attribute.get('id')
    if name is not None:
        return name
    name = attribute.get('pid')
    if name is not None:
        entity = attribute.getparent()
        eid = f"{entity.get('id')}." if entity is not None else ''
        return f'{eid}{name}'
    entity = attribute.getparent()
    if entity is not None:
        attributes = heimdall.getAttributes(entity)
        index = attributes.index(attribute)
        return f"{entity.get('id')}.{index}"
    return "?"


def _item2row(item, attributes, pipe):
    """TODO

    :param item: HERA item element
    :param attributes: Attribute identifiers
    :param pipe: Multivalue separator
    """
    row = list()
    for a in attributes:
        aid = a.get('id')
        pid = a.get('pid')
        metadata = heimdall.getMetadata(item, aid=aid, pid=pid)
        value = pipe.join((m.text or '') for m in metadata)
        row.append(value)
    return row
