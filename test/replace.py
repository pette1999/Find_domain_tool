arr = ["hello", "hi", "goodbye", "morning"]
new_arr = []

for i in arr:
    new_arr.append(i.replace("e", ""))

print(new_arr)