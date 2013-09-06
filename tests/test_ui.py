import mock
import unittest

from pythonwarrior.config import Config
from pythonwarrior.ui import UI
from io import BytesIO


class TestUI(unittest.TestCase):
    def setUp(self):
        self.ui = UI()
        self.config = Config
        self.config.delay = None
        self.out_stream = BytesIO()
        self.in_stream = BytesIO()
        self.config.out_stream = self.out_stream
        self.config.in_stream = self.in_stream

    def test_should_add_puts_to_out_stream(self):
        self.ui.puts("hello")
        self.assertEqual(self.out_stream.getvalue(), "hello\n")

    def test_should_add_write_to_out_stream_without_newline(self):
        self.ui.write("hello")
        self.out_stream.seek(0)
        self.assertEqual(self.out_stream.getvalue(), "hello")

    def test_should_fetch_gets_from_in_stream(self):
        self.in_stream.write("bar")
        self.in_stream.seek(0)
        self.assertEqual(self.ui.gets(), "bar")

    def test_should_gets_should_return_empty_string_if_no_input(self):
        self.config.in_stream = None
        self.assertEqual(self.ui.gets(), "")

    def test_should_request_text_input(self):
        self.in_stream.write("bar")
        self.in_stream.seek(0)
        self.assertEqual(self.ui.request("foo"), "bar")
        self.assertEqual(self.out_stream.getvalue(), "foo")

    @mock.patch('pythonwarrior.ui.UI.request')
    def test_should_ask_for_yes_no_and_return_true_when_yes(self, mock_req):
        mock_req.return_value = 'y'
        self.assertTrue(self.ui.ask("foo?"))

    @mock.patch('pythonwarrior.ui.UI.request')
    def test_should_ask_for_yes_no_and_return_false_when_no(self, mock_req):
        mock_req.return_value = 'n'
        self.assertFalse(self.ui.ask("foo?"))

    @mock.patch('pythonwarrior.ui.UI.request')
    def test_should_ask_for_yes_no_and_return_false_for_any_input(self,
                                                                  mock_req):
        mock_req.return_value = 'aklhasdf'
        self.assertFalse(self.ui.ask("foo?"))

    @mock.patch('pythonwarrior.ui.UI.request')
    def test_should_present_multiple_options_and_return_selected_one(self,
                                                                     mock_req):
        mock_req.return_value = '2'
        self.assertEqual(self.ui.choose('item', ['foo', 'bar', 'test']), 'bar')
        output = self.out_stream.getvalue()
        assert '[1] foo' in output
        assert '[2] bar' in output
        assert '[3] test' in output

    @mock.patch('pythonwarrior.ui.UI.request')
    def test_choose_should_accept_array_as_option(self, mock_req):
        mock_req.return_value = 3
        self.assertEqual(
            self.ui.choose('item', ['foo', 'bar', ['tower', 'easy']]),
            'tower'
        )
        assert '[3] easy' in self.out_stream.getvalue()

    @mock.patch('pythonwarrior.ui.UI.puts')
    @mock.patch('pythonwarrior.ui.UI.gets')
    @mock.patch('pythonwarrior.ui.UI.request')
    def test_choose_should_return_option_without_prompt_if_only_one_item(
            self, mock_req, mock_gets, mock_puts):
        self.assertEqual(self.ui.choose('item', ['foo']), 'foo')
        assert not mock_puts.called
        assert not mock_gets.called

    def test_choose_should_return_first_value_in_array_if_one_item(self):
        self.assertEqual(self.ui.choose('item', [['foo', 'bar']]), 'foo')

    @mock.patch('time.sleep')
    @mock.patch('pythonwarrior.ui.UI.puts')
    def test_should_delay_after_puts_when_specified(self,
                                                    mock_puts,
                                                    mock_sleep):
        self.config.delay = 1.3
        self.ui.puts_with_delay('foo')
        mock_puts.assert_called_with('foo')
        mock_sleep.assert_called_with(1.3)

    @mock.patch('time.sleep')
    @mock.patch('pythonwarrior.ui.UI.puts')
    def test_should_not_delay_puts_when_no_delay(self,
                                                 mock_puts,
                                                 mock_sleep):
        self.ui.puts_with_delay('foo')
        mock_puts.assert_called_with('foo')
        assert not mock_sleep.called
