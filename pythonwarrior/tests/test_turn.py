import mock
import unittest
from pythonwarrior.turn import Turn
from pythonwarrior.abilities.feel import Feel


class TestTurnWithActions(unittest.TestCase):
    def setUp(self):
        self.turn = Turn({'walk_': None, 'attack_': None})

    def test_should_have_no_action_performed_at_first(self):
        self.assertIsNone(self.turn.action)

    def test_should_be_able_to_perform_action_and_recall_it(self):
        self.turn.walk_()
        self.assertEqual(self.turn.action, ['walk_'])

    def test_should_include_arguments_passed_to_action(self):
        self.turn.walk_('forward')
        self.assertEqual(self.turn.action, ['walk_', 'forward'])

    def test_should_not_be_able_to_call_multiple_actions_per_turn(self):
        self.turn.walk_('forward')
        self.assertRaises(Exception, self.turn.attack_)


class TestTurnWithSenses(unittest.TestCase):
    def setUp(self):
        with mock.patch('pythonwarrior.abilities.feel.Feel.space',
                        mock.Mock()):
            self.feel = Feel(mock.Mock())
            self.turn = Turn({'feel': self.feel})

    def test_call_sense_with_any_argument_and_return_expected_results(self):
        self.assertEqual(self.turn.feel(), self.feel.perform())
        self.assertEqual(self.turn.feel('backward'),
                         self.feel.perform('backward'))
