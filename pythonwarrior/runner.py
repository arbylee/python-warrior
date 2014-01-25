import argparse

from pythonwarrior.config import Config
from pythonwarrior.game import Game


class Runner(object):
    def __init__(self, arguments, stdin, stdout):
        self.arguments = arguments
        self.stdin = stdin
        self.stdout = stdout
        self.game = Game()

    def run(self):
        Config.in_stream = self.stdin
        Config.out_stream = self.stdout
        Config.delay = 0.2
        self.parse_options()
        self.game.start()

    def parse_options(self):
        parser = argparse.ArgumentParser(description='Process options')
        parser.add_argument('-d', '--directory', action=SetDirectory,
                            help='Run under given directory')
        parser.add_argument('-l', '--level', action=SetLevel, type=int,
                            help='Practice level on epic')
        parser.add_argument('-s', '--skip', action=SkipInput, nargs=0,
                            help='Skip user input')
        parser.add_argument('-t', '--time', action=SetDelay, type=float,
                            help='Delay each turn by seconds')

        parser.parse_args()


class SetDirectory(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        Config.path_prefix = values


class SetLevel(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        Config.practice_level = values


class SkipInput(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        Config.skip_input = True


class SetDelay(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        Config.delay = values
