import keras
import scipy.io
import numpy

seed = 7
numpy.random.seed(seed)

location = '/media/jones/Documents and Data/SEDS Projects Team/'

mat = scipy.io.loadmat(location + 'Stanford Dogs Dataset/train_data.mat')

