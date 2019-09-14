#!/usr/bin/env python3
import re
print('Using | :')
mRegex = re.compile(r'aaa|bb cc')
mo1 = mRegex.search('aaa bbb ccc ddd')
print('mo1.group(): ' + mo1.group()) #aaa
mo2 = mRegex.search('bbb ccc aaa ddd')
print('mo2.group(): ' + mo2.group()) #bb cc

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print('mo.group(): ' + mo.group()) #Batmobile
print('mo.group(1): ' + mo.group(1)) #mobile

print('Using ? :')
batRegex = re.compile(r'Bat(wo)?man')
mo3 = batRegex.search('Batman lost a wheel')
print('mo3.group(): ' + mo3.group()) #Batman
mo4 = batRegex.search('Batwoman lost a wheel')
print('mo4.group(): ' + mo4.group()) #Batwoman

print('Using * :')
batRegex = re.compile(r'Bat(wo)*man')
mo5 = batRegex.search('Batman lost a wheel')
print('mo5.group(): ' + mo5.group()) #Batman
mo6 = batRegex.search('Batwoman lost a wheel')
print('mo6.group(): ' + mo6.group()) #Batwoman
mo7 = batRegex.search('Batwowowowoman lost a wheel')
print('mo7.group(): ' + mo7.group()) #Batwowowowoman

print('Using + :')
batRegex = re.compile(r'Bat(wo)+man')
mo8 = batRegex.search('Batwoman lost a wheel')
print('mo8.group(): ' + mo8.group()) #Batwoman
mo9 = batRegex.search('Batwowowowoman lost a wheel')
print('mo9.group(): ' + mo9.group()) #Batwowowowoman

haRegex = re.compile(r'(Ha){3}')
mo10 = haRegex.search('HaHaHa')
print('mo10.group(): ' + mo10.group())
mo11 = haRegex.search('Ha')
print('mo11 == None : ', end = '')
print(mo11 == None)







