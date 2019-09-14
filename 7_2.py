#!/usr/bin/env python3
import re
#Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneNumRegex.search('My number id 415-555-4242.')
print('Phone number found: ' + mo.group())