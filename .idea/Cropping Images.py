import cv2

location = '/media/jones/Documents and Data/SEDS Projects Team/Stanford Dogs Dataset/Images/'

with open('parsedData.txt','r') as ins:
    array = []
    for line in ins:
        array.append(line)

def cropImg(name,xMin,xMax,yMin,yMax):
    '''
    print(name)
    print(xMin)
    print(xMax)
    print(yMin)
    print(yMax)
    '''
    '''
    cv2.imwrite('/media/jones/Documents and Data/SEDS Projects Team/Stanford Dogs Dataset/Images/Cropped Images/n02085620_199.jpg',img1)
    '''

    img = cv2.imread(location+name)
    imgCropped = img[yMin:yMax,xMin:xMax]

    #cv2.waitKey(0) & 0xFF
    print(str(cv2.imwrite(str(location+'Cropped Images/'+name),imgCropped)) + name)

for values in array:
    xmin = int(values.split(',')[0])
    xmax = int(values.split(',')[2])
    ymin = int(values.split(',')[1])
    ymax = int(values.split(',')[3])
    filename = values.split(',')[4][:-1]
    '''
    print(xmin)
    print(xmax)
    print(ymin)
    print(ymax)
    print(filename)
    print('\n')
    '''
    cropImg(filename,xmin,xmax,ymin,ymax)


