! pip install kaggle
! mkdir ~/.kaggle
! cp kaggle.json ~/.kaggle/
! chmod 600 ~/.kaggle/kaggle.json

! kaggle datasets download dansbecker/cityscapes-image-pairs    # change the name
! unzip cityscapes-image-pairs.zip

import os
from os import walk
import numpy as np
import cv2

train_location = 'cityscapes_data/train/'
val_loaction = 'cityscapes_data/val/'

# training data preparation
train_set = []
train_set_X = []
train_set_Y = []


############### ANOTHER WAY TO GET THE DATASET   ##################

# for (dir_path, dir_names, file_names) in walk(train_location):
#     #train_set.extend(file_names)
#     break

# for img_name in file_names:
#    image = cv2.imread(train_location + str(img_name))
#    [rows, cols, _] = image.shape
#    X = image[0:rows, 0:cols//2]
#    Y = image[0:rows, cols//2:cols]
#    train_set_X.append(X)
#    train_set_Y.append(Y)

###################################################################

for img_name in os.listdir(train_location):
   image = cv2.imread(train_location + str(img_name))
   [rows, cols, _] = image.shape
   X = image[0:rows, 0:cols//2]
   Y = image[0:rows, cols//2:cols]
   train_set_X.append(X)
   train_set_Y.append(Y)

train_set_X = np.array(train_set_X)
train_set_Y = np.array(train_set_Y)

np.save('Train_X.npy', train_set_X)
np.save('Train_Y.npy', train_set_Y)

%matplotlib inline
import matplotlib.pyplot as plt

plt.imshow(train_set_X[0])
#plt.imshow(train_set_Y[0])


import matplotlib.image as mpimg

img = mpimg.imread('cityscapes_data/train/1.jpg')
plt.imshow(img)

