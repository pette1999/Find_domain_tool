b = []
a = []

with open("before.txt", "r") as l:
    b = l.readlines()
b= [x.strip() for x in b]


with open("after.txt", "r") as l2:
    a = l2.readlines()
a = [y.strip() for y in a]

for i in range(0, len(b)):
    if b[i] == a[i]:
        print("true")
    else:
        print("false")