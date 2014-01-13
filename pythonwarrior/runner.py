from optparse import OptionParser
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
        #TODO FINISH ME!!!
        options = OptionParser()
        return options
