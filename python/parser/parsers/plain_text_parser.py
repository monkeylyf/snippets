"""Parser factory for plain text format.

Author: yifeng@niara.com
"""

from abstract_parser import AbstractParser


class ParserFactory(AbstractParser):

    """Parser factory for plain text format."""

    def __init__(self, fh, delimiter='\t', prefix=None, regex=None):
        """Initilizer."""
        super(ParserFactory, self).__init__(fh, regex=regex)

        self.delimiter = delimiter
        self.prefix = prefix

    def _regex(self):
        """"""
        raise NotImplemented

    def _skip(self, line):
        """"""
        return self.prefix is not None and line.startswith(self.prefix)

    def _format(self, line):
        """"""
        if self.delimiter:
            return map(str.strip, line.split(self.delimiter))
        else:
            return line

    def __repr__(self):
        """"""
        return "<plain text iterator object at {0}>".format(hex(id(self)))


def main():
    print ParserFactory()


if __name__ == '__main__':
    main()
