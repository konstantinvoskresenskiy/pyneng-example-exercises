# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
l=()
b1=False
b2=False
b3=True
p = 0
c = 0
schet=0
Ip_adress=input('Введите IP-адрес:')
schet=Ip_adress.count('.')
l=Ip_adress.split('.')
if Ip_adress=='255.255.255.255': 
   print('local broadcast')
   b1=True
elif Ip_adress=='0.0.0.0': 
   print('unassigned')
   b2=True
for i in l:
   if (i.isdigit()==True):
    p+=1
    print(p)
    if (int(i)>=0) and (int(i)<=255):
     c+=1 
     print(c)      
if (p==len(l)) and (c==len(l)) and (schet==3):
   if(int(l[0])>=1) and (int(l[0])<=223):
     print('unicast')
   elif (int(l[0])>=224) and (int(l[0])<=239):
     print('multicast')
   elif (b1 == False) and (b2 == False):
     print('unused')
else:
     print('Неправильный IP-адрес,введите по новой:')
    