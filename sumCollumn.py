file_name = 'sumColumnExample.txt'


def sumColumn(file):
    f = open(file, 'r')
    x = 0
    for i in f.readlines():
        x += int(i)

    f.close()
    return x

print(sumColumn(file_name))
# result 40
