import re

sign1 = ","
sign2 = "-"
sign3 = "("
sign4 = ")"
sign5 = "'"
after_name = []
first = []
last = []

with open("name.txt","r") as l:
    names = l.readlines()

names = [x.strip() for x in names]

# for x in names:
#     x = re.sub(' +',' ',x)

for i in range(0, len(names)):
    if (sign1 in names[i] and sign2 in names[i]):
        word = names[i]
        n1 = word.find(sign1)
        n2 = word.find(sign2)
        if n1 > n2:
            word = word[:n2]
        else:
            word = word[:n1]
        names[i] = word
        after_name.append(names[i])
    elif sign1 in names[i]:
        word = names[i]
        n = word.find(sign1)
        word = word[:n]
        names[i] = word
        after_name.append(names[i])
    elif sign2 in names[i]:
        word = names[i]
        n = word.find(sign2)
        word = word[:n]
        names[i] = word
        after_name.append(names[i])
    else:
        after_name.append(names[i])
l.close()
#clean "," "-"

for i in range(0, len(after_name)):
    if (sign3 in names[i] and sign4 in names[i]):
        word = after_name[i]
        n1 = word.find(sign3)
        n2 = word.find(sign4)
        word2 = word[:n1] + word[n2+1:]
        word2 = word2.split(" ")
        word = ""
        for j in word2:
            word += j
        after_name[i] = word
    elif sign3 in names[i]:
        word = names[i]
        n = word.find(sign3)
        word = word[:n]
        after_name[i] = word
    elif sign4 in names[i]:
        word = names[i]
        n = word.find(sign4)
        word = word[:n]
        after_name[i] = word
    else:
        pass

for i in range(len(after_name)):
    box = after_name[i].split(" ")
    if len(box)>2:
        after_name[i] = box[0] + " " + box[1]
    else:
        pass
#clean the length to 2

for i in range(len(after_name)):
    box = after_name[i].split(" ")
    print(box)
    if len(box)==1:
        if "." in box[0]:
            box.remove(box[0])
            after_name[i] = ""
    elif len(box)==2:
        if "." in box[0]:
            box.remove(box[0])
            after_name[i] = box[0]
        elif "." in box[1]:
            box.remove(box[1])
            after_name[i] = box[0]
        else:
            pass
#delete middle name

for i in range(len(after_name)):
    word = after_name[i]
    if sign5 in word:
        n = word.find(sign5)
        word2 = word[:n] + word[n+1:]
        after_name[i] = word2
#clean '

for i in range(len(after_name)):
    box = after_name[i].split(" ")
    if len(box)==2:
        box.remove(box[1])
        after_name[i] = box[0]

for i in range(len(after_name)):
    if len(after_name[i])==1:
        after_name[i] = ""

for i in after_name:
    print(i)

d = open("after.txt", "w")
for i in after_name:
    d.write(i)
    d.write("\n")
d.close()
#write the right name out
