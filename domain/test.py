word = "news.microsoft.com"
length = len(word)
tail = word[length-3:length]
if tail == "com":
    print("index: ", word.index("."))
    index = word.index(".")
    word = word[index+1:length]
    print("New word: ", word)
else:
    print("Something is wrong")
    print("Tail: ", tail)
# =============================================================== #

## Test for validators.py
# import validators 

# print(validators.email("haichen@chapman.edu"))

# print(validators.url("http:/haichen.com"))

# domain = ["chenhaifan.com", "dxc.technology", "dellemc.com", "panasonic.aero", "pitch.studio", "calif.aaa.com", "aaa.com"]

# index = 1
# for i in domain:
#     print(index, validators.domain(i))
#     index += 1

# =============================================================== #

## Test for time.py


# import time

# start = time.time()

# for i in range(0, 10):
#     print(int(time.time() - start))
#     time.sleep(1)
# print("before")

# time.sleep(10)
# print("after")

# print("clock: ", time.clock())

# print(int(time.time() - start))
# time.sleep(5)
# print(int(time.time() - start))

# print(time.time()-start)

# if(time.time() - start >= 10):
#     print("too long")
# else:
#     print("good")
