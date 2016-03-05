file_name = 'sumAllExample.txt'


def sumAll(file):
    f = open(file, 'r')
    lines = f.read()
    print(lines)
    x = ''
    my_list = []
    for i in lines:
        if i.isnumeric() == True:
            x += i
        elif i.isspace() == True or i == '\n':
            if x == '':
                pass
            else:
                my_list.append(int(x))
                x = ''

    f.close()
    return sum(my_list)

print(sumAll(file_name))

# Again ugly but works
