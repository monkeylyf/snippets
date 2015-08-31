"""Utilities for parsers

"""

from __init__ import parsed_file


def test_csv_parser():
    filename = './data/text.csv'
    parser_typ = 'csv_parser'
    parameters = dict(delimiter=',')

    with open(filename, 'r') as csvfile:
        darr = parsed_file(parser_typ, csvfile, **parameters)
        for line in darr:
            print line


def test_xml_parser():
    filename = './data/controllers_20140610_1530.xml'
    parser_typ = 'xml_parser'

    parameters = dict(traverser=lambda x : x.attrib)

    with open(filename, 'r') as xmlfile:
        darr = parsed_file(parser_typ, xmlfile, **parameters)
        for line in darr:
            print line


def test_plain_text():
    filename = './data/malwareurl_20140610_1530.txt'
    parser_typ = 'plain_text_parser'

    parameters = dict(delimiter='|', prefix=('#', 'ASN'))

    with open(filename, 'r') as txtfile:
        darr = parsed_file(parser_typ, txtfile, **parameters)
        for line in darr:
            print line


def main():
    test_csv_parser()
    test_xml_parser()
    test_plain_text()


if __name__ == '__main__':
    main()
