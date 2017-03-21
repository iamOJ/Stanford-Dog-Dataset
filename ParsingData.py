import scipy.io
import numpy
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET
import cv2

location = '/media/jones/Documents and Data/SEDS Projects Team/'

filenames = []
par=[]
boundboxes=[]
mat = scipy.io.loadmat(location + 'Stanford Dogs Dataset/lists/train_list.mat')
for file in mat['file_list']:
    filenames.append(
        location + 'Annotation/' + file[0][0][:-4])
    # print('/media/jones/Documents and Data/SEDS Projects Team/Stanford Dogs Dataset/Annotation/'+file[0][0][:-4])


# print(mat['file_list'])

def CharToInt(a):
    val = 0
    for i in range(0, len(a)):
        val = val + (ord(a[i]) - 48) * (10 ** (len(a) - i - 1))
    return val


'''
 img = cv2.imread('/media/jones/Documents and Data/SEDS Projects Team/Stanford Dogs Dataset/Images/n02085620-Chihuahua/n02085620_7.png')
 img1=img[28:192,121:256]
 cv2.imwrite('cropped.jpg',img1)
'''

target = open('parsedData.txt','w')
target.truncate()

for i in filenames:
    tree = ET.parse(i)
    root = tree.getroot()
    for child in root:
        for child1 in child:
            if child1.tag == 'bndbox':
                for child2 in child1:
                    # print(child.text,child1.text)
                    if (child2.tag == 'xmin'):
                        par.append(CharToInt(child2.text))
                    if (child2.tag == 'xmax'):
                        par.append(CharToInt(child2.text))
                    if (child2.tag == 'ymin'):
                        par.append(CharToInt(child2.text))
                    if (child2.tag == 'ymax'):
                        par.append(CharToInt(child2.text))
                boundboxes.append(par)
                #print(par)
                #target.write('\n'.join(par))
                target.writelines(list("%s," % item for item in par))
                target.write(mat['file_list'][filenames.index(i)][0][0])
                #target.write(i)
                target.write('\n')
                #target.write("\n")
                par.clear()
