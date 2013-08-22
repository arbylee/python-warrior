class Config(object):
    delay = None
    in_stream = None
    out_stream = None
    practice_level = None
    path_prefix = "."
    skip_input = None

    @staticmethod
    def reset():
        Config.delay = None
        Config.in_stream = None
        Config.out_stream = None
        Config.practice_level = None
        Config.path_prefix = "."
        Config.skip_input = None
