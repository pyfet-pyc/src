from random import randint

money = 1000
tmp = money
while tmp > 0:
    print('你的总资产为:', money)
    needs_go_on = False
    tmp = money

first = randint(1, 6) + randint(1, 6)
print('玩家摇出了%d点' % first)
if first == 7 or first == 11:
    print('玩家胜!')
    money += debt
elif first == 2 or first == 3 or first == 12:
    print('庄家胜!')
    money -= debt
else:
    needs_go_on = True

print('你破产了, 游戏结束!')
