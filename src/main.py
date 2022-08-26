import argparse


from utils import print_args, try_catch
from ToolChain import ToolChain
from toolhub import factory


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, required=True, help='path to config')
    ### more arguments ###

    return parser.parse_args()


# @try_catch
def main(args):
    chain = ToolChain(factory, args.config)
    chain.run()


if __name__ == '__main__':
    args = get_args()
    print_args(args)
    main(args)