with open('input.txt') as f:
    data = f.read().splitlines()

calories = []
sum_cal = 0

for line in data:
    if line == "":
        calories.append(sum_cal)
        sum_cal = 0
    else:
        sum_cal += int(line)

calories.sort(reverse=True)
print(sum(calories[0:3]))