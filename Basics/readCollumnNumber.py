file_name = 'readCollumnNumber.txt'


def read_column_number(file):
    f = open(file, 'r')
    lines = f.readlines()
    new_list = []

    for i in lines:
        new_list.append(i[:-1])

    for i in range(0, len(new_list)):
        list = new_list[i].split(' ')
        if (len(list)) > 1 and list[1] == 'Error:':
            z = list[2:-1]
            print("Line %s Error type: %s" % (list[0], ' '.join(z)))
            print("Time: %s" % list[-1])
    f.close()

read_column_number(file_name)
