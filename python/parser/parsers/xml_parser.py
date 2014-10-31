"""XML parser factory.

Author: yifeng
"""

try:
    from lxml import etree as ET
except ImportError:
    import xml.etree.ElementTree as ET


from abstract_parser import AbstractParser


class ParserFactory(AbstractParser):

    """XML parser factory."""

    def __init__(self, fh, traverser=None, regex=None):
        """Initilizer."""
        super(ParserFactory, self).__init__(fh, regex=regex)

        root = ET.parse(self.fh).getroot()
        self.fh = (child for child in root)

        # Override self._format if traverser is not None
        self._format = traverser or self._format

    def _skip(self, line):
        """"""
        return False

    def _regex(self):
        """"""
        raise NotImplemented

    def _format(self, line):
        """"""
        return line

    def __repr__(self):
        """"""
        return "<xml iterator object at {0}>".format(hex(id(self)))


def main():
    print ParserFactory()


if __name__ == '__main__':
    main()
