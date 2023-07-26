import numpy as np
from PIL import Image
import matplotlib.pyplot as mp
from ImageProcessing import ImageProcessor


class ColorFilter:
    
    def __init__(self) :
        pass
    
    def invert(self, array):
        """
        Inverts the color of the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        maxvalue=255
        shape=array.shape
        newarr=np.copy(array)
        for i in range(shape[0]):
            for j in range(shape[1]):
                for _ in range(3):
                    newarr[i][j][_]=255-newarr[i][j][_]
        return newarr

    def to_blue(self, array):
        """
        Applies a blue filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Except """
        result=np.copy(array)
        shape=result.shape
        """ for i in range(shape[0]):
            for j in range(shape[1]):
                result[i][j][0]=0
                result[i][j][1]=0 """
        result[:,:,0]=0
        result[:,:,1]=0 
        return result
        
    def to_green(self, array):
        """
        Applies a blue filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Except """
        result=np.copy(array)
        shape=result.shape
        """ for i in range(shape[0]):
            for j in range(shape[1]):
                result[i][j][0]=0
                result[i][j][1]=0 """
        result[:,:,2]=0
        result[:,:,0]=0 
        return result
        
        
    def to_red(self, array):
        """
        Applies a blue filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Except """
        result=np.copy(array)
        shape=result.shape
        """ for i in range(shape[0]):
            for j in range(shape[1]):
                result[i][j][0]=0
                result[i][j][1]=0 """
        result[:,:,1]=0
        result[:,:,2]=0 
        return result
        
        
    def to_celluloid(self, array):
            
        """
        Applies a celluloid filter to the image received as a numpy array.
        Celluloid filter must display at least four thresholds of shades.
        Be careful! You are not asked to apply black contour on the object,
        you only have to work on the shades of your images.
        Remarks:
        celluloid filter is also known as cel-shading or toon-shading.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        num_shades=4
        step=256//num_shades
        shape=array.shape
        result=np.copy(array)
        for i in range(shape[0]):
            for j in range(shape[1]):
                result[i][j][0]=(array[i][j][0] // step) * step +step//2
                result[i][j][1]=(array[i][j][1] // step) * step +step//2
                result[i][j][2]=(array[i][j][2] // step) * step +step//2
                
        
        result = np.clip(result, 0, 255)
        return result
    
    
    def to_grayscale(self, array):
            
        """
        Applies a celluloid filter to the image received as a numpy array.
        Celluloid filter must display at least four thresholds of shades.
        Be careful! You are not asked to apply black contour on the object,
        you only have to work on the shades of your images.
        Remarks:
        celluloid filter is also known as cel-shading or toon-shading.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        num_shades=4
        step=256//num_shades
        shape=array.shape
        result=np.copy(array)
        for i in range(shape[0]):
            for j in range(shape[1]):
                result[i][j]=sum(array[i][j])/3
                
        
        return result

imp=ImageProcessor()
arr = imp.load("/home/housni/Python-ML/basics/M3/istockphoto-1368965646-612x612.jpg")

cf = ColorFilter()
imp.display(cf. invert(arr)) 
imp.display(cf.to_blue(arr))
imp.display(cf.to_green(arr))
imp.display(cf.to_red(arr))
imp.display(cf.to_celluloid(arr))
imp.display(cf.to_grayscale(arr))
