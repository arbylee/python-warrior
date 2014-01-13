import mock
import unittest
from pythonwarrior.units.warrior import Warrior


class TestWarrior(unittest.TestCase):
    def setUp(self):
        self.warrior = Warrior()

    def test_should_default_name_to_warrior(self):
        self.assertEqual(self.warrior.name(), 'Warrior')

    def test_should_be_able_to_set_name(self):
        self.warrior.name_attr = "Joe"
        self.assertEqual(self.warrior.name(), "Joe")
        self.assertEqual(str(self.warrior), "Joe")

    def test_should_have_20_max_health(self):
        self.assertEqual(self.warrior.max_health, 20)

    def test_should_have_0_score_at_beginning_and_be_able_to_earn_points(self):
        self.assertEqual(self.warrior.score, 0)
        self.warrior.earn_points(5)
        self.assertEqual(self.warrior.score, 5)

    @mock.patch('pythonwarrior.units.warrior.Warrior.player')
    def test_should_call_player_play_turn_and_pass_turn_to_player(self,
                                                                  mock_player):
        returned_player = mock.Mock()
        mock_player.return_value = returned_player
        self.warrior.play_turn('turn')
        mock_player.assert_called_once_with()
        returned_player.play_turn.assert_called_once_with('turn')

    @unittest.skip
    @mock.patch('pythonwarrior.units.warrior.player.Player')
    def test_should_instantiate_player_first_time_and_return_same_object_next_time(self, mock_player):
        player = mock.Mock()
        mock_player.return_value = player
        self.assertEqual(self.warrior.player(), player)
        self.assertEqual(self.warrior.player(), player)

    def test_should_have_an_attack_power_of_5(self):
        self.assertEqual(self.warrior.attack_power, 5)

    def test_should_have_a_shoot_power_of_3(self):
        self.assertEqual(self.warrior.shoot_power, 3)

    def test_should_appear_as_AT_symbol_on_map(self):
        self.assertEqual(self.warrior.character, "@")

    def test_should_be_able_to_add_golem_abilities_which_are_used_on_base_golem(self):
        self.warrior.add_golem_abilities("walk")
        self.assertEqual(self.warrior.base_golem().abilities.keys(), ["walk"])
