import argparse
from twittp.model import TrendModel


def main():
    """Parses arguments using argparse and executes corresponding code"""
    command_parser = argparse.ArgumentParser(description='twittp -- Twitter Trend Prediction')
    subparsers = command_parser.add_subparsers(title="commands")

    build_model_parser = subparsers.add_parser('build-model', help='Build a '
                                               'model for other actions in '
                                               'twittp')

    build_model_parser.description = 'Build a model for other actions in twittp'

    build_model_parser.add_argument('tweets', help='The JSON file containing '
                                    'tweets from the Twitter API')
    build_model_parser.add_argument('trends', help='The JSON file containing '
                                    'trends from the Twitter API')
    build_model_parser.add_argument('--stopword', help='An optional CSV file '
                                    'containing words to ignore when '
                                    'constructing the model')
    build_model_parser.add_argument('--trend-preempt', help='The number of'
                                    'windows to preempt a trend by', default=0)
    build_model_parser.set_defaults(func=TrendModel.model_from_files)

    args = command_parser.parse_args()
    if args.func == TrendModel.model_from_files:
        model = TrendModel.model_from_files(args.tweets, args.trends,
                                           args.stopwords)
        print(model.serialize_model())


if __name__ == '__main__':
    main()
