# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
# Chiang's first python program!!!!congratulation!!!
alreadyhave = []
left = 0
goods = [[0, 'book', 100], [1, 'guitar', 20000], [2, 'keyboard', 2000], [3, 'human being', 33333]]
salary = input('Please input your salary:')
if salary.isdigit():
    salary = int(salary)


def quit(input, alreadyhave, left):
    if left == 'q' or left == 'exit' or left == 'quit':
        left = 0
    if input == 'q' or input == 'exit' or input == 'quit':
        if alreadyhave == []:
            print('You have nothing', 'and your money left', left)
            exit()
        print('You have', alreadyhave, ',')
        print('and your money left', left)
        exit()
    else:
        pass


while True:
    quit(salary, alreadyhave, salary)
    for i in range(0, goods.__len__()):
        #    print(goods[i][0],goods[i][1],goods[i][2])
        print(goods[i])
    num = input('Please choice goods:')
    if num.isdigit():
        num = int(num)
    quit(num, alreadyhave, salary)
    if int(num) > goods.__len__():
        print('Out of range!!!!')
        continue
    pay = goods[num][2]
    if pay < salary:
        salary = (salary - pay)
        alreadyhave.append(goods[num])
        print('success!!!you only have', salary, '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    else:
        print('You have not enough money!!!!!!!!!!!!!!!!!!!!!!!!!')
