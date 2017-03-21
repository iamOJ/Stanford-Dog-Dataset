import cv2

location = '/media/jones/Documents and Data/SEDS Projects Team/Stanford Dogs Dataset/Images/'

with open('parsedData.txt','r') as ins:
    array = []
    for line in ins:
        array.append(line)

xMax = 0
yMax = 0

for values in array:
    xmin = int(values.split(',')[0])
    xmax = int(values.split(',')[2])
    ymin = int(values.split(',')[1])
    ymax = int(values.split(',')[3])
    filename = values.split(',')[4][:-1]


    if(xMax<(xmax-xmin)):
        xMax = (xmax-xmin)
        print(xmax - xmin)
        #print(ymax - ymin)
        print(filename)
    if (yMax < (ymax - ymin)):
        yMax = (ymax - ymin)
        #print(xmax - xmin)
        print(ymax - ymin)
        print(filename)
