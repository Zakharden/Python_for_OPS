import argparse

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("yaml_file")

    args = parser.parse_args()

    print(args)