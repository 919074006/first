shop=[
    ["联想电脑",6000],
    ["Iphone 16x plus",15000],
    ["PS5游戏机",3500],
    ["老干妈",7.5],
    ["老于妈",5.5],
    ["卫龙辣条",10],
    ["HUA WEI watch",1200],
    ["MAC PC",15000]
]
coupon=[
    ["联想电脑",6000],
    ["卫龙辣条",10]
]
mycart=[]
salary=input("请输入您的余额：")
salary=int(salary)
M=salary
import random
S=random.choice(coupon)   #choice随机获得列表中的某个列表数据
if salary<0:
 print("对不起，您的输入有误，请重新输入！")
 salary = input("请输入您的余额：")
 salary = int(salary)
 M = salary
else:
 print("恭喜您获得",S[0],"优惠券")
while True:
     for index, value in enumerate(shop):
         print(index, value)
     choes = input("请输入商品序号：")
     if choes.isdigit():
         choes = int(choes)
         if choes < len(shop):
             if salary >= shop[choes][1]:
                 mycart.append(shop[choes])
                 salary = salary - shop[choes][1]
                 print("恭喜，添加成功！您的余额还剩：￥", salary)
                 print("已有", mycart)
             else:
                 print("穷鬼，钱不够，请选择其他商品！")
         elif choes >= len(shop):
             print("对不起，您的输入有误，请重新输入！")
     elif choes == 'Q' or choes == 'q':
         print("欢迎下次光临，再见！")
         break
     else:
         print("对不起，您的输入有误，请重新输入！")

some=mycart.count(["联想电脑",6000])
same=mycart.count(["卫龙辣条",10])
J=(M-salary)/10
J=int(J)
print("您可获得积分",J)
if S==["联想电脑",6000]:
    salary = salary + some * 3000
elif S==["卫龙辣条",10] and same>3:
    salary=salary+300
    print("优惠券优惠后","您剩余",salary)



