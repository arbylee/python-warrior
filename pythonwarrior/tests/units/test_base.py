import unittest
import mock
from pythonwarrior.units.base import UnitBase


class TestUnitBase(unittest.TestCase):
    def setUp(self):
        self.unit = UnitBase()

    def test_should_have_attack_of_zero(self):
        self.assertEqual(self.unit.attack_power, 0)

    def test_should_be_dead_if_no_position(self):
        self.assertEqual(self.unit.position, None)
        self.assertFalse(self.unit.is_alive())

    def test_should_be_alive_if_has_position(self):
        self.unit.position = mock.Mock()
        self.assertTrue(self.unit.is_alive())

    def test_should_default_max_health_to_0(self):
        self.assertEqual(self.unit.max_health, 0)

    def test_should_default_health_to_max_health(self):
        self.unit.max_health = 10
        self.assertEqual(self.unit.health, 10)

    def test_should_subtract_health_when_taking_damage(self):
        self.unit.max_health = 10
        self.unit.take_damage(3)
        self.assertEqual(self.unit.health, 7)

    def test_should_set_position_to_none_when_out_of_health(self):
        self.max_health = 10
        self.unit.take_damage(10)
        self.assertEqual(self.unit.position, None)

    def test_should_return_name_as_string_representation(self):
        self.assertEqual(self.unit.name(), 'UnitBase')
        self.assertEqual(str(self.unit), 'UnitBase')

    @mock.patch('pythonwarrior.units.base.UnitBase.next_turn')
    @mock.patch('pythonwarrior.units.base.UnitBase.play_turn')
    def test_should_prepare_turn_by_calling_play_turn_with_next_turn_object(
            self, mock_play_turn, mock_next_turn):
        mock_next_turn.return_value = "next_turn"
        self.unit.prepare_turn()
        mock_play_turn.assert_called_with('next_turn')

    @mock.patch('pythonwarrior.units.base.UnitBase.next_turn')
    @mock.patch('pythonwarrior.units.base.Walk')
    def test_should_perform_action_when_calling_perform_on_turn(
            self, mock_walk, mock_next_turn):
        self.unit.position = mock.Mock()

        walk_object = mock.Mock(name='asdfs')
        mock_walk.return_value = walk_object

        self.unit.add_abilities('walk_')

        turn = mock.Mock(action=['walk_', 'backward'])
        mock_next_turn.return_value = turn

        self.unit.prepare_turn()
        self.unit.perform_turn()
        walk_object.perform.assert_called_once_with('backward')

    @mock.patch('pythonwarrior.units.base.UnitBase.next_turn')
    @mock.patch('pythonwarrior.units.base.Walk')
    def test_should_not_form_action_when_dead(self, mock_walk, mock_next_turn):
        self.unit.position = None

        walk_object = mock.Mock()
        mock_walk.return_value = walk_object
        walk_object.perform.side_effect = Exception('shouldnt be called')

        self.unit.add_abilities('walk_')
        turn = mock.Mock(action=['walk_', 'backward'])
        mock_next_turn.return_value = turn

        self.unit.prepare_turn()
        self.unit.perform_turn()

    def test_should_not_raise_exception_when_perform_turn_with_no_action(self):
        self.unit.prepare_turn()
        self.unit.perform_turn()

    @mock.patch('pythonwarrior.units.base.UnitBase.abilities')
    @mock.patch('pythonwarrior.units.base.Turn')
    def test_should_pass_abilities_to_new_turn_when_calling_next_turn(
            self, mock_turn, mock_abilities):
        mock_turn.return_value = 'turn'
        self.assertEqual(self.unit.next_turn(), 'turn')
        mock_turn.assert_called_once_with(mock_abilities)

    @mock.patch('pythonwarrior.units.base.Walk')
    def test_should_add_abilities_to_abilities_dict(self, mock_walk):
        mock_walk.return_value = 'walk'
        self.unit.add_abilities("walk_")
        self.assertEqual(self.unit.abilities, {'walk_': 'walk'})

    def test_should_appear_as_question_mark_on_map(self):
        self.assertEqual(self.unit.character, "?")

    def test_should_be_released_from_bonds_when_taking_damage(self):
        self.unit.max_health = 10
        self.unit.bind()
        self.assertTrue(self.unit.is_bound())
        self.unit.take_damage(2)
        self.assertFalse(self.unit.is_bound())

    def test_should_be_released_from_bonds_when_calling_release(self):
        self.unit.bind()
        self.unit.unbind()
        self.assertFalse(self.unit.is_bound())

    @mock.patch('pythonwarrior.units.base.UnitBase.next_turn')
    def test_should_not_perform_action_when_bound(self, mock_next_turn):
        self.unit.position = mock.Mock()
        self.unit.bind()
        self.unit.add_abilities("walk_")
        turn = mock.Mock()
        turn.action = ["walk_", "backward"]
        mock_next_turn.return_value = turn
        self.unit.prepare_turn()
        self.unit.perform_turn()


if __name__ == '__main__':
    unittest.main()
