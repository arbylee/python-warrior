import mock
import unittest

from pythonwarrior.abilities.bind import Bind
from pythonwarrior.units.base import UnitBase


class TestBind(unittest.TestCase):
    def setUp(self):
        self.bind = Bind(mock.Mock())

    def test_should_bind_recipient(self):
        receiver = UnitBase()
        self.bind.unit = mock.Mock(return_value=receiver)
        self.bind.perform()
        self.assertTrue(receiver.is_bound())

    def test_should_do_nothing_if_no_recipient(self):
        self.bind.unit = mock.Mock(return_value=None)
        self.bind.perform()
