import unittest
import mock
from pythonwarrior.abilities.base import AbilityBase


class TestAbilityBase(unittest.TestCase):
    def setUp(self):
        unit = mock.Mock()
        self.ability = AbilityBase(unit)

    def test_should_have_offset_for_directions(self):
        self.assertEqual(self.ability.offset('forward'), [1, 0])
        self.assertEqual(self.ability.offset('right'), [0, 1])
        self.assertEqual(self.ability.offset('backward'), [-1, 0])
        self.assertEqual(self.ability.offset('left'), [0, -1])

    def test_should_have_offset_for_relative_forward_and_right_amounts(self):
        self.assertEqual(self.ability.offset('forward',
                                             forward=2), [2, 0])
        self.assertEqual(self.ability.offset('forward',
                                             forward=2, right=1), [2, -1])
        self.assertEqual(self.ability.offset('right',
                                             forward=2, right=1), [1, 2])
        self.assertEqual(self.ability.offset('backward',
                                             forward=2, right=1), [-2, 1])
        self.assertEqual(self.ability.offset('left',
                                             forward=2, right=1), [-1, -2])

    @mock.patch('pythonwarrior.abilities.base.AbilityBase.space')
    def test_should_fetch_unit_at_given_direction_with_distance(self,
                                                                mock_space):
        space = mock.Mock()
        space.unit = 'unit'
        mock_space.return_value = space
        self.assertEqual(self.ability.unit('right', 3, 1), 'unit')

    def test_should_have_no_description(self):
        self.assertEqual(self.ability.description(), None)

    def test_should_raise_an_exception_if_direction_isnt_recognized(self):
        self.assertRaises(Exception, self.ability.verify_direction, 'foo')

if __name__ == '__main__':
    unittest.main()
