#!/usr/bin/env python3
import re

vRegex = re.compile(r'[aeiouAEIOU]')
print(vRegex.findall('RoboCop eats baby food. BABY FOOD.'))

cRegex = re.compile(r'[^aeiouAEIOU]')
print(cRegex.findall('RoboCop eats baby food. BABY FOOD.'))