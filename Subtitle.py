import torch
import torch.nn as nn
import torch.optim as optim
from torch.autograd import Variable
import torchvision
from torchvision import datasets, models, transforms
import numpy as np
import json
from PIL import Image


class Subtitle:
    def __init__(self):
        self.vgg16 = models.vgg16(pretrained=True)
        self.vgg16.eval()
        self.labels = json.load(open('imagenet_class_index.json', 'r', encoding="utf-8"))
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
    def predictImage(self,img):
        img = Image.open(img)
        img_tensor = self.preprocess(img)
        img_tensor.unsqueeze_(0)
        out = self.vgg16(Variable(img_tensor))
        return self.labels[np.argmax(out.data.numpy())]['ja']
