# -*- coding: utf-8 -*-
"""
Задание 6.3

В скрипте сделан генератор конфигурации для access-портов.

Сделать аналогичный генератор конфигурации для портов trunk.

В транках ситуация усложняется тем, что VLANов может быть много, и надо понимать,
что с ним делать.

Поэтому в соответствии каждому порту стоит список
и первый (нулевой) элемент списка указывает как воспринимать номера VLAN,
которые идут дальше.

Пример значения и соответствующей команды:
    ['add', '10', '20'] - команда switchport trunk allowed vlan add 10,20
    ['del', '17'] - команда switchport trunk allowed vlan remove 17
    ['only', '11', '30'] - команда switchport trunk allowed vlan 11,30

Задача для портов 0/1, 0/2, 0/4:
- сгенерировать конфигурацию на основе шаблона trunk_template
- с учетом ключевых слов add, del, only

Код не должен привязываться к конкретным номерам портов. То есть, если в словаре
trunk будут другие номера интерфейсов, код должен работать.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan",
]

access = {"0/12": "10", "0/14": "11", "0/16": "17", "0/17": "150"}
trunk = {"0/1": ["add", "10", "20"], "0/2": ["only", "11", "30"], "0/4": ["del", "17"]}

for intf, vlan in access.items():
    print("interface FastEthernet" + intf)
    for command in access_template:
        if command.endswith("access vlan"):
            print(f" {command} {vlan}")
        else:
            print(f" {command}")

for intf, vlans in trunk.items():
    action = vlans[0].replace("add", " add").replace("only", "").replace("del", " remove")
    vlans2 = (",").join(vlans[1:])
    print(f"Interface FastEthernet {intf}")
    for command in trunk_template:
        if command.endswith("allowed vlan"):
            print(f"{command}{action} {vlans2}")
        else:
            print(f"{command}")

#variant2
for intf, vlans in trunk.items():
    action = vlans[0]
    vlans2 = (",").join(vlans[1:])
    print(f"Interface FastEthernet {intf}")
    for command in trunk_template:
        if command.endswith("allowed vlan"):
            if action == "add":
                print(f"{command} add {vlans2}")
            elif action == "del":
                print(f"{command} remove {vlans2}")
            elif action == "only":
                print(f"{command} {vlans2}")
        else:
            print(f"{command}")
         
#variant3
trunk_actions = {"add":" add", "del":" remove", "only":""}
for intf, vlans in trunk.items():
    print(f"Interface FastEthernet {intf}")
    for command in trunk_template:
        if command.endswith("allowed vlan"):
            action = vlans[0]
            vlans2 = (",").join(vlans[1:])
            print(f"{command}{trunk_actions[action]} {vlans2}")
        else:
            print(f"{command}")
            
            
