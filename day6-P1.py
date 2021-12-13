fs = open("day6.txt", "r")
data = fs.read()
fs.close()

mega_list = data.split(",")
my_list = []
for item in mega_list:
    my_list.append(int(item))

del mega_list


def algorithm(lst):
    global my_list
    count = 0
    empty_list = []
    for items in lst:
        if items != 0:
            empty_list.append(items - 1)
        else:
            empty_list.append(6)
            count += 1

    for any_num in range(count):
        empty_list.append(8)

    my_list = empty_list
    return my_list


for i in range(80):
    print(algorithm(my_list))


print(len(my_list))
