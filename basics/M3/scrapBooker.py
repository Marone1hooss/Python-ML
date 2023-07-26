import numpy as np
class ScrapBooker:
    def crop(self, array, dim, position=(0,0)):
        
        """
        Crops the image as a rectangle via dim arguments (being the new height
        and width of the image) from the coordinates given by position arguments.
        Args:
        -----
        array: numpy.ndarray
        dim: tuple of 2 integers.
        position: tuple of 2 integers.
        Return:
        -------
        new_arr: the cropped numpy.ndarray.
        None (if combinaison of parameters not compatible).
        Raise:
        ------
        This function should not raise any Exception.
        """
        shape=array.shape
        if dim[0]+position[0]>shape[0] or dim[1]+position[1]>shape[1]:
            print("combinaison of parameters not compatible")
            return None 
        newarray=array[position[0]:dim[0]+position[0],position[1]:dim[1]+position[1]]

        return newarray 
    
    
    
    
    
    def thin(self, array, n, axis):
        """
        Deletes every n-th line pixels along the specified axis (0: Horizontal, 1: Vertical)
        Args:
        -----
        array: numpy.ndarray.
        n: non null positive integer lower than the number of row/column of the array
        (depending of axis value).
        axis: positive non null integer.
        Return:
        -------
        new_arr: thined numpy.ndarray.
        None (if combinaison of parameters not compatible).
        Raise:
        ------
        This function should not raise any Exception.
        """
        i=n
        while i< array.shape[axis]:
            array=np.delete(array,i,axis=axis)
            i+=n

        return array
        
    
    def juxtapose(self, array, n, axis):
        """
        Juxtaposes n copies of the image along the specified axis.
        Args:
        -----
        array: numpy.ndarray.
        n: positive non null integer.
        axis: integer of value 0 or 1.
        Return:
        -------
        new_arr: juxtaposed numpy.ndarray.
        None (combinaison of parameters not compatible).
        Raises:
        -------
        This function should not raise any Exception.
        """
        # Perform the juxtaposition based on the axis value
        if axis == 0:
            new_arr = np.vstack([array] * n)  # Stack n copies vertically
        else:
            new_arr = np.hstack([array] * n)  # Stack n copies horizontally

        return new_arr
    
    def mosaic(self, array, dim):
        """
        Makes a grid with multiple copies of the array. The dim argument specifies
        the number of repetition along each dimensions.
        Args:
        -----
        array: numpy.ndarray.
        dim: tuple of 2 integers.
        Return:
        -------
        new_arr: mosaic numpy.ndarray.
        None (combinaison of parameters not compatible).
        Raises:
        -------
        This function should not raise any Exception.
        """
        new_arr=np.hstack([array]*dim[0])
        new_arr=np.vstack([new_arr]*dim[1])
        return new_arr
    
spb = ScrapBooker()
arr1 = np.arange(0,25).reshape(5,5)
print(spb.crop(arr1, (3,1),(1,0)))
#Output :

arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1,9)
print(spb.thin(arr2,3,0))
#Output :

arr3 = np.array([[1, 2, 3],[1, 2, 3],[1, 2, 3]])
print(spb.juxtapose(arr3, 3, 1))
#Output :
