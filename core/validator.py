import os

def file_exists(path):
    return os.path.isfile(path)

def directory_exists(path):
    return os.path.isdir(path)