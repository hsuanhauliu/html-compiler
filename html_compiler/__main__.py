"""
    A simple and lightweight html compilating program.
"""

from argparse import ArgumentParser

import html_compiler as hc


def main():
    """ main """

    # Parse args
    parser = ArgumentParser(description='Input root filename.')
    parser.add_argument('filename', type=str,
                        help='Root filename')
    parser.add_argument('-o', '--output', type=str, default='output.html',
                        help='Output filename')
    args = parser.parse_args()

    soup = hc.compile(args.filename)
    hc.output(soup, args.output)


if __name__ == "__main__":
    main()
