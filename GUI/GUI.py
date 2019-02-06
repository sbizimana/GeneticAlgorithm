#from tkinter import *
#from graphics import *
from Picture import *
from Population import *



img = Picture("random.jpg")

pop = Population(img, .8, 150, 1)
pop.evolve()

