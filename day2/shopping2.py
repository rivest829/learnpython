# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
# shopping的改良版
pruduct = [['book', 89], ['guitar', '2100'], ['keyboard', 5320], ['Mac pro', 10200], ['Human being', 340000]]
money = input('Please input the money you have:')
cart = []
if money.isdigit():
    while True:
        money = int(money)
        if money >= 0:
            print('-------shoplist--------')
            for a, b in enumerate(pruduct):
                print(a, b)
        else:
            print('Money cannot be minus')
        num = input('Choice the goods:')
        if num.isdigit():
            num = int(num)
            if num >= 0 and num < len(pruduct):
                if num < money:
                    cart.append(pruduct[num])
                    money = money - int(pruduct[num][1])
                    print('You have bought:', pruduct[num][0])
                    print('You left:', money, 'Yuan')
        elif num == 'q':
            print('-------You have---------')
            for i in cart:
                print(i)
            print('You left:', money)
            exit()
        else:
            print('Invalid input!!!!')
elif money == 'q':
    print('Good bye,baby!')
    exit()
else:
    exit('invalid input')
