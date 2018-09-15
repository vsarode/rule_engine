import json
import os
from os.path import dirname, abspath

from datetime import datetime

base_path = dirname(dirname(abspath(__file__)))


def get_source_to_rule_map():
    rule_objects = read_rules()
    m = {}
    for rule in rule_objects:
        source_signal, value_type, rule_value = parse_rule_string(rule)
        if (source_signal, value_type) in m:
            rule_and_value = {'rule': rule, 'value': rule_value}
            m[(source_signal, value_type)].append(rule_and_value)
        else:
            rule_and_value = {'rule': rule, 'value': rule_value}
            m[(source_signal, value_type)] = [rule_and_value]
    return m


def get_value_type(value):
    if value.isalpha() and value in ['LOW', 'HIGH']:
        value_type = "String"
        return value_type
    try:
        value_type = "Integer" if float(value) else None
        return value_type
    except:
        pass
    if value.isalpha and value in ['future']:
        value_type = "Datetime"
    return value_type


def derive_rule_value(rule_value):
    if rule_value in ['future']:
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    else:
        return rule_value


def parse_rule_string(rule):
    last_part = rule.split(' ')[-1].strip()
    value_type = get_value_type(last_part)
    source = rule.split(' ')[0]
    return source, value_type, last_part


def read_json_stream():
    file_path = (os.path.join(os.path.join(base_path, "assets"),
                              'raw_data.json'))
    f = open(file_path, "r").read()
    data = json.loads(f)
    return data


def read_rules():
    file_path = (os.path.join(os.path.join(base_path, "assets"),
                              'rules.txt'))
    f = open(file_path, "r")
    return f.readlines()


if __name__ == "__main__":
    m = get_source_to_rule_map()
    for  o in m[('ATL1', 'Integer')]:
        print(o['rule'])
        print(o['value'])

    # for o in read_json_stream():
    #     print(o)
    # print(read_rules())
    # for o in read_rules().readlines():
    # print(o)
