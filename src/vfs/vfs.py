import os
import sys
from fuse import FUSE, Operations

class MemoryFS(Operations):
    def __init__(self):
        self.files = {}
        self.directories = {'/': []}

    def create(self, path, mode):
        self.files[path] = b''
        parent = os.path.dirname(path)
        if parent in self.directories:
            self.directories[parent].append(path)
        else:
            self.directories[parent] = [path]

    def read(self, path, size, offset):
        return self.files[path][offset:offset + size]

    def write(self, path, data, offset):
        self.files[path] = self.files[path][:offset] + data
        return len(data)

    def readdir(self, path, fh):
        return ['.', '..'] + self.directories.get(path, [])

    def unlink(self, path):
        del self.files[path]
        parent = os.path.dirname(path)
        self.directories[parent].remove(path)

if __name__ == '__main__':
    fuse = FUSE(MemoryFS(), sys.argv[1], foreground=True)