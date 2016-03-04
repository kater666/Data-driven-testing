name = 'readColumnExample.txt'

def print_file(file):
    f = open(file, 'r')
    lines = f.readlines()
    my_list = []
    print(lines)
    x = ''
    for i in lines:
        if i.isnumeric() == True:
            x += i
        else:
            my_list.append(x)
            x = ''

    f.close()
    return my_list

print(print_file(name))
