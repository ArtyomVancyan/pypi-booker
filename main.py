import os
from distutils.dir_util import copy_tree
from tempfile import TemporaryDirectory


def main():
    with TemporaryDirectory() as tempdir:
        copy_tree("template", tempdir)
        os.chdir(tempdir)
        os.system("python3 setup.py sdist bdist_wheel")
        os.system("python3 -m twine upload dist/*")


if __name__ == "__main__":
    main()
