import random

swappedWins = 0
nonSwappedWins = 0

choices = [1,2,3]

iterations = 1000000
i = 0

while i < iterations:
    chosen = random.choice(choices)
    car = random.choice(choices)

    if car != chosen:
        newChoices = [car, chosen]
    else:
        newChoices = [car, random.choice([x for x in choices if x != chosen])]


    swap = random.random() < 0.5

    if swap:
        chosen = [x for x in newChoices if x != chosen][0]

    win = car == chosen

    if win and swap:
        swappedWins += 1

    if win and not swap:
        nonSwappedWins += 1
    i += 1

print("swappedWins: ", swappedWins)
print("nonSwappedWins: ", nonSwappedWins)


