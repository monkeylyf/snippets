"""CSV parser factory.

Author: yifeng
"""

from csv import (reader, QUOTE_MINIMAL)

from abstract_parser import AbstractParser


class ParserFactory(AbstractParser):

    """CSV parser factory."""

    def __init__(self, fh, regex=None, delimiter=' ', quotechar='|', quoting=QUOTE_MINIMAL):
        """Initilizer."""
        super(ParserFactory, self).__init__(fh, regex)

        self.fh = reader(self.fh, delimiter=delimiter, quotechar=quotechar,
                         quoting=quoting)

    def _regex(self):
        """"""
        raise NotImplemented

    def _skip(self, line):
        """"""
        return False

    def _format(self, line):
        """"""
        return line

    def __repr__(self):
        """"""
        return "<csv iterator object at {0}>".format(hex(id(self)))


def main():
    print ParserFactory()


if __name__ == '__main__':
    main()
