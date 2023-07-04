import cv2
import matplotlib.pyplot as plt
from os import listdir
import sys
import shutil

path = 'C:\\Users\\GAME\\Desktop\\DeepLearning\\TCC\\frost\\'
image_list = listdir(path)


count = 0
for image in image_list:
    print(image)
    img = cv2.imread(path+image, cv2.IMREAD_UNCHANGED)
    cv2.imwrite('C:\\Users\\GAME\\Desktop\\DeepLearning\\TCC\\original_images\\'+''+image,img)