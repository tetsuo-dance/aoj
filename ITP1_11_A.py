class Dice:

    def __init__(self, my_dices):
        dices = my_dices

    def moveE(self):
        new_dice0 = dices[3]
        new_dice1 = dices[1]
        new_dice2 = dices[0]
        new_dice3 = dices[5]
        new_dice4 = dices[4]
        new_dice5 = dices[2]
        dices[0] = new_dice0
        dices[1] = new_dice1
        dices[2] = new_dice2
        dices[3] = new_dice3
        dices[4] = new_dice4
        dices[5] = new_dice5

    def moveN(self):
        new_dice0 = dices[1]
        new_dice1 = dices[5]
        new_dice2 = dices[2]
        new_dice3 = dices[3]
        new_dice4 = dices[0]
        new_dice5 = dices[4]
        dices[0] = new_dice0
        dices[1] = new_dice1
        dices[2] = new_dice2
        dices[3] = new_dice3
        dices[4] = new_dice4
        dices[5] = new_dice5

    def moveS(self):
        new_dice0 = dices[4]
        new_dice1 = dices[0]
        new_dice2 = dices[2]
        new_dice3 = dices[3]
        new_dice4 = dices[5]
        new_dice5 = dices[1]
        dices[0] = new_dice0
        dices[1] = new_dice1
        dices[2] = new_dice2
        dices[3] = new_dice3
        dices[4] = new_dice4
        dices[5] = new_dice5

    def moveW(self):
        new_dice0 = dices[2]
        new_dice1 = dices[1]
        new_dice2 = dices[5]
        new_dice3 = dices[0]
        new_dice4 = dices[4]
        new_dice5 = dices[3]
        dices[0] = new_dice0
        dices[1] = new_dice1
        dices[2] = new_dice2
        dices[3] = new_dice3
        dices[4] = new_dice4
        dices[5] = new_dice5

    def returnDice(self):
        return dices[0]


dices = input().split()
moves = list(input())
mydice = Dice(dices)
for i in range(len(moves)):
    if moves[i] == "E":
        mydice.moveE()
    elif moves[i] == "N":
        mydice.moveN()
    elif moves[i] == "S":
        mydice.moveS()
    else:
        mydice.moveW()

print(mydice.returnDice())
