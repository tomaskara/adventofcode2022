import numpy as np
import copy
import sys

sys.setrecursionlimit(5000)

with open('input.txt') as f:
    data = f.read().splitlines()

array = np.array([list(x) for x in data])
numbers_array = np.vectorize(lambda x: ord(x) - ord('a')+1)(array)
numbers_array = np.where(numbers_array == -13, 1, numbers_array)
numbers_array = np.where(numbers_array == -27, 26, numbers_array)
horizontal_wall = np.zeros((1, numbers_array.shape[1]), dtype=int)
numbers_array = np.vstack((horizontal_wall, numbers_array,horizontal_wall))
vertical_wall = np.zeros((numbers_array.shape[0],1), dtype=int)
numbers_array = np.hstack((vertical_wall, numbers_array, vertical_wall))

start_nodes = tuple(np.argwhere(numbers_array == 1))
end_node = tuple(np.argwhere(array == "E")[0])
end_node = tuple(x + 1 for x in end_node)

coordinates_dict = {(i, j): 10000 for i in range(numbers_array.shape[0]) for j in range(numbers_array.shape[1])}




def step(cp, steps):
    if cp == end_node:
        return
    current_value = numbers_array[cp[0]][cp[1]]

    down_coordinates = (cp[0]+1,cp[1])
    down_value = numbers_array[down_coordinates]
    if down_value <= current_value + 1 and coordinates_dict[down_coordinates] > (steps + 1) and down_value != 0:
        coordinates_dict[down_coordinates] = steps + 1
        step(down_coordinates, steps+1)

    up_coordinates = (cp[0]-1,cp[1])
    up_value = numbers_array[up_coordinates]
    if up_value <= current_value + 1 and coordinates_dict[up_coordinates] > (steps + 1) and up_value != 0:
        coordinates_dict[up_coordinates] = steps + 1
        step(up_coordinates, steps+1)

    right_coordinates = (cp[0],cp[1]+1)
    right_value = numbers_array[right_coordinates]
    if right_value <= current_value + 1 and coordinates_dict[right_coordinates] > (steps + 1) and right_value != 0:
        coordinates_dict[right_coordinates] = steps + 1
        step(right_coordinates, steps+1)

    left_coordinates = (cp[0],cp[1]-1)
    left_value = numbers_array[left_coordinates]
    if left_value <= current_value + 1 and coordinates_dict[left_coordinates] > (steps + 1) and left_value != 0:
        coordinates_dict[left_coordinates] = steps + 1
        step(left_coordinates, steps+1)

    return coordinates_dict[end_node]


distances = []

for i in start_nodes:
    coordinates_dict[tuple(i)] = 1
    distances.append(step(tuple(i), 0))
    coordinates_dict = {(i, j): 10000 for i in range(numbers_array.shape[0]) for j in range(numbers_array.shape[1])}
print(min(distances))