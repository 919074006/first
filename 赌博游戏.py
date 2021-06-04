print("开始游戏！")
money = 5000
print("您有",money,"个金币")

import random
num = random.randint(1,100)

t = 0
b = money - 500
while t < 16 and b > -500:
    number = input("请输入您要猜的数：")
    number = int(number)
    if number > num:
        print("大了！")
        print("剩余",b,"个金币")
        t = t + 1
    elif number < num:
        print("小了！")
        print("剩余",b,"个金币")
        t = t + 1
    else:
        print("恭喜猜中！本次数字为：",num,"   奖励3000金币！")
        b = b + 3000
        print("剩余", b, "个金币")
        import random
        num = random.randint(1,100)
    b = b - 500



