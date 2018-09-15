from stream_filter.src.date_utils import get_date_from_string
from abc import ABC, abstractmethod

class Signal(ABC):
    def __init__(self, signal, value, value_type):
        self.__signal = signal
        self.__value = value
        self.__value_type = value_type

    def get_signal(self):
        return self.__signal

    def get_value(self):
        return self.__value

    def get_value_type(self):
        return self.__value_type

    def set_signal(self, signal):
        self.__signal = signal

    def set_value(self, value):
        self.__value = value

    def set_value_type(self, value_type):
        self.__value_type = value_type

    @abstractmethod
    def is_greater_than_value(self, value):
        pass

    @abstractmethod
    def is_less_than_value(self, value):
        pass

    @abstractmethod
    def is_equals_to_value(self, value):
        pass

    @abstractmethod
    def is_not_equals_value(self, value):
        pass
