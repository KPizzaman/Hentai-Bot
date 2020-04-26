from PIL import Image
from math import floor
im = Image.open("hacka.jpg")
px = im.load()
dictionary = {
    0: " ",
    1: ".",
    2: ":",
    3: "-",
    4: "=",
    5: "+",
    6: "*",
    7: "#",
    8: "%",
    9: "@"

}
width = im.size[0]
scale = floor(width/142)
newwidth = scale * 142
farray = []
averagecolour = 0
count = 0
a = 0
for i in range(im.size[1]):
    farray.append([])
    for j in range(newwidth):
        if count == scale:
            farray[i].append(floor(averagecolour/scale))
            count = 0
            averagecolour = 0
        for k in range(2):
            a += px[j, i][k]
            a = round(a/85.3)
        averagecolour += a
        a = 0 
        count += 1
heightscale = floor(scale/0.5)
newheight = int(floor(im.size[1]/heightscale)*heightscale)
count = 0
averagecolour = 0
imagearray = []
for j in range(int(newheight/heightscale)):
    imagearray.append([])
for i in range(142):
    for j in range(newheight):
        if count == heightscale:
            imagearray[int(j/heightscale)].append(dictionary[floor(averagecolour/scale)])
            count = 0
            averagecolour = 0
        averagecolour += farray[j-1][i-1]
        count += 1

f = open("cock.txt", "w")
for i in range(floor(newheight/heightscale)):
    temp = ""
    for j in range(len(imagearray[i])):
        temp += str(imagearray[i][j])
    f.write(temp)
    f.write("\n")












'''

for i in range(im.size[1]):
    smalarray = []
    for j in range(im.size[0]):
        a = 0
        for k in range(2):
            a += px[j, i][k]
            a = round(a/85.3)
            smalarray.append(dictionary[a])
    array.append(smalarray)
for i in range(615):
    temp = ""
    for j in range(len(array[i])):
        temp += str(array[i][j])
    f.write(temp)
    f.write("\n")'''