import cv2
import matplotlib.pyplot as plt
from os import listdir
import sys

sys.path.append('/')

from salt_pepper import salt_and_pepper

print(cv2.__version__)

def downsample2x(img,name):
    scale_percent = 50
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized2x = cv2.resize(img, dim, interpolation = cv2.INTER_CUBIC)
    print('Resized Dimensions : ',resized2x.shape)

    status = cv2.imwrite('C:\\Users\\GAME\\Desktop\\DeepLearning\\TCC\\LR Images\\Bicubic\\2x\\'+name,resized2x)
    print("Image 2x written to file-system : ",status)

    blur2x = cv2.GaussianBlur(resized2x,(5,5),0)
    status = cv2.imwrite('C:\\Users\\GAME\\Desktop\\DeepLearning\\TCC\\LR Images\\Bicubic_blur\\2x\\'+name,blur2x)
    print("Blur Image 2x written to file-system : ",status)

    sp2x = salt_and_pepper(resized2x)
    status = cv2.imwrite('C:\\Users\\GAME\\Desktop\\DeepLearning\\TCC\\LR Images\\Bicubic_sp\\2x\\'+name,sp2x)
    print("Salt and Pepper Image 2x written to file-system : ",status)

def downsample3x(img,name):
    scale_percent = 35
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized3x = cv2.resize(img, dim, interpolation = cv2.INTER_CUBIC)
    print('Resized Dimensions : ',resized3x.shape)

    status = cv2.imwrite('C:\\Users\\GAME\\Desktop\\DeepLearning\\TCC\\LR Images\\Bicubic\\3x\\'+name,resized3x)
    print("Bicubic Image 3x written to file-system : ",status)

    blur3x = cv2.GaussianBlur(resized3x,(5,5),0)
    status = cv2.imwrite('C:\\Users\\GAME\\Desktop\\DeepLearning\\TCC\\LR Images\\Bicubic_blur\\3x\\'+name,blur3x)
    print("Blur Image 3x written to file-system : ",status)

    sp3x = salt_and_pepper(resized3x)
    status = cv2.imwrite('C:\\Users\\GAME\\Desktop\\DeepLearning\\TCC\\LR Images\\Bicubic_sp\\3x\\'+name,sp3x)
    print("Salt and Pepper Image 3x written to file-system : ",status)

def downsample4x(img,name):
    scale_percent = 25
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)

    resized4x = cv2.resize(img, dim, interpolation = cv2.INTER_CUBIC)
    print('Resized Dimensions : ',resized4x.shape)

    status = cv2.imwrite('C:\\Users\\GAME\\Desktop\\DeepLearning\\TCC\\LR Images\\Bicubic\\4x\\'+name,resized4x)
    print("Image 4x written to file-system : ",status)
    
    sp4x = cv2.GaussianBlur(resized4x,(5,5),0)
    status = cv2.imwrite('C:\\Users\\GAME\\Desktop\\DeepLearning\\TCC\\LR Images\\Bicubic_blur\\4x\\'+name,sp4x)
    print("Blur Image 4x written to file-system : ",status)
    
    sp4x = salt_and_pepper(resized4x)
    status = cv2.imwrite('C:\\Users\\GAME\\Desktop\\DeepLearning\\TCC\\LR Images\\Bicubic_sp\\4x\\'+name,sp4x)
    print("Salt and Pepper Image 4x written to file-system : ",status)

path = 'C:\\Users\\GAME\\Desktop\\DeepLearning\\TCC\\original_images'
image_list = listdir(path)
print(image_list)

for image in image_list:
    img_path = path + '\\' + image
    img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    downsample2x(img,image)
    downsample3x(img,image)
    downsample4x(img,image)