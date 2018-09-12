import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

#Fashion MNIST data
##images of different clothing

##t-shirt/top 0, pants 1, pullover 2, dress 3, coat 4, sandal 5
##shirt 6, sneaker 7, bag 8, boot 9
fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
#size of dataset (images are 28x28)
train_images.shape

#plot example of data
plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)

#preprocess data - scale between 0 and 1
train_images = train_images / 255.0
test_images = test_images / 255.0
