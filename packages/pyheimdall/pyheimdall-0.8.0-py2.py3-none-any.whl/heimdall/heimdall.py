#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Provides CRUD operations to search in or edit a HERA elements tree.

:copyright: The pyHeimdall contributors.
:licence: Afero GPL, see LICENSE for more details.
:SPDX-License-Identifier: AGPL-3.0-or-later
"""

from .properties import (
    getProperty, getProperties,
    createProperty, deleteProperty,
    replaceProperty, updateProperty,
    )
from .entities import (
    getEntity, getEntities,
    createEntity, deleteEntity,
    replaceEntity, updateEntity,
    )
from .attributes import (
    getAttribute, getAttributes,
    createAttribute, deleteAttribute,
    replaceAttribute, updateAttribute,
    )
from .items import (
    getItem, getItems,
    createItem, deleteItem,
    replaceItem, updateItem,
    )
from .metadata import (
    getMetadata, getValue, getValues,
    createMetadata, deleteMetadata,
    )
from .util import (
        get_node as _get_node,
        get_nodes as _get_nodes,
        get_root as _get_root,
        create_nodes as _create_nodes,
    )

CONNECTORS_IN = dict()
CONNECTORS_OUT = dict()


def discover():
    from pkgutil import iter_modules
    from importlib import import_module
    from heimdall import connectors
    for submodule in iter_modules(connectors.__path__):
        path = f'heimdall.connectors.{submodule.name}'
        import_module(path)


def getDatabase(**options):
    r"""Imports a database as a HERA element tree

    :param \**options: Keyword arguments, see below.
    :return: HERA element tree
    :rtype: lxml.ElementTree

    :Keyword arguments:
        * **url** (``str``) -- Location of the database to load
        * **format** (``str``) -- Format of the database to load, see below

    This function can be used to import an HERA element tree from different
    formats, depending of the ``format`` option.
    Supported formats are:

    * ``xml:hera``: XML file; see
      :py:class:`heimdall.hera.getDatabase`
    * ``json:hera``: JSON file; see
      :py:class:`heimdall.json.getDatabase`
    * ``csv``: CSV files; see
      :py:class:`heimdall.csv.getDatabase`
    * ``sql:mariadb``: MariaDB database; see
      :py:class:`heimdall.sql.mysql.getDatabase`
    * ``sql:mysql``: MySQL database; see
      :py:class:`heimdall.sql.mysql.getDatabase`
    * ``api:nakala``: Nakala API; see
      :py:class:`heimdall.third_party.nakala.getDatabase`
    * ``api:collectiveaccess``: CollectiveAccess API; see
      :py:class:`heimdall.third_party.collective_access.getDatabase`

    Depending on ``format`` option, ``getDatabase`` may accept more options.
    See the individual module ``getDatabase`` documentation for more info.
    """
    fun = CONNECTORS_IN[options['format']]
    return fun(**options)


def createDatabase():
    """Creates an empty database

    :return: HERA element tree
    :rtype: lxml.ElementTree
    """
    from .connectors import xml
    return xml.createDatabase()


def serialize(tree, **options):
    r"""Exports a HERA element tree

    :param tree: HERA element tree
    :param \**options: (optional) Keyword arguments, see description.

    This function can be used to export an HERA element tree in different
    formats, depending of the ``format`` parameter.
    Supported formats are:

    * ``xml:hera``: XML file; see
      :py:class:`heimdall.hera.serialize`
    * ``json:hera``: JSON file; see
      :py:class:`heimdall.json.serialize`
    * ``csv``: CSV files; see
      :py:class:`heimdall.csv.serialize`
    * ``sql:mariadb``: MariaDB dump file; see
      :py:class:`heimdall.sql.mysql.serialize`
    * ``sql:mysql``: MySQL dump file; see
      :py:class:`heimdall.sql.mysql.serialize`

    Depending on ``format`` option, ``serialize`` may accept more options.
    See the individual module ``serialize`` documentation for more info.
    """
    fun = CONNECTORS_OUT[options['format']]
    return fun(tree, **options)


__copyright__ = "Copyright the pyHeimdall contributors."
__license__ = 'AGPL-3.0-or-later'
__all__ = [
    'getDatabase',
    'createDatabase',
    'serialize',

    'getProperty', 'getProperties',
    'createProperty', 'deleteProperty',
    'replaceProperty', 'updateProperty',

    'getEntity', 'getEntities',
    'createEntity', 'deleteEntity',
    'replaceEntity', 'updateEntity',
    'getAttribute', 'getAttributes',
    'createAttribute', 'deleteAttribute',
    'replaceAttribute', 'updateAttribute',

    'getItem', 'getItems',
    'createItem', 'deleteItem',
    'replaceItem', 'updateItem',
    'getMetadata', 'getValue', 'getValues',
    'createMetadata', 'deleteMetadata',

    '__copyright__', '__license__',
    ]
