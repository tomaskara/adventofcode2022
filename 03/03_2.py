import string

alphabet = [x for x in (string.ascii_lowercase+string.ascii_uppercase)]

with open('input.txt') as f:
    data = f.read().splitlines()

priorities = 0

for i in range(0, len(data), 3):
    group = data[i:i+3]
    common = set(group[0]).intersection(set(group[1]), set(group[2]))
    priorities += alphabet.index(common.pop()) + 1

print(priorities)


