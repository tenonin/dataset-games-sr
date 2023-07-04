import cv2
from os import listdir
import pathlib
import random
from statistics import mean
from skimage.metrics import structural_similarity as ssim
import numpy as np
from datetime import datetime

start_time = datetime.now()

original_path = 'C:\\Users\\GAME\\Desktop\\DeepLearning\\TCC\\original_images\\'
image_list = listdir(original_path)

hr_path = 'C:\\Users\\GAME\\Desktop\\DeepLearning\\TCC\\HR Images\\'
hr_image_folder = listdir(hr_path)

print(hr_image_folder)

original_folder = []

for image in image_list:
    img_path = original_path + '\\' + image
    original_folder.append(img_path)

hr_folder_2x = {'Bicubic':[], 'Bicubic_blur':[], 'Bicubic_sp':[]}
hr_folder_3x = {'Bicubic':[], 'Bicubic_blur':[], 'Bicubic_sp':[]}
hr_folder_4x = {'Bicubic':[], 'Bicubic_blur':[], 'Bicubic_sp':[]}

for folder in hr_image_folder:
    path_to_metrics = hr_path + folder
    metric_list = listdir(path_to_metrics)
    for mFolder in metric_list:
        path_image_list = path_to_metrics + '\\' + mFolder
        image_list = listdir(path_image_list)
        for image in image_list:
            if (mFolder == '2x'):
                img_path = path_image_list + '\\' + image
                hr_folder_2x[folder].append(img_path)
            elif mFolder == '3x':
                img_path = path_image_list + '\\' + image
                hr_folder_3x[folder].append(img_path)
            else:
                img_path = path_image_list + '\\' + image
                hr_folder_4x[folder].append(img_path)

psnr_array_2x = {'Bicubic':[], 'Bicubic_blur':[], 'Bicubic_sp':[]}
ssim_array_2x = {'Bicubic':[], 'Bicubic_blur':[], 'Bicubic_sp':[]}

psnr_array_3x = {'Bicubic':[], 'Bicubic_blur':[], 'Bicubic_sp':[]}
ssim_array_3x = {'Bicubic':[], 'Bicubic_blur':[], 'Bicubic_sp':[]}

psnr_array_4x = {'Bicubic':[], 'Bicubic_blur':[], 'Bicubic_sp':[]}
ssim_array_4x = {'Bicubic':[], 'Bicubic_blur':[], 'Bicubic_sp':[]}

for metric in hr_folder_2x:
    for image in range(len(hr_folder_2x[metric])):
        print("2x Folder {} {}".format(metric,image))
        if cv2.imread(hr_folder_2x[metric][image]).shape[0] == cv2.imread(original_folder[image], cv2.IMREAD_UNCHANGED).shape[0] and cv2.imread(hr_folder_2x[metric][image]).shape[1] == cv2.imread(original_folder[image], cv2.IMREAD_UNCHANGED).shape[1]:
            score, diff = ssim(np.squeeze(cv2.imread(hr_folder_2x[metric][image], cv2.IMREAD_UNCHANGED)), np.squeeze(cv2.imread(original_folder[image], cv2.IMREAD_UNCHANGED)), full=True, channel_axis=2)
            ssim_array_2x[metric].append(score)
            psnr_array_2x[metric].append(cv2.PSNR(cv2.imread(hr_folder_2x[metric][image], cv2.IMREAD_UNCHANGED), cv2.imread(original_folder[image], cv2.IMREAD_UNCHANGED)))

for metric in hr_folder_3x:
    for image in range(len(hr_folder_3x[metric])):
        print("3x Folder {} {}".format(metric,image))
        if cv2.imread(hr_folder_2x[metric][image]).shape[0] == cv2.imread(original_folder[image], cv2.IMREAD_UNCHANGED).shape[0] and cv2.imread(hr_folder_2x[metric][image]).shape[1] == cv2.imread(original_folder[image], cv2.IMREAD_UNCHANGED).shape[1]:
            score, diff = ssim(np.squeeze(cv2.imread(hr_folder_3x[metric][image], cv2.IMREAD_UNCHANGED)), np.squeeze(cv2.imread(original_folder[image], cv2.IMREAD_UNCHANGED)), full=True, channel_axis=2)
            ssim_array_3x[metric].append(score)
            psnr_array_3x[metric].append(cv2.PSNR(cv2.imread(hr_folder_3x[metric][image], cv2.IMREAD_UNCHANGED), cv2.imread(original_folder[image], cv2.IMREAD_UNCHANGED)))

for metric in hr_folder_4x:
    for image in range(len(hr_folder_4x[metric])):
        print("4x Folder {} {}".format(metric,image))
        if cv2.imread(hr_folder_2x[metric][image]).shape[0] == cv2.imread(original_folder[image], cv2.IMREAD_UNCHANGED).shape[0] and cv2.imread(hr_folder_2x[metric][image]).shape[1] == cv2.imread(original_folder[image], cv2.IMREAD_UNCHANGED).shape[1]:
            score, diff = ssim(np.squeeze(cv2.imread(hr_folder_4x[metric][image], cv2.IMREAD_UNCHANGED)), np.squeeze(cv2.imread(original_folder[image], cv2.IMREAD_UNCHANGED)), full=True, channel_axis=2)
            ssim_array_4x[metric].append(score)
            psnr_array_4x[metric].append(cv2.PSNR(cv2.imread(hr_folder_4x[metric][image], cv2.IMREAD_UNCHANGED), cv2.imread(original_folder[image], cv2.IMREAD_UNCHANGED)))


psnr_mean_2x = {'Bicubic':0, 'Bicubic_blur':0, 'Bicubic_sp':0}
ssim_mean_2x = {'Bicubic':0, 'Bicubic_blur':0, 'Bicubic_sp':0}

psnr_mean_3x = {'Bicubic':0, 'Bicubic_blur':0, 'Bicubic_sp':0}
ssim_mean_3x = {'Bicubic':0, 'Bicubic_blur':0, 'Bicubic_sp':0}

psnr_mean_4x = {'Bicubic':0, 'Bicubic_blur':0, 'Bicubic_sp':0}
ssim_mean_4x = {'Bicubic':0, 'Bicubic_blur':0, 'Bicubic_sp':0}

for metric in psnr_array_2x:
    psnr_mean_2x[metric] = mean(psnr_array_2x[metric])

for metric in ssim_array_2x:
    ssim_mean_2x[metric] = mean(ssim_array_2x[metric])

for metric in psnr_array_3x:
    psnr_mean_3x[metric] = mean(psnr_array_3x[metric])

for metric in ssim_array_3x:
    ssim_mean_3x[metric] = mean(ssim_array_3x[metric])

for metric in psnr_array_4x:
    psnr_mean_4x[metric] = mean(psnr_array_4x[metric])

for metric in ssim_array_4x:
    ssim_mean_4x[metric] = mean(ssim_array_4x[metric])

print("PSNR 2x: {}\n\n SSIM 2x: {}\n\nPSNR 3x: {}\n\n SSIM 3x: {}\n\nPSNR 4x: {}\n\n SSIM 4x: {}\n\n".format(psnr_mean_2x, ssim_mean_2x, psnr_mean_3x, ssim_mean_3x, psnr_mean_4x, ssim_mean_4x))

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))