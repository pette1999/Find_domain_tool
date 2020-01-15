with open("link.txt","r") as f:
    link = f.readlines()
link = [x.strip() for x in link]
print(link)
print(len(link))
for i in range(0, len(link)):
    print(link[i])
