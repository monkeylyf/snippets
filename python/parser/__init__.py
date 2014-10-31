"""Parsers package.

Author: yifeng@niara.com
"""

from parsers import _get_factories


def parsed_file(typ, fh, **kwargs):
    """"""
    return _get_factories()[typ](fh, **kwargs)


__all__ = ['parsed_file']
