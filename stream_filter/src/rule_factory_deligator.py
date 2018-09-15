# def get_rule(source, value_type, rule_string, signal_object):
#     func_map = {(source, value_type): get_rule_func(rule_string, signal_object)}
from stream_filter.src.date_signal import DateSignal
from stream_filter.src.date_utils import get_date_from_string
from stream_filter.src.integer_signal import IntegerSignal
from stream_filter.src.signal import Signal


def get_value_type(value):
    if value.isalpha() and value in ['LOW', "HIGH"]:
        value_type = "String"
        return value_type
    try:
        value_type = "Integer" if float(value) else None
        return value_type
    except:
        pass
    value_type = "Datetime"
    return value_type


def parse_rule_string(rule):
    last_part = rule.split(' ')[-1]
    value_type = get_value_type(last_part)
    source = rule.split(' ')[0]
    rule_string = rule.split(' ')[1:]
    return source, value_type, rule_string


def get_rule_func(rule_string, signal_object):
    truth_table = [x in rule_string.split(' ') for x in ['above', 'greater',
                                                         'future']]
    if True in truth_table:
        return signal_object.is_greater_than_value

    truth_table = [x in rule_string.split(' ') for x in ['below', 'leaser',
                                                         'less']]
    if True in truth_table:
        return signal_object.is_less_than_value

    truth_table = [x in rule_string.split(' ') for x in ['equal', 'equals',
                                                         'never']]
    if True in truth_table:
        return signal_object.is_equals_to_value

    truth_table = [x in rule_string.split(' ') for x in ['not equal',
                                                         'not equals']]
    if True in truth_table:
        return signal_object.is_not_equals_value


if __name__ == "__main__":
    print(parse_rule_string('ATL3 should not be in future'))
    sig_obj = DateSignal("ATL1", get_date_from_string("2017-06-13 22:40:10"),
                      "Datetime")
    # import pdb; pdb.set_trace()

    func = get_rule_func("ATL3 should not be in future", sig_obj)
    print(func)

    if func:
        print(func("2017-06-12 22:40:10"))
    else:
        print('chal bhag')
