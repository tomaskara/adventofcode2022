import string

alphabet = [x for x in (string.ascii_lowercase+string.ascii_uppercase)]

with open('input.txt') as f:
    data = f.read().splitlines()

priorities = 0

for line in data:
    in_both = set(line[:len(line)//2]).intersection(set(line[len(line)//2:]))
    priorities += alphabet.index(in_both.pop())+1

print(priorities)


