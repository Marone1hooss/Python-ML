import numpy as np
from numpy.linalg import norm 

def dictance(a,b):
    return norm(a-b)


class cluster:
    
    def __init__(self,centroid,elements=[]) :
        self.centroid=centroid
        self.elements=elements
        
    def calculatecentroid(self):
        vals=np.zeros(len(self.elements[0]))
        for i in self.elements:
            vals+=i
        vals=vals/len(self.elements)
        return vals


class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=4):
        self.ncentroid = ncentroid #number of centroids
        self.max_iter = max_iter #number of max iterations to update the centroids
        self.centroids = [] #values of the centroids
        
    def fit(self, X):
        
        centroids=[]
        clusters=[]
        for i in range(self.ncentroid):
            temp=np.random.choice(X)
            while temp in centroids:
                temp=np.random.choice(X)
            clus=cluster(temp)
            clusters.append(clus)
            centroids.append(temp)
    
        for _ in range(self.max_iter):
            shape=X.shape
            for i in range(shape[0]):
                min = 0
                indx=0
                for j in range(self.ncentroid):
                    if dictance(X[i],clusters[j].centroid)<min:
                        indx=j
                clusters[j].elements=np.append(clusters[j].elements,X[i])
            t=0
            for j in range(self.ncentroid):
                temp=clusters[j].calculatecentroid()
                if temp==clusters[j].centroid:
                    t+=1
                else:
                    clusters[j].centroid=temp
            if t==self.ncentroid:
                break
        
        return clusters
                
            
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.
        Args:
        -----
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
        None.
        Raises:
        -------
        This function should not raise any Exception.
        """
        
    def predict(self, X):
        """
        Predict from wich cluster each datapoint belongs to.
        Args:
        -----
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
        the prediction has a numpy.ndarray, a vector of dimension m * 1.
        Raises:
        -------
        This function should not raise any Exception.
        """