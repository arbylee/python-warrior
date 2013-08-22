import os
from jinja2 import Environment, PackageLoader
from pythonwarrior.level import Level


class PlayerGenerator(object):
    def __init__(self, level):
        self.level = level
        self.previous_level = Level(self.level.profile, self.level.number-1)

    def templates_path(self):
        return os.path.normpath(os.path.dirname(__file__) + "/templates")

    def generate(self):
        if self.level.number == 1:
            if not os.path.exists(self.level.player_path()):
                os.makedirs(self.level.player_path())
            player_file = open(self.level.player_path())
            template = open(self.templates_path + '/player.py', "w")
            player_file.write(template.read())
            template.close()
            player_file.close()

        env = Environment(loader=PackageLoader('pythonwarrior', 'templates'))
        readme_template = env.get_template('README')

        readme = open(self.level.player_path() + '/README', 'w')
        readme.write(readme_template.render())
        readme.close()
