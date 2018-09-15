from stream_filter.src.signal import Signal


class IntegerSignal(Signal):
    def __init__(self, signal, value, value_type):
        Signal.__init__(self, signal, value, value_type)

    def is_greater_than_value(self, value):
        if self.get_value() > float(value):
            return True
        else:
            return False

    def is_less_than_value(self, value):
        if self.get_value() < float(value):
            return True
        else:
            return False

    def is_equals_to_value(self, value):
        if self.get_value() == value:
            return True
        else:
            return False

    def is_not_equals_value(self, value):
        if not self.get_value() == value:
            return True
        else:
            return False