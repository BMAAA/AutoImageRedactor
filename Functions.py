import os
from tkinter import *
from PIL import Image


class IM:
    def __init__(self, fol_i, fol_o):
        self.input_images = fol_i
        self.output_images = fol_o

    def magnifier(self, x, y):
        for images in list(filter(lambda i: i.endswith(".png") or i.endswith(".jpg") or i.endswith(".jpeg"),
                                  os.listdir(self.input_images))):
            # working with image
            im = Image.open(self.input_images + "/" + images)
            data = im.getdata()
            x1, y1 = im.size
            n = min(x // x1, y // y1)
            im1 = Image.new('RGBA', (int(x1) * n, int(y1) * n), (255, 255, 255, 0))
            newdata = [(data[i * x1 + j] * n for j in range(x1) for _ in range(n) for i in range(y1))
                       if n > 1 else data]

            # save new image
            self.save_file(images, newdata, im1)

    def deleter(self, color):
        for images in list(filter(lambda i: i.endswith(".png") or i.endswith(".jpg") or i.endswith(".jpeg"),
                                  os.listdir(self.input_images))):
            # working with image
            im = Image.open(self.input_images + "/" + images)
            data = im.getdata()
            x, y = im.size
            im1 = Image.new('RGBA', (x, y), (255, 255, 255, 0))
            if color in data:
                for i in range(y):
                    for j in range(x):
                        if data[i * x + j] == color:
                            data[i * x + j] = (255, 255, 255, 0)

            # save new image
            self.save_file(images, data, im1)

    def save_file(self, name, data, image):
        if data:
            image.putdata(data)
            image.save(f"{self.output_images}/{name}")
            print(name)
