# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если н есколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
l=list()
schet1=0
schet2=0
b1=False
b2=False
b3=False
Ip_adress=input('Введите IP-адрес:')
l=Ip_adress.split('.')
if Ip_adress.count('.')==3:
   b1=True
for i in l:
   if i.isdigit()==True:
      schet1+=1
   if schet1==4:
      b2=True
for j in l:
   if (b2==True) and (int(j)>=0) and (int(j)<=255):
      schet2+=1
   if schet2==4:
      b3=True
if (b1!=True) or (b2!=True) or (b3!=True):
   print('Неправильный IP-адрес')
else:           
   if(int(l[0])>=1) and (int(l[0])<=223):
    print('unicast')
   elif (int(l[0])>=224) and (int(l[0])<=239):
    print('multicast')
   elif Ip_adress=='255.255.255.255':
    print('local broadcast')
   elif Ip_adress=='0.0.0.0': 
    print('unassigned')
   else:
    print('unused')         