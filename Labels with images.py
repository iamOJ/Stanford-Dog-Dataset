import scipy.io

location = '/media/jones/Documents and Data/SEDS Projects Team/'

mat = scipy.io.loadmat(location + 'Stanford Dogs Dataset/lists/train_list.mat')
target = open('names+labels.txt', 'w')
target.truncate()

for i in range(mat['file_list'].size):
    name = mat['file_list'][i][0][0]
    label = mat['labels'][i][0]

    target.write(name)
    target.write(',')
    target.write(str(label))
    target.write('\n')
    print(name+"  "+str(label)+"\n")
target.close()