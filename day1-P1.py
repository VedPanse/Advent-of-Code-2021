# For getting raw input, read a file called day1.txt

fs = open("day1.txt", "r")
data = fs.read()
fs.close()

my_list = data.split("\n")


increment = 0

ind = 0

for i in range(len(my_list) - 1):
    if int(my_list[ind]) < int(my_list[ind+1]):
        increment += 1
    ind += 1


print(increment)
