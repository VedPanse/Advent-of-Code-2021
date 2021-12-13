ORIGINAL_DICT = {"forward": 0, "down": 0, "up": 0}

fs = open("day2.txt", "r")
data = fs.read()
fs.close()

mega_list = data.split("\n")
print(mega_list)

my_list = []

for item in mega_list:
    my_list.append(item.split(" "))

print(my_list)

for item in my_list:
    given_key = item[0]
    given_value = int(item[1])

    pre_value = ORIGINAL_DICT[given_key]
    ORIGINAL_DICT[given_key] = pre_value + given_value


ascend = abs(ORIGINAL_DICT["up"] - ORIGINAL_DICT["down"])

req_value = ORIGINAL_DICT["forward"] * ascend

print(req_value)
