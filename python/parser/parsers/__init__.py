"""Parsers package.

Author: yifeng@niara.com
"""


from importlib import import_module
from pkgutil import iter_modules


FACTORIES_SINGLETON=None


def _get_factories():
    global FACTORIES_SINGLETON

    if not FACTORIES_SINGLETON:
        FACTORIES_SINGLETON = _load_parser_factories()

    return FACTORIES_SINGLETON


def _load_parser_factories(name='ParserFactory'):
    """"""
    factory_clz_mapping = {}

    mods = _walk_modules('nparser.parsers')

    for mod in mods:
        mod_name =  mod.__name__
        submod_name = mod_name.split('.')[-1]
        try:
            clz = getattr(mod, name)
            factory_clz_mapping[submod_name] = clz
        except AttributeError, e:
            pass

    return factory_clz_mapping


def _walk_modules(path):
    """Loads a module and all its submodules from a the given module path and
    returns them. If *any* module throws an exception while importing, that
    exception is thrown back.

    For example: _walk_modules('foo.bar')

    Stole this piece of code from Python Scrapy.
    """
    mods = []
    mod = import_module(path)
    mods.append(mod)

    if hasattr(mod, '__path__'):
        for _, subpath, ispkg in iter_modules(mod.__path__):
            fullpath = path + '.' + subpath
            if ispkg:
                mods += _walk_modules(fullpath)
            else:
                submod = import_module(fullpath)
                mods.append(submod)

    return mods


__all__ = ['_get_factories']
