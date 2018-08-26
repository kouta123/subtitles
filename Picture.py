from PIL import Image, ImageDraw, ImageFont

import random
from Watson import Watson
class Picture:
    def __init__(self):
        self.fontPath = "./font/HGRME.TTC"
        self.watson = Watson()
        self.position = self.__extractPosition()
 
   

    def __extractPosition(self):
        with open("position.txt", "r",encoding="utf-8") as f:
            data = f.read()
        data = data.split("\n")
        return data


    def writeDescription(self,img_file):
        text = self.watson.predictImage(img_file)
        img_file = Image.open(img_file)
        img_file = img_file.point(lambda x: x*0.8)
        width,height = img_file.size
        draw = ImageDraw.Draw(img_file)
        text += " " + self.position[random.randrange(len(self.position))]
        text_len = len(text)
        size = height / 10
        if text_len * size > width:
            size = width / text_len
        font = ImageFont.truetype(self.fontPath, int(size))
        draw.text((width / 2 - text_len/2 * int(size), height -int(size) - 5), text, fill=(255, 255, 255), font=font)
        return img_file