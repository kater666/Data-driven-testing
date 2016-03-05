# Create a file, write some lines into it.

f = open('basics.txt', 'w')
f.write("First line I wrote into the file\n")
f.write("This is second line\nThis is third line\n")
f.write('\n\n\n')
f.write("More datas\nhere\nand here\n")
f.close()


# Create methods to read from file with for loop, read() and readlines()

def read_file1(file):
    x = open(file, 'r')
    for i in x:
        if i == '\n':
            pass
        else:
            print(i[:-1])
    x.close()


def read_file2(file):
    x = open(file, 'r')
    lines = x.readlines()
    for i in lines:
        if i == '\n':
            pass
        else:
            print(i[:-1])
    x.close()


def read_file3(file):
    x = open(file, 'r')
    more_lines = x.read()
    print(more_lines)
    x.close()

# Print the result of your methods.
print("\n#1\n")
read_file1('basics.txt')
print("\n#2\n")
read_file2('basics.txt')
print("\n#3\n")
read_file3('basics.txt')

# http://pastebin.com/XRiUFWpM
