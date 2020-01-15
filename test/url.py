from urllib.parse import urlsplit

link = []
domain = []

with open("link.txt","r") as l:
    link = l.readlines()
link = [x.strip() for x in link]

link_number = len(link)

for i in range(0,link_number):
    base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(link[i]))
    domain.append(base_url)
l.close()
d = open("domain.txt", "w")
for i in domain:
    d.write(i)
    d.write("\n")
d.close()
