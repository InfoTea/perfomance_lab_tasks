import sys

file1_name = sys.argv[1]
file2_name = sys.argv[2]

with open(file1_name, 'r') as file:
    file1 = file.read().split()

with open(file2_name, 'r') as file:
    file2 = file.read().split()

x_center, y_center, radius = tuple(float(coord) for coord in file1)
coords = [(float(file2[i - 1]), float(file2[i])) for i in range(1, len(file2), 2)]

epsilon = sys.float_info.epsilon

for x_point, y_point in coords:
    x = abs(x_center - x_point)
    y = abs(y_center - y_point)
    if abs(x ** 2 + y ** 2 - radius ** 2) < epsilon:
        print(0)
    elif x ** 2 + y ** 2 < radius ** 2:
        print(1)
    else:
        print(2)
