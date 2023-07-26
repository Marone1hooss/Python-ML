import numpy as np
from PIL import Image
import matplotlib.pyplot as mp
class ImageProcessor:
    def __init(self):
        ...
    def load(self,path):
        image=Image.open(path)
        image=np.array(image)
        print(image.shape)
        
        return image
    def display(self,array):
        mp.imshow(array)
        mp.axis('off')
        mp.show()
        
img=ImageProcessor()
""" print(img.load("130272-a-letter-download-hq.png"))
img.display(img.load("130272-a-letter-download-hq.png")) """