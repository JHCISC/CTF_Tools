#-*- coding: utf-8 -*-
import CTFEZ

for i in range(0, 1000):
    print("===========================================================")
    print('0#退出程序\n1#ascii码转化\n2#二进制转化为字符\n3#base64解码\n4#摩斯密码\n5#栅栏密码\n6#凯撒密码\n7#培根密码\n8#当铺密码')
    number = int(input("请输入选择的功能: "))
    if number == 0:
        break
    elif number == 1:
        CTFEZ.asciitrun()
    elif number == 2:
        CTFEZ.bintrun()
    elif number == 3:
        CTFEZ.base64trun()
    elif number == 4:
        CTFEZ.morsetrun()
    elif number == 5:
        CTFEZ.fencetrun()
    elif number == 6:
        CTFEZ.caesartrun()
    elif number == 7:
        CTFEZ.Bacontrun()
    elif number == 8:
        CTFEZ.dangputrun()
