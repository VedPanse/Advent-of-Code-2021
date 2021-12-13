AIM = 0
HORIZONTAL = 0
DEPTH = 0

fs = open("day2.txt", "r")
data = fs.read()
fs.close()

mega_list = data.split("\n")

my_list = []

for item in mega_list:
    my_list.append(item.split(" "))


for item in my_list:
    given_key = item[0]
    given_val = int(item[1])

    if given_key == "forward":
        HORIZONTAL += given_val
        DEPTH += (AIM * given_val)
    elif given_key == "down":
        AIM += given_val
    else:
        AIM -= given_val

print(HORIZONTAL * DEPTH)
