import unittest

from stream_filter.src.date_signal import DateSignal
from stream_filter.src.date_utils import get_date_from_string
from stream_filter.src.integer_signal import IntegerSignal
from stream_filter.src.signal_factory import get_signal_object
from stream_filter.src.string_signal import StringSignal


class TestSignalFactory(unittest.TestCase):
    def test_is_getting_instance_of_string_class(self):
        signal_obj = get_signal_object("ALT1", "LOW", "String")
        self.assertIsInstance(signal_obj, StringSignal, "No type of object")

    def test_is_getting_instance_of_date_class(self):
        signal_obj = get_signal_object("ALT1", "2017-06-13 22:40:10",
                                       "Datetime")
        print(signal_obj)
        self.assertIsInstance(signal_obj, DateSignal, "No type of object")

    def test_is_getting_instance_of_integer_class(self):
        signal_obj = get_signal_object("ALT1", "20.50", "Integer")
        self.assertIsInstance(signal_obj, IntegerSignal, "No type of object")


class TestStringSignalRules(unittest.TestCase):
    def setUp(self):
        self.string_signal_object = StringSignal("ALT1", "LOW", "String")

    def test_is_equal_to_value_return_true(self):
        self.assertEqual(self.string_signal_object.is_equals_to_value("LOW"),
                         True)

    def test_is_equal_to_value_return_false(self):
        self.assertEqual(self.string_signal_object.is_equals_to_value("HIGH"),
                         False)

    def test_is_not_equal_to_value_return_true(self):
        self.assertEqual(self.string_signal_object.is_not_equals_value("HIGH"),
                         True)

    def test_is_not_equal_to_value_return_false(self):
        self.assertEqual(self.string_signal_object.is_not_equals_value("LOW"),
                         False)


class TestDateSignalRules(unittest.TestCase):
    def setUp(self):
        self.date_signal_object = DateSignal("ALT1",
                                             get_date_from_string("2017-06-13 " \
                                                                  "22:40:10"),
                                             "Datetime")

    def test_is_equal_to_value_return_true(self):
        self.assertEqual(self.date_signal_object.is_equals_to_value(
            "2017-06-13 22:40:10"),
            True)

    def test_is_equal_to_value_return_false(self):
        self.assertEqual(self.date_signal_object.is_equals_to_value(
            "2017-06-14 22:40:10"),
            False)

    def test_is_not_equal_to_value_return_true(self):
        self.assertEqual(self.date_signal_object.is_not_equals_value(
            "2017-06-14 22:40:10"),
            True)

    def test_is_not_equal_to_value_return_false(self):
        self.assertEqual(
            self.date_signal_object.is_not_equals_value("2017-06-13 22:40:10"),
            False)

    def test_is_greater_than_value_return_true(self):
        self.assertEqual(self.date_signal_object.is_greater_than_value(
            "2017-06-12 22:40:10"), True)

    def test_is_greater_than_value_return_false(self):
        self.assertEqual(self.date_signal_object.is_greater_than_value(
            "2017-06-14 22:40:10"), False)

    def test_is_less_than_value_return_true(self):
        self.assertEqual(self.date_signal_object.is_greater_than_value(
            "2017-06-12 22:40:10"), True)

    def test_is_less_than_value_return_false(self):
        self.assertEqual(self.date_signal_object.is_greater_than_value(
            "2017-06-14 22:40:10"), False)


class TestIntegerSignal(unittest.TestCase):
    def setUp(self):
        self.integer_signal = IntegerSignal("ALT2", 24.56, "Integer")

    def test_is_equal_to_value_return_true(self):
        self.assertEqual(self.integer_signal.is_equals_to_value(24.56),
                         True)

    def test_is_equal_to_value_return_false(self):
        self.assertEqual(self.integer_signal.is_equals_to_value(25),
                         False)

    def test_is_not_equal_to_value_return_true(self):
        self.assertEqual(self.integer_signal.is_not_equals_value(25),
                         True)

    def test_is_not_equal_to_value_return_false(self):
        self.assertEqual(
            self.integer_signal.is_not_equals_value(24.56),
            False)

    def test_is_greater_than_value_return_true(self):
        self.assertEqual(self.integer_signal.is_greater_than_value(23), True)

    def test_is_greater_than_value_return_false(self):
        self.assertEqual(self.integer_signal.is_greater_than_value(25), False)

    def test_is_less_than_value_return_true(self):
        self.assertEqual(self.integer_signal.is_greater_than_value(23), True)

    def test_is_less_than_value_return_false(self):
        self.assertEqual(self.integer_signal.is_greater_than_value(25), False)


if __name__ == "__main__":
    unittest.main()
