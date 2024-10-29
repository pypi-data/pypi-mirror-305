# -*- coding: utf-8 -*-
from .heimdall import CONNECTORS_IN as _IN, CONNECTORS_OUT as _OUT


def connector_in(format):
    if type(format) is not list:
        format = [format, ]

    def inner(fun):
        for f in format:
            _IN[f] = fun

    return inner


def connector_out(format):
    if type(format) is not list:
        format = [format, ]

    def inner(fun):
        for f in format:
            _OUT[f] = fun

    return inner
