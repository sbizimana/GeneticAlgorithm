from graphics import *
import Image
import numpy as np

class Picture():
  def __init__(self, photo):
    print("Loading Image...")
    self.img = Image.open(photo)
    self.array = np.array(self.img)
    self.temp = Image.fromarray(self.array)
    print("Image Loaded.\n")

    #self.img.load()
    self.height, self.width = self.img.size
    self.size = self.height * self.width
    #self.matrix = [[0 for y in range(self.width)] for x in range(self.height)]
    #self.temp = self.img.getpixel((133,119))
    #for x in range(self.height):
    #  for y in range(self.width):
    #    self.matrix[x][y] = [int('%02x%02x%02x' % self.img.getpixel((x,y)), 16)]
    #    self.matrix[x][y] = list(self.img.getpixel((x,y)))
    #    Eprint(x, y, self.img.getpixel((x,y)))
    #    pass

  def show(self):
      self.temp.show()

    

