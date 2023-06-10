import argparse
from search import search
from tests import run_tests


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--fp", help="Data source")
    parser.add_argument("-n", help="Number of expected results")

    args = parser.parse_args()._get_kwargs()
    argTuples = dict(args)
    if not argTuples["fp"] and not argTuples["n"]:
        return run_tests()
    if argTuples["fp"] and not argTuples["n"]:
        raise ValueError("please provide the number of expected results")
    if argTuples["n"] and not argTuples["fp"]:
        raise ValueError("please provide a data source")
    print(search(argTuples["fp"], int(argTuples["n"])))


if __name__ == "__main__":
    main()
