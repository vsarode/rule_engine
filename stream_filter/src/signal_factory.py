from stream_filter.src.date_signal import DateSignal
from stream_filter.src.date_utils import get_date_from_string
from stream_filter.src.integer_signal import IntegerSignal
from stream_filter.src.string_signal import StringSignal


def get_signal_object(signal, value, value_type):
    if value_type == "Integer":
        return IntegerSignal(signal, float(value), value_type)
    if value_type == "String":
        return StringSignal(signal, value, value_type)
    if value_type == "Datetime":
        return DateSignal(signal, get_date_from_string(value), value_type)


if __name__ == "__main__":
    print(get_signal_object("ATL3", "2017-05-13 06:22:35", "Datetime"))
