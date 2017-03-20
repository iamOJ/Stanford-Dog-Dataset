import cv2

location = '/media/jones/Documents and Data/SEDS Projects Team/Stanford Dogs Dataset/Images/'

with open('parsedData.txt','r') as ins:
    array = []
    for line in ins:
        array.append(line)

def cropImg(name,xMin,xMax,yMin,yMax):
    print(name)
    print(xMin)
    print(xMax)
    print(yMin)
    print(yMax)
    '''
    img = cv2.imread(location+name)
    imgCropped = img[yMin:yMax,xMin:xMax]
    cv2.imwrite(location+'Cropped Images/'+name,imgCropped)
    cv2.waitKey(0) & 0xFF
    print('File saved at' + location+'Cropped Images/'+name)
    '''

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


