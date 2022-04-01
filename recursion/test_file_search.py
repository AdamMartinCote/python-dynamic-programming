import types

from recursion.file_search import search


def test_file_search():
    filename = "m2.conf"
    path = "C:\\tools"
    search(filename, path)
