import argparse
import os
import pydoc
import sys

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(PROJECT_DIR)


def main():
    parser = argparse.ArgumentParser(description='Run analyzers here')

    parser.add_argument('catalog', type=str)

    catalog = parser.parse_args().catalog
    get_analyzer(os.path.splitext(catalog)[0]).run()


def get_analyzer(analyzer_name):
    args = 'src.analyzers.{analyzer_name}.{analyzer_class}'.format(
        analyzer_name=analyzer_name,
        analyzer_class=analyzer_name)
    return  pydoc.locate(args)()


if __name__ == '__main__':
    main()
