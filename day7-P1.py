fs = open("day7.txt", "r")
data = fs.read()
fs.close()

mega_list = data.split(",")
some_list = []

for items in mega_list:
    some_list.append(int(items))

some_list.sort()

median = some_list[round((len(some_list) + 1)/2) - 1]

fuel_list = []

for items in some_list:
    fuel_list.append(abs(median - items))

print(sum(fuel_list))
