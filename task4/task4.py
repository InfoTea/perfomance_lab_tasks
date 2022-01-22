import sys

input_string = sys.argv[1]

input_list = sorted([int(x) for x in input_string.split()])
min_element = input_list[0]
max_element = input_list[-1]

cost_dict = {}
for elem in input_list:
    cost_dict[elem] = cost_dict.get(elem, 0) + 1

keys_list = sorted(cost_dict.keys())

steps = 0

while min_element != max_element:
    if cost_dict[min_element] < cost_dict[max_element]:
        cost_dict[keys_list[1]] += cost_dict[min_element]
        steps += cost_dict[min_element] * (keys_list[1] - keys_list[0])
        del cost_dict[min_element]
        del keys_list[0]
    else:
        cost_dict[keys_list[-2]] += cost_dict[max_element]
        steps += cost_dict[max_element] * (keys_list[-1] - keys_list[-2])
        del cost_dict[max_element]
        del keys_list[-1]

    min_element = min(keys_list)
    max_element = max(keys_list)

print(steps)
