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


    def writeDescription(self,imgFile):
        text = self.watson.predictImage(imgFile)
        imgFile = Image.open(imgFile)
        imgFile = imgFile.point(lambda x: x*0.8)
        width,height = imgFile.size
        draw = ImageDraw.Draw(imgFile)
        text += " " + self.position[random.randrange(len(self.position))]
        textLen = len(text)
        size = height / 10
        if textLen * size > width:
            size = width / textLen
        font = ImageFont.truetype(self.fontPath, int(size))
        draw.text((width / 2 - textLen/2 * int(size), height -int(size) - 5), text, fill=(255, 255, 255), font=font)
        return imgFile