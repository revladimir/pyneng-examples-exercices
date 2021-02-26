# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Сообщение должно выводиться только один раз.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
#start
ip = input("Enter IP address: ")
octets = ip.split(".")

valid_ip = len(octets) == 4

for i in octets:
    if i.isdigit() and 0 <= int(i) < 256 and valid_ip:
        valid_ip = True
    else:
        valid_ip = False

if valid_ip: 
    if int(octets[0]) in range (1,224):
        print("unicast")
    elif int(octets [0]) in range (224, 240):
        print("multicast")
    elif ip == "255.255.255.255":
        print("local broadcast")
    elif ip == "0.0.0.0":
        print("unassigned")
    else:
        print("unused")
else: 
    print("Wrong ip address")
