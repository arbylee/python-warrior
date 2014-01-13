import shutil
import os
from jinja2 import Environment, PackageLoader


class PlayerGenerator(object):
    def __init__(self, level, previous_level):
        self.level = level
        self.previous_level = previous_level

    def generate(self):
        if self.level.number == 1:
            if not os.path.exists(self.level.player_path()):
                os.makedirs(self.level.player_path())
            shutil.copy(self.templates_path() +
                        '/player.py', self.level.player_path() + '/player.py')

        env = Environment(loader=PackageLoader('pythonwarrior', 'templates'))
        readme_template = env.get_template('README')

        readme = open(self.level.player_path() + '/README', 'w')
        readme.write(readme_template.render(level=self.level))
        readme.close()

    def templates_path(self):
        return os.path.normpath(os.path.dirname(__file__) + "/templates")
