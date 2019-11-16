"""
    Compiler module.
"""

import os

from bs4 import BeautifulSoup


def compile(path):
    """ Recursive function for merging components """
    soup = ""
    next_dir, filename = _separate_dir_and_file(path)
    with cd(next_dir):
        with open(filename, "r") as rfile:
            soup = BeautifulSoup(rfile, 'html.parser')

        component_tags = soup.findAll("div", {"class": "m_component"})
        for tag in component_tags:
            tag_id = tag.get("id")
            component_file = tag_id + ".html"
            component = compile(component_file)
            soup.find(id=tag_id).replaceWith(component)

    return soup


def _separate_dir_and_file(path):
    """ Helper function for separating file directory and the file """
    temp = path.rfind("/")
    if temp == -1:
        return ".", path
    return path[:temp], path[temp + 1:]


class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)
