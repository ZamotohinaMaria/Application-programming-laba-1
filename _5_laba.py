import glob
from PIL import Image

import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

from torchvision import datasets, models, transforms
from torch.utils.data import DataLoader, Dataset

#using numpy
import numpy as np

#for data load or save
import pandas as pd

#visualize some datasets
import matplotlib.pyplot as plt

#check our work directory
import os

class dataset(torch.utils.data.Dataset):
    
    def __init__(self,file_list,transform=None):
        self.file_list = file_list
        self.transform = transform
        
        
    #dataset length
    def __len__(self):
        self.filelength = len(self.file_list)
        return self.filelength
    
    #load an one of images
    def __getitem__(self,idx):
        img_path = self.file_list[idx]
        print(img_path)
        img = Image.open(img_path)
        img_transformed = self.transform(img)
        
        label = img_path.split('/')[-1].split('.')[0]
        if label == 'dog':
            label=1
        elif label == 'cat':
            label=0
        print(label)  
            
        return img_transformed,label
    

def main():
    print('laba 5 started')
    images_list = []
    images_list = glob.glob(os.path.join('dataset/dataset_random_name','*.jpg'))
    train_list = images_list[0 : int(len(images_list)*0.8)]
    test_list = images_list[int(len(images_list)*0.8) : int(len(images_list)*0.9)]
    val_list = images_list[int(len(images_list)*0.9) : int(len(images_list))]
    
    
    print(len(images_list))
    print(images_list[:5])
    
    print(len(train_list))
    print(train_list[:5])
    
    print(len(test_list))
    print(test_list[:5])
    
    print(len(val_list))
    print(val_list[:5])
    #-------проверка картинок-----------------------------------
    random_idx = np.random.randint(1,len(images_list),size=10)

    fig = plt.figure()
    i=1
    for idx in random_idx:
        ax = fig.add_subplot(2,5,i)
        img = Image.open(images_list[idx])
        plt.imshow(img)
        i+=1

    plt.axis('off')
    plt.show()
    
    print(train_list[0].split('/')[-1].split('.')[0])
    #------------------------------------------------------------
    
    train_transforms =  transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.RandomResizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor()
    ])

    val_transforms = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.RandomResizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor()
    ])

    test_transforms = transforms.Compose([   
        transforms.Resize((224, 224)),
        transforms.RandomResizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor()
    ])
    
    train_data = dataset(train_list, transform=train_transforms)
    test_data = dataset(test_list, transform=test_transforms)
    val_data = dataset(val_list, transform=val_transforms)
    
    print(train_data[0])

if __name__ == '__main__':
    main()
