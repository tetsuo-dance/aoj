class Dice:

    def __init__(self, my_dices):
        dices = my_dices

    def __init__(self, my_dices):
        self.dices = my_dices

    def moveE(self):
        new_dice0 = self.dices[3]
        new_dice1 = self.dices[1]
        new_dice2 = self.dices[0]
        new_dice3 = self.dices[5]
        new_dice4 = self.dices[4]
        new_dice5 = self.dices[2]
        self.dices[0] = new_dice0
        self.dices[1] = new_dice1
        self.dices[2] = new_dice2
        self.dices[3] = new_dice3
        self.dices[4] = new_dice4
        self.dices[5] = new_dice5

    def moveN(self):
        new_dice0 = self.dices[1]
        new_dice1 = self.dices[5]
        new_dice2 = self.dices[2]
        new_dice3 = self.dices[3]
        new_dice4 = self.dices[0]
        new_dice5 = self.dices[4]
        self.dices[0] = new_dice0
        self.dices[1] = new_dice1
        self.dices[2] = new_dice2
        self.dices[3] = new_dice3
        self.dices[4] = new_dice4
        self.dices[5] = new_dice5

    def moveS(self):
        new_dice0 = self.dices[4]
        new_dice1 = self.dices[0]
        new_dice2 = self.dices[2]
        new_dice3 = self.dices[3]
        new_dice4 = self.dices[5]
        new_dice5 = self.dices[1]
        self.dices[0] = new_dice0
        self.dices[1] = new_dice1
        self.dices[2] = new_dice2
        self.dices[3] = new_dice3
        self.dices[4] = new_dice4
        self.dices[5] = new_dice5

    def moveW(self):
        new_dice0 = self.dices[2]
        new_dice1 = self.dices[1]
        new_dice2 = self.dices[5]
        new_dice3 = self.dices[0]
        new_dice4 = self.dices[4]
        new_dice5 = self.dices[3]
        self.dices[0] = new_dice0
        self.dices[1] = new_dice1
        self.dices[2] = new_dice2
        self.dices[3] = new_dice3
        self.dices[4] = new_dice4
        self.dices[5] = new_dice5


def moves(dice, ops):
    for i in range(len(ops)):
        if ops[i] == "S":
            dice.moveS()
        elif ops[i] == "N":
            dice.moveN()
        elif ops[i] == "W":
            dice.moveW()
        else:
            dice.moveE()


dices = input().split()
dices2 = input().split()
ans = "No"
dice_moves = ["W", "W", "W", "W", "NW", "WW"]
mydice = Dice(dices)
mydice2 = Dice(dices2)

for j in range(len(dice_moves)):
    moves(mydice, dice_moves[j])
    for k in range(4):
        if mydice.dices[0] == mydice2.dices[0] and mydice.dices[1] == mydice2.dices[1] \
                and mydice.dices[2] == mydice2.dices[2] and mydice.dices[3] == mydice2.dices[3] \
                and mydice.dices[4] == mydice2.dices[4] and mydice.dices[5] == mydice2.dices[5]:
            ans = "Yes"
        mydice.moveN()
print(ans)
