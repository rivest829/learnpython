# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
count = 0
_name='chiang'
while count <50 :
    name = input("what's my name?")
    if name == _name:
        print('fucking right!!')
        break
    else:
        print('YOU SON OF A BITCH!!!!')
    count += 1
    if count%3==0:
        confirm = input('DO YOU WANT TO CONTINUE?(yes/no)')
        if confirm=='yes' or confirm =='y' or confirm == 'ok':
            continue
        else:
            print('FUCK OFF!')
        break
else:#这个语法牛逼啊
    print('TOO MUCH TRY!!!!')