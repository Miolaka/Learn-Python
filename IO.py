import urllib
import os

x=input('some number:')
y=raw_input('anything:') #raw_input is not defined.

file=open('./stuff.dat', 'wa')
file.write(y)
file.close()

os.remove('./stuff.dat')

file=urllib.urlopen("http://www.google.com")
cotent=file.readlines()

print()