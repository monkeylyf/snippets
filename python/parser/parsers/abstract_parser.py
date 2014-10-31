"""Abstract parser class.

Author: yifeng
"""

from abc import ABCMeta, abstractmethod


class AbstractParser(object):

    """Abstract parser class."""

    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, fh, regex=None):
        """Initializer."""
        self.fh = fh
        self.regex = regex

    def __iter__(self):
        """Implementation of iter as an iterator."""
        return self

    def next(self):
        """Implementation of next as an iterator."""
        try:
            line = next(self.fh)
            if self._skip(line):
                return self.next()
            else:
                return self._format(line)
        except StopIteration:
            raise

    @abstractmethod
    def _regex(self):
        """Regex for pattern extraction."""
        pass

    @abstractmethod
    def _skip(self):
        """Skip line/content."""
        pass

    @abstractmethod
    def _format(self, line):
        """"""
        pass
