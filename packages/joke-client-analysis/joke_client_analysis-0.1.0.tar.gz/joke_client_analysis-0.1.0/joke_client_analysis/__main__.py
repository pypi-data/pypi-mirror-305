import argparse
from joke_client_analysis import analysis


def main(args):
    analysis(args.input_file, args.output_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-file', action='store')
    parser.add_argument('--output-file', action='store')

    args = parser.parse_args()
    main(args)
