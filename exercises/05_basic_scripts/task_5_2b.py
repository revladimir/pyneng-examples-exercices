# -*- coding: utf-8 -*-
"""
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
#start
import sys

ip, mask = sys.argv[1].split("/")


oct1, oct2, oct3, oct4 = ip.split(".")
oct1, oct2, oct3, oct4 = int(oct1), int(oct2), int(oct3), int(oct4)
net_bin = "{:08b}{:08b}{:08b}{:08b}".format(oct1, oct2, oct3, oct4)
mask = int(mask)
net2 = net_bin[:mask] + "0" * (32 - mask)

net1, net2, net3, net4 = [
    int(net2[:8], 2), 
    int(net2[8:16], 2),
    int(net2[16:24], 2),
    int(net2[24:32], 2)
    ]
ip_output = """
Network:
{0:<8}  {1:<8}  {2:<8}  {3:<8}
{0:<08b}  {1:<08b}  {2:<08b}  {3:<08b}"""

net_output = """
Mask:
/{0}
{1:<8}  {2:<8}  {3:<8}  {4:<8}
{1:<08b}  {2:<08b}  {3:<08b}  {4:<08b}"""

bin_mask = "1" * mask + "0" * (32 - mask)
m1, m2, m3, m4 = [
    int(bin_mask[0:8], 2), 
    int(bin_mask[8:16], 2), 
    int(bin_mask[16:24], 2), 
    int(bin_mask[24:32], 2)
    ]
print (ip_output.format(net1, net2, net3, net4))
print (net_output.format(mask, m1, m2, m3, m4))
