#  т.к. в условие нет ограничений на объём памяти, решал через рекурсию.
#  можно для экономии памяти выполнить решение через циклы

import sys
import json
import copy

path_values = sys.argv[1]
path_tests = sys.argv[2]


def find_value(list_dict, id):
    for count, value in enumerate(list_dict['values']):
        if value['id'] == id:
            return value['value']
    return None


def rewrite_json(list_where, list_from):
    for dictionary in list_where:
        id = dictionary['id']
        if 'value' in dictionary:
            dictionary['value'] = find_value(list_from, id)
        if 'values' in dictionary:
            rewrite_json(dictionary['values'], list_from)
    return list_where


with open(path_values, 'r') as file:
    data_values = json.load(file)

with open(path_tests, 'r') as file:
    data_tests = json.load(file)

new_data = copy.deepcopy(data_tests)
new_data['tests'] = rewrite_json(data_tests['tests'], data_values)

with open('report.json', 'w') as file:
    json.dump(data_tests, file, indent=1, ensure_ascii=False)
