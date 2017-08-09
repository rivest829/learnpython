# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
import getpass

_name = 'rivest829'
_password = 'jiang123'
name = input("what's ur fucking name?!\n————：")
guitar = input("Who play guitar?")
bass = input("Who play bass")
password = getpass.getpass("Password:")
output0 = '''
-----------Band Come!-------------------
UR name is fucking %s!!!
UR guitar is fucking %s!
Ur bass is fucking %s!!
0000000000000000000000000000000000000000
''' % (name, guitar, bass)
output1 = '''
-----------Band Come!-------------------
UR name is fucking {fucker1}!!!
UR guitar is fucking {fucker2}!
Ur bass is fucking {fucker3}!!
1111111111111111111111111111111111111111
'''.format(fucker1=name, fucker2=guitar, fucker3=bass)
output2 = '''
-----------Band Come!-------------------
UR name is fucking {0}!!!
UR guitar is fucking {1}!
Ur bass is fucking {2}!!
2222222222222222222222222222222222222222
'''.format(name, guitar, bass)
print(output0)
print(output1)
print(output2)
if name == _name and password == _password:
    print('Login successd')
else:
    print('Invalid name or password')
