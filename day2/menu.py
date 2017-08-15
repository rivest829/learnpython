# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
menu={'Peking':{
            'Chaoyang':{
                'Oulu',
                'Guomao',
                'Shuangjing'
            },
            'Haidian':{
                'Tsinghua',
                'NorthBig',
                'Wudaokou'
            }
      },
      'Xian':{
          'Lintong':{
              'XUST',
              'XPT',
              'Huatsing pool'
          },
          'Weiyang':{
              'Daming gong',
              'BigHua 1964'
          },
          'TallNew':{
              'Son of a bitch',
              'Fucking Huoju tower'
          }
      },
      'Fujian':{
             'Nanping':{
                 'Motherland',
                 'Shaowu',
                 'Nakou'
             },
             'Putian':{
                 'LoverLand',
                 'Xiuyu'
             }
      }
}


exit_flag=True
while exit_flag:
    for i in menu:
        print(i)
    command=input('What u want:')
    if command in menu:
        while exit_flag:
            for i in menu[command]:
                print(i)
            command2 = input('what u want:')
            if command2 in menu[command]:
                while exit_flag:
                    for i in menu[command][command2]:
                        print(i)
                    command3=input('what u want:')
                    for i in menu[command][command2]:
                        print(i)
                    if command3=='b':
                        break
                    elif command3=='q':
                        exit_flag=False
                    else:
                        print('Wrong input')
            elif command2 == 'b':
                break
            elif command2 == 'q':
                exit_flag = False
            else:
                print('Wrong input')
    elif command=='q':
        exit_flag=False