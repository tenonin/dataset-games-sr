import cv2
from os import listdir
import pathlib
import random
import sys

sys.path.append('/')

from salt_pepper import salt_and_pepper

print(cv2.__version__)

def upsample2x(img,name,folder):
    scale_percent = 50
    width = int(img.shape[1] / scale_percent * 100)
    height = int(img.shape[0] / scale_percent * 100)
    dim = (width, height)
    resized2x = cv2.resize(img, dim, interpolation = cv2.INTER_CUBIC)
    print('Resized Dimensions : ',resized2x.shape)
    status = cv2.imwrite('C:\\Users\\GAME\\Desktop\\DeepLearning\\TCC\\HR Images\\{}\\2x\\{}'.format(folder,name),resized2x)
    print("Image 2x written to file-system : ",status)

def upsample3x(img,name,folder):
    scale_percent = 35
    width = int(img.shape[1] / scale_percent * 100)
    height = int(img.shape[0] / scale_percent * 100)
    dim = (width, height)
    resized3x = cv2.resize(img, dim, interpolation = cv2.INTER_CUBIC)
    print('Resized Dimensions : ',resized3x.shape)
    status = cv2.imwrite('C:\\Users\\GAME\\Desktop\\DeepLearning\\TCC\\HR Images\\{}\\3x\\{}'.format(folder,name),resized3x)
    print("Image 3x written to file-system : ",status)

def upsample4x(img,name,folder):
    scale_percent = 25
    width = int(img.shape[1] / scale_percent * 100)
    height = int(img.shape[0] / scale_percent * 100)
    dim = (width, height)
    resized4x = cv2.resize(img, dim, interpolation = cv2.INTER_CUBIC)
    print('Resized Dimensions : ',resized4x.shape)
    status = cv2.imwrite('C:\\Users\\GAME\\Desktop\\DeepLearning\\TCC\\HR Images\\{}\\4x\\{}'.format(folder,name),resized4x)
    print("Image 4x written to file-system : ",status)

path = 'C:\\Users\\GAME\\Desktop\\DeepLearning\\TCC\\LR Images\\'
folder_list = listdir(path)
image_list = []
print(folder_list)

for folder in folder_list:
    path_to_metrics = path + '\\' + folder
    metric_list = listdir(path_to_metrics)
    for mfolder in metric_list:
        path_image_list = path_to_metrics + '\\' + mfolder
        image_list = listdir(path_image_list)
        print(folder,mfolder)
        for image in image_list:
            if (mfolder == '2x'):
                img_path = path_image_list + '\\' + image
                img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
                upsample2x(img,image,folder)
            elif mfolder == '3x':
                img_path = path_image_list + '\\' + image
                img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
                upsample3x(img,image,folder)
            else:
                img_path = path_image_list + '\\' + image
                img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
                upsample4x(img,image,folder)