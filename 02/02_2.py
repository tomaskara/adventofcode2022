with open('input.txt') as f:
    data = f.read().splitlines()

wins = ["A Y", "B Z", "C X"]
loses = ["A Z", "B X", "C Y"]
draws = ["A X", "B Y", "C Z"]

score = 0

for line in data:
    first, second = line.split(" ")

    if second == "Z":
        for w in wins:
            if first == w.split(" ")[0]:
                second = w.split(" ")[1]
        score += 6
    elif second == "Y":
        for d in draws:
            if first == d.split(" ")[0]:
                second = d.split(" ")[1]
        score += 3
    else:
        for ls in loses:
            if first == ls.split(" ")[0]:
                second = ls.split(" ")[1]

    if second == "Z":
        score += 3
    elif second == "Y":
        score += 2
    else:
        score += 1

print(score)