import torch
import torch.nn as nn
import torch.optim as optim
from torch.autograd import Variable
import torchvision
from torchvision import datasets, models, transforms

import json
import numpy as np
from PIL import Image, ImageDraw, ImageFont

import random

class Picture:
    def __init__(self):
        self.fontPath = "./font/HGRME.TTC"
        self.vgg16 = models.vgg16(pretrained=True)
        self.vgg16.eval()
        normalize = transforms.Normalize(
                mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225]
        )
        
        self.preprocess = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            normalize
        ])
        self.labels = json.load(open('imagenet_class_index.json', 'r', encoding="utf-8"))
        self.position = self.__extractPosition()
        

    def __extractPosition(self):
        with open("position.txt", "r",encoding="utf-8") as f:
            data = f.read()
        data = data.split("\n")
        return data

    def __predictImage(self,img):
        img_tensor = self.preprocess(img)
        img_tensor.unsqueeze_(0)
        out = self.vgg16(Variable(img_tensor))
        return self.labels[np.argmax(out.data.numpy())]

    def writeDescription(self,imgFile):
        imgFile = Image.open(imgFile)
        imgFile = imgFile.point(lambda x: x*0.8)
        width,height = imgFile.size
        draw = ImageDraw.Draw(imgFile)
        text = self.__predictImage(imgFile)['ja']
        text += " " + self.position[random.randrange(len(self.position))]
        textLen = len(text)
        size = height / 10
        if textLen * size > width:
            size = width / textLen
        font = ImageFont.truetype(self.fontPath, int(size))
        draw.text((width / 2 - textLen/2 * int(size), height -int(size) - 5), text, fill=(255, 255, 255), font=font)
        return imgFile