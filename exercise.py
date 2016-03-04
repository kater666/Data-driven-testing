name = 'readColumnExample.txt'

def print_file(file):
    f = open(file, 'r')
    lines = f.readlines()
    my_list = []
    x = ''
    for i in lines:
        for j in i:
            if j.isnumeric() == True:
                x += j
            else:
                if x == '':
                    pass
                else:
                    my_list.append(x)

                x = ''

    f.close()
    return my_list

print_file(name)


# Ugly but works
