# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
#start
while True:
    ip = input("Enter IP address: ")
    octets = ip.split(".")

    valid_ip = len(octets) == 4

    for i in octets:
        if i.isdigit() and 0 <= int(i) < 256 and valid_ip:
            valid_ip = True
            break
        else :
            valid_ip = False
    if valid_ip:
        break
    else:
        print("Wrong ip address")
     

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

    
            
