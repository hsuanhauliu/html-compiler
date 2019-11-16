"""
    Utility functions.
"""

from bs4 import BeautifulSoup


def output(soup, filename, prettify=False):
    """ Output the html """
    with open(filename, "w") as wfile:
        if prettify:
            wfile.write(str(soup.prettify()))
        else:
            wfile.write(str(soup))
