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

    def returnDice2(self):
        return dices[2]

    def returnDice3(self):
        return dices[1]


dices = input().split()
q = int(input())
mydice = Dice(dices)
ans = ""

for i in range(q):
    u, f = input().split()
    for j in range(4):
        if mydice.returnDice() == u:
            for k in range(4):
                if mydice.returnDice3() == f:
                    ans = mydice.returnDice2()
                    break
                mydice.moveE()
                mydice.moveN()
                mydice.moveW()
        mydice.moveE()
    else:
        for k in range(4):
            if mydice.returnDice() == u:
                for l in range(4):
                    if mydice.returnDice3() == f:
                        ans = mydice.returnDice2()
                        break
                mydice.moveE()
                mydice.moveN()
                mydice.moveW()
            mydice.moveN()
    print(ans)
