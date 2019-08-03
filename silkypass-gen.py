#!/usr/bin/env python
#coding:utf-8

import string

passwd = 's1lKy'

chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
f = open('possible-silky-passwords.txt', 'a')
for char_1 in chars:
	for char_2 in chars:
		print(passwd + char_1 + char_2)
		f.write(passwd + char_1 + char_2 + '\n')

f.close()