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
    print(menu)
    command=input('What u want:')
    if command in menu:
        print(menu[command])
        command2=input('what u want:')
        while exit_flag:
            print(menu[command][command2])
            command3=input('what u want:')

    elif command=='q':
        exit_flag=False