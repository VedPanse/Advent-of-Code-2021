IND = 0
COMMON_SKELETON = []
my_list = []

fs = open("day3.txt", "r")
data = fs.read()
fs.close()

mega_list = data.split("\n")

inter = []


def find_most_common(lst):
    if lst.count("0") > lst.count("1"):
        return "0"
    else:
        return "1"


def main_algo():
    global inter, IND
    for item in mega_list:
        inter.append(item[IND])
    common = find_most_common(inter)

    COMMON_SKELETON.append(common)


for i in range(len(mega_list[0])):
    main_algo()
    IND += 1
    inter = []
    


for num in COMMON_SKELETON:
    print(num)

print(list(set(my_list)))

