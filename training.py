import numpy
import pandas
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline


seed = 7
numpy.random.seed(seed)

location = '/media/jones/Documents and Data/SEDS Projects Team/'

target = open('names+labels.txt')
data = target.readlines()
names = []
labels = []
for i in range (0,len(data)):
    temp = data[i].split(',')
    names.append(temp[0])
    labels.append(int(temp[1].split('\n')[0]))

labelsnp = numpy.asarray(labels)

encoder = LabelEncoder()
encoder.fit(labelsnp)
encoded_Y = encoder.transform(labelsnp)

dummy_y = np_utils.to_categorical(encoded_Y)

model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(3, 150, 150)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

