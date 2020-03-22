import argparse
import os
import imp
import pydoc
import sys

sys.path.append("C:\Users\RoiHa\PycharmProjects\dependencies")

import src.analyzers as analyzers
ANALYZERS_DIR = os.path.abspath(analyzers.__file__)


def main():
    parser = argparse.ArgumentParser(description='Example with non-optional arguments')

    parser.add_argument('catalog', type=str)

    catalog = parser.parse_args().catalog
    run_analyzer(os.path.splitext(catalog)[0])


def run_analyzer(analyzer_name):
    args = 'src.analyzers.{analyzer_name}.{analyzer_class}'.format(
        analyzer_name=analyzer_name,
        analyzer_class=analyzer_name)
    return  pydoc.locate(args)


if __name__ == '__main__':
    main()
