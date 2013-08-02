import unittest
import mock
from pythonwarrior.units.base import UnitBase

class TestUnitBase(unittest.TestCase):
    def setUp(self):
        self.unit = UnitBase()

    def test_should_have_attack_of_zero(self):
        self.assertEqual(self.unit.attack_power(), 0)

    def test_should_be_dead_if_no_position(self):
        self.assertEqual(self.unit.position, None)
        self.assertFalse(self.unit.is_alive())

    def test_should_be_alive_if_has_position(self):
        self.unit.position = mock.Mock()
        self.assertTrue(self.unit.is_alive())

    def test_should_default_max_health_to_0(self):
        self.assertEqual(self.unit.max_health, 0)

    @mock.patch('pythonwarrior.units.base.UnitBase.max_health', 10)
    def test_should_default_health_to_max_health(self):
        self.assertEqual(self.unit.health(), 10)

    @mock.patch('pythonwarrior.units.base.UnitBase.max_health', 10)
    def test_should_subtract_health_when_taking_damage(self):
        self.unit.take_damage(3)
        self.assertEqual(self.unit.health(), 7)

    @mock.patch('pythonwarrior.units.base.UnitBase.max_health')
    def test_should_set_position_to_none_when_out_of_health(self, mock_max_health):
        mock_max_health.return_value = 10
        self.unit.take_damage(10)
        self.assertEqual(self.unit.position, None)

    def test_should_return_name_as_string_representation(self):
        self.assertEqual(self.unit.name(), 'UnitBase')
        self.assertEqual(str(self.unit), 'UnitBase')

    @mock.patch('pythonwarrior.units.base.UnitBase.next_turn')
    @mock.patch('pythonwarrior.units.base.UnitBase.play_turn')
    def test_should_prepare_turn_by_calling_play_turn_with_next_turn_object(self, mock_play_turn, mock_next_turn):
        mock_next_turn.return_value = "next_turn"
        self.unit.prepare_turn()
        mock_play_turn.assert_called_with('next_turn')

    @mock.patch('pythonwarrior.units.base.Walk')
    def test_should_add_abilities_to_abilities_dict(self, mock_walk):
        mock_walk.return_value = 'walk'
        self.unit.add_abilities("walk!")
        self.assertEqual(self.unit.abilities, {'walk!': 'walk'})

    def test_should_appear_as_question_mark_on_map(self):
        self.assertEqual(self.unit.character(), "?")

    @mock.patch('pythonwarrior.units.base.UnitBase.max_health', 10)
    def test_should_be_released_from_bonds_when_taking_damage(self):
        self.unit.bind()
        self.assertTrue(self.unit.is_bound())
        self.unit.take_damage(2)
        self.assertFalse(self.unit.is_bound())

    @unittest.skip
    def test_should_be_released_from_bonds_when_calling_release(self):
        assertTrue(False)

if __name__ == '__main__':
    unittest.main()
