from stream_filter.src.parser_funcs import derive_rule_value, read_json_stream, \
    get_source_to_rule_map
from stream_filter.src.rule_factory_deligator import get_rule_func
from stream_filter.src.signal_factory import get_signal_object


def run_engine(entry, rule_map):
    signal_object = get_signal_object(entry['signal'], entry['value'],
                               entry['value_type'])
    if rule_map.get((entry['signal'], entry['value_type'])):
        rule_value = derive_rule_value(rule_map[(entry['signal'],
                                                 entry['value_type'])][
                                           'value'])
        rule_function = get_rule_func(rule_map[(entry['signal'],
                                                  entry['value_type'])][
                                            'rule'], signal_object)
        if rule_function and rule_function(rule_value):
            print(entry['signal'])


if __name__ == "__main__":
    rule_map = get_source_to_rule_map()
    # print(rule_map[('ATL1', 'Integer')]['rules'])
    # print(rule_map[('ATL1', 'Integer')]['value'])
    #
    # run_engine({'signal': 'ATL1', 'value_type': 'Integer', 'value':
    #     '2019'}, rule_map)
    data = read_json_stream()
    for entry in data:
        run_engine(entry, rule_map)
#
