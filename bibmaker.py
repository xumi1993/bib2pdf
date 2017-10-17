from urllib import request
import os
import argparse

class bibmaker(object):
    def __init__(self, libfile):
        self.libfile = libfile

    def append_bib(self, path):
        if os.path.exists(path):
            with open(path) as f:
                cont = f.read()
        else:
            try:
                cont = request.urlopen(path).read()
            except:
                raise ValueError('Invalid path \'%s\'' % path)
        with open(self.libfile, 'a+') as f:
            f.write(cont+'\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script for importing bib to lib')
    parser.add_argument('-I', dest='libfile', help='bib libfile path')
    parser.add_argument('bib', type=str, help='bib url or file')
    args = parser.parse_args()
