GAMMA_RATE = ""
EPSILON_RATE = ""

fs = open("day3.txt", "r")
data = fs.read()
fs.close()

mega_list = data.split("\n")
main_list = []


def gamma_producer(ind):
    global main_list
    inter = []

    for item in mega_list:
        inter.append(item[ind])

    if inter.count("0") > inter.count("1"):
        main_list.append("0")
    elif inter.count("0") < inter.count("1"):
        main_list.append("1")


length = len(mega_list[0])

for i in range(length):
    gamma_producer(i)


for item in main_list:
    GAMMA_RATE += item


epsilon_list = []


def epsilon_producer(ind):
    global epsilon_list
    inter = []

    for item in mega_list:
        inter.append(item[ind])

    if inter.count("0") > inter.count("1"):
        epsilon_list.append("1")
    elif inter.count("0") < inter.count("1"):
        epsilon_list.append("0")


length = len(mega_list[0])

for i in range(length):
    epsilon_producer(i)


for item in epsilon_list:
    EPSILON_RATE += item


def binaryToDecimal(n):
    return int(n, 2)


GAMMA_RATE_D = binaryToDecimal(GAMMA_RATE)
EPSILON_RATE_D = binaryToDecimal(EPSILON_RATE)

print(f"The power consumption of submarine is {GAMMA_RATE_D * EPSILON_RATE_D}.")

