import random
target = random.randint(1, 99)
my = int(input("输入数字:"))
if my < 1 or my > 99:
    print("退出")
    exit()
elif my > target:
    print('你赢了')
elif my < target:
    print('你输了')
else:
    print("平手")
