from sys import argv

script, filename = argv
'''
# Open file in read + write mode.
# This mode doesn't truncate the file in the beginning.
# truncate() doesn't work here. Why?
txt = open(filename, 'r+')

print(txt.read())

line1 = input("> ")
txt.write(line1)

print(txt.read())
txt.close()
'''

# Opening file in write + read mode.
# File is truncated in the beginning.
txt = open(filename, 'w+')

line1 = input("> ")
txt.write(line1)

txt.close()
