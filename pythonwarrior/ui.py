from pythonwarrior.config import Config
import time


class UI(object):
    @staticmethod
    def puts(msg):
        if Config.out_stream:
            return Config.out_stream.write(msg + "\n")

    @staticmethod
    def puts_with_delay(msg):
        result = UI.puts(msg)
        if Config.delay:
            time.sleep(Config.delay)
        return result

    @staticmethod
    def write(msg):
        if Config.out_stream:
            return Config.out_stream.write(msg)

    @staticmethod
    def gets():
        if Config.in_stream:
            return Config.in_stream.readline()
        else:
            return ''

    @staticmethod
    def request(msg):
        UI.write(msg)
        return UI.gets().rstrip()

    @staticmethod
    def ask(msg):
        return UI.request("%s [yn] " % msg) == 'y'

    @staticmethod
    def choose(item, options):
        if len(options) == 1:
            response = options[0]
        else:
            for idx, option in enumerate(options):
                if type(option) == list:
                    UI.puts("[%d] %s" % (idx+1, option[-1]))
                else:
                    UI.puts("[%d] %s" % (idx+1, option))
            choice = UI.request("Choose %s by typing the number: " % item)
            response = options[int(choice)-1]
        if type(response) == list:
            return response[0]
        else:
            return response
