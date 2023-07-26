import numpy as np

class numpyCreator:
    def __init__(self):
        ...
    def from_list(self,list):
        return np.array(list)
    def from_tuple(self,tuple):
        return np.array(tuple)
    def from_shap(self,shap,value):
        array=np.zeros(shap)
        for i in range(shap[0]):
            for j in range(shap[1]):
                array[i][j]=value
        return array
    def random(self,shap):
        return np.random.randint(100,shap)
    