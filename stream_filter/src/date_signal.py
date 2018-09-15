from stream_filter.src.date_utils import get_date_from_string
from stream_filter.src.signal import Signal


class DateSignal(Signal):
    def __init__(self, signal, value, value_type):
        Signal.__init__(self, signal, value, value_type)

    def is_greater_than_value(self, value):
        date = get_date_from_string(value)
        if self.get_value() > date:
            return True
        else:
            return False

    def is_less_than_value(self, value):
        date = get_date_from_string(value)
        if self.get_value() < date:
            return True
        else:
            return False

    def is_equals_to_value(self, value):
        date = get_date_from_string(value)
        if self.get_value() == date:
            return True
        else:
            return False

    def is_not_equals_value(self, value):
        date = get_date_from_string(value)
        if not self.get_value() == date:
            return True
        else:
            return False


if __name__ == "__main__":
    s = DateSignal("ALT1", get_date_from_string("2017-06-13 22:40:10"),
                   "Datetime")

