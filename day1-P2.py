fs = open("day1.txt", "r")
data = fs.read()
fs.close()

mega_list = data.split("\n")
my_list = []


def calculate_sum(ind):
    try:
        my_list.append(int(mega_list[ind]) + int(mega_list[ind+1]) + int(mega_list[ind+2]))
    except IndexError:
        pass


for i in range(len(mega_list)-1):
    calculate_sum(i)


increment = 0

ind = 0

for i in range(len(my_list) - 1):
    if int(my_list[ind]) < int(my_list[ind+1]):
        increment += 1
    ind += 1


print(increment)

