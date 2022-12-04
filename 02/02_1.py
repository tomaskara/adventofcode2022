with open('input.txt') as f:
    data = f.read().splitlines()

wins = ["A Y", "B Z", "C X"]
loses = ["A Z", "B X", "C Y"]
draws = ["A X", "B Y", "C Z"]

score = 0

for line in data:
    first, second = line.split(" ")
    if line in wins:
        score += 6
    elif line in draws:
        score += 3

    if second == "Z":
        score += 3
    elif second == "Y":
        score += 2
    else:
        score += 1

print(score)