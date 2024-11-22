import pdb

from os import listdir
from os.path import join,isfile


def iterate_folder(folder):
    for path in sorted(listdir(folder)):
        full_path = join(folder, path)

        if "venv" in path or "git" in path:
            continue

        if isfile(full_path):
            print(f"file ==> {full_path}")
        else:
            iterate_folder(full_path)

iterate_folder("ex")
