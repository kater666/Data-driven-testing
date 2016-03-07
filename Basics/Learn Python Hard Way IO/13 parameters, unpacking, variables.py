from sys import argv

'''
script, first, second, third = argv

print('The script is called:', script)
print('Your first variable is:', first)
print('Your second variable is:', second)
print('Your third variable is:', third)
'''

script, user_name, = argv

prompt = '> '

print("How old are you?")
age = input(prompt)

print("What sex are you?")
sex = input(prompt)

print("Where are you from?")
country = input(prompt)

print("""
%r is from %r.
%r is %r years old.
%r is a %r.
""" % (user_name, country, user_name, age, user_name, sex))