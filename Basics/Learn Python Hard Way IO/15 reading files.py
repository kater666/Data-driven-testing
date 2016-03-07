# Importring modules
from sys import argv

# Set arguments to variables
# Script holds the name of this script
# filename holds the name of file user will pass while running this scipt in command line
script, filename = argv

# Open file named 'filename' and set it to txt variable
txt = open(filename)

# Print out the name of opened file
print('Here\'s your file %r:' % filename)
# Print out all content of the opened file
print(txt.read())
txt.close()
# Take filename again
print("Type the filename again:")
file_again = input("> ")

# Open a file again, or open a new file, depends on passed value in line 19
txt_again = (open(file_again))

# Print out the content of file in txt_again
print(txt_again.read())
txt_again.close()