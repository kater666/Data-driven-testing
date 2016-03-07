from sys import argv
from time import sleep
script, filename = argv
txt = open(filename)
print(txt.read())
txt.close()
