import glob
import os

from pythonwarrior.config import Config
from pythonwarrior.level import Level
from pythonwarrior.player_generator import PlayerGenerator
from pythonwarrior.profile import Profile
from pythonwarrior.tower import Tower
from pythonwarrior.ui import UI


class Game(object):
    def __init__(self):
        self._profile = None
        self._current_level = None
        self._next_level = None

    def start(self):
        UI.puts('Welcome to Python Warrior')
        if os.path.exists(Config.path_prefix + '/.profile'):
            self._profile = Profile.load(Config.path_prefix + '/.profile')
        else:
            if not os.path.exists(Config.path_prefix + '/pythonwarrior'):
                self.make_game_directory()

        if self.profile().epic:
            if self.profile().level_after_epic():
                self.go_back_to_normal_mode()
            else:
                self.play_epic_mode()
        else:
            self.play_normal_mode()

    def make_game_directory(self):
        if UI.ask("No pythonwarrior directory found, \
                  would you like to create one?"):
            os.mkdir(Config.path_prefix + '/pythonwarrior')
        else:
            UI.puts('Unable to continue without directory.')
            raise Exception("Unable to continue without directory.")

    def play_epic_mode(self):
        if Config.delay:
            Config.delay = Config.delay/2

        self.profile().current_epic_score = 0
        self.profile().current_epic_grades = {}
        if Config.practice_level:
            self._current_level = self._next_level = None
            self.profile().level_number = Config.practice_level
            self.play_current_level()
        else:
            playing = True
            while playing:
                self._current_level = self._next_level = None
                self.profile().level_number += 1
                playing = self.play_current_level()
            self.profile().save()

    def play_normal_mode(self):
        if Config.practice_level:
            UI.puts("Unable to practice level while not in epic mode,"
                    "remove -l options")
        else:
            if self.current_level().number == 0:
                self.prepare_next_level()
                UI.puts("First level has been generated."
                        "See the pythonwarrior/%s/README for instructions."
                        % self.profile().directory_name())
            else:
                self.play_current_level()

    def play_current_level(self):
        continue_play = True
        UI.puts("Starting level %d" % self.current_level().number)
        self.current_level().play()
        if self.current_level().is_passed():
            if self.next_level().exists():
                UI.puts("Success! You have found the stairs.")
            else:
                UI.puts("CONGRATULATIONS! You have climbed to the top "
                        "of the tower and rescued the fair maiden Python")
                continue_play = False
            self.current_level().tally_points()
            if self.profile().epic:
                if self.final_report() and not continue_play:
                    UI.puts(self.final_report())
            else:
                self.request_next_level()
        else:
            continue_play = False
            UI.puts("Sorry, you failed level %d. "
                    "Change your script and try again." %
                    self.current_level().number)
            if (not Config.skip_input) and self.current_level().clue \
                    and UI.ask("Would you like to read the "
                               "additional clues for this level?"):
                        UI.puts(self.current_level().clue)
        return continue_play

    def request_next_level(self):
        if not Config.skip_input:
            if self.next_level().exists():
                if UI.ask('Would you like to continue on to the next level?'):
                    self.prepare_next_level()
                    UI.puts('See the updated README in the pythonwarrior/' +
                            self.profile().directory_name() +
                            ' directory')
                else:
                    UI.puts('Staying on current level.'
                            'Try to earn more points next time.')

            else:
                if UI.ask('Would you like to continue on to epic mode?'):
                    self.prepare_epic_mode()
                    UI.puts('Run pythonwarrior again to play epic mode.')
                else:
                    UI.puts("Staying on current level. "
                            "Try to earn more points next time.")

    def prepare_next_level(self):
        self.next_level().load_level()
        PlayerGenerator(self.next_level(), self.current_level()).generate()
        self.profile().level_number += 1
        self.profile().save()

    def prepare_epic_mode(self):
        self.profile().enable_epic_mode()
        self.profile().level_number = 0
        self.profile().save()

    def go_back_to_normal_mode(self):
        self.profile().enable_normal_mode()
        self.prepare_next_level()
        UI.puts('Another level has been added since you started epic, '
                'going back to normal mode')
        UI.puts('See the updated README in the '
                'pythonwarrior/%s directory' % self.profile().directory_name())

    def profiles(self):
        return map(lambda profile: Profile.load(profile), self.profile_paths())

    def profile_paths(self):
        return glob.glob(Config.path_prefix + '/pythonwarrior/**/.profile')

    def profile(self):
        if self._profile is None:
            self._profile = self.choose_profile()
        return self._profile

    def new_profile(self):
        profile = Profile()
        profile.tower_path = UI.choose('tower', self.towers()).path
        profile.warrior_name = UI.request('Enter a name for your warrior: ')
        return profile

    def towers(self):
        return map(lambda path: Tower(path), self.tower_paths())

    def tower_paths(self):
        tower_paths = glob.glob(os.path.normpath(os.path.abspath(__file__) +
                                                 '/../towers/*'))
        tower_paths = filter(lambda path: os.path.isdir(path), tower_paths)
        return tower_paths

    def current_level(self):
        if not self._current_level:
            self._current_level = self.profile().current_level()
        return self._current_level

    def next_level(self):
        if not self._next_level:
            self._next_level = self.profile().next_level()
        return self._next_level

    def final_report(self):
        average_grade = self.profile().calculate_average_grade()
        if average_grade and not Config.practice_level:
            report = ""
            report += ("Your average grade for this tower is: %s\n\n" %
                       Level.grade_letter(average_grade))

    def choose_profile(self):
        profile = UI.choose('profile',
                            self.profiles() + [['new', 'New Profile']])
        if profile == 'new':
            profile = self.new_profile()
            if filter(lambda prof: prof.player_path == profile.player_path,
                      self.profiles()):
                if UI.ask('Are you sure you want to replace your existing'
                          'profile for this tower?'):
                    UI.puts('Replacing existing profile.')
                    return profile
                else:
                    UI.puts('Not replacing profile.')
                    raise Exception('Not replacing profile')
            else:
                return profile
        else:
            return profile
