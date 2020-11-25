class Dice:

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

    def returnDice(self):
        return self.dices[0]


dices1 = input().split()
dice1 = Dice(dices1)

dices2 = input().split()
dice2 = Dice(dices2)
ans = "No"

for i in range(4):
    if dice1.dices[0] == dice2.dices[0] and dice1.dices[1] == dice2.dices[1] \
            and dice1.dices[2] == dice2.dices[2] and dice1.dices[3] == dice2.dices[3] \
            and dice1.dices[4] == dice2.dices[4] and dice1.dices[5] == dice2.dices[5]:
        ans = "Yes"
    dice1.moveE()

for i in range(4):
    if dice1.dices[0] == dice2.dices[0] and dice1.dices[1] == dice2.dices[1] \
            and dice1.dices[2] == dice2.dices[2] and dice1.dices[3] == dice2.dices[3] \
            and dice1.dices[4] == dice2.dices[4] and dice1.dices[5] == dice2.dices[5]:
        ans = "Yes"
    dice1.moveN()

print(ans)
