import sys

print(sys.version_info)
# -*- coding: utf-8 -*-
'''
Задание 4.5

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.

Результатом должен быть список: ['1', '3', '8']

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'
command1 = set(list((command1[command1.find('vlan ')+5:]).split(',')))
command2 = set(list((command2[command2.find('vlan ')+5:]).split(',')))
#command = set((command1[command1.find('vlan ')+5:]).split(',')-(command2[command2.find('vlan ')+5:]).split(','))
#command = (list(command))
command=command2&command1
print(sorted(command))
print(command1)
print(command2)
#print(sorted(command2-command1))
