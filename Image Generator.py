from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

path = '/media/jones/Documents and Data/SEDS Projects Team/Stanford Dogs Dataset/Images/'

target = open('names+labels.txt')
data = target.readlines()
names = []
labels = []
for i in range (0,len(data)):
    temp = data[i].split(',')
    names.append(temp[0])
    labels.append(temp[1])

datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')
for name in names:
    img = load_img(name)  # this is a PIL image
    x = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150)
    x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, 150, 150)

    # the .flow() command below generates batches of randomly transformed images
    # and saves the results to the `preview/` directory
    i = 0
    for batch in datagen.flow(x, batch_size=1,
                              save_to_dir='preview', save_prefix='catty', save_format='jpeg'):
        i += 1
        if i > 20:
            break  # otherwise the generator would loop indefinitely