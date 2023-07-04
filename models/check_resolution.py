import cv2
import matplotlib.pyplot as plt
from os import listdir
import sys
import shutil

path = 'C:\\Users\\GAME\\Desktop\\DeepLearning\\TCC\\original_images\\'
image_list = listdir(path)


count = 0
for image in image_list:
    img = cv2.imread(path+image, cv2.IMREAD_UNCHANGED)
    if img.shape[1] != 1920:
        shutil.move(path+image, "C:\\Users\\GAME\\Desktop\\DeepLearning\\TCC\\fake images")
        print(image)