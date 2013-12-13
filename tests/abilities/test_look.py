import mock
import unittest

from pythonwarrior.abilities.look import Look


class TestLook(unittest.TestCase):
    def setUp(self):
        self.unit = mock.Mock()
        self.look = Look(self.unit)

    def test_should_get_3_objects_at_position_from_offset(self):
        def fake_rel_space(x, y):
            mapping = {(1, 0): 1,
                       (2, 0): 2,
                       (3, 0): 3}
            return mapping[(x, y)]
        mock_rel_space = mock.Mock(side_effect=fake_rel_space)
        self.unit.position.relative_space = mock_rel_space

        self.assertEqual([1, 2, 3], self.look.perform('forward'))
        self.assertEqual(3, mock_rel_space.call_count)
