class vector:
    def __init__(self,input) :
        if not isinstance(input,float) and not  isinstance(input,int):
            if (len(input)==1):
                self.shap=(1,len(input[0]))
                self.values=input
            elif isinstance(input,tuple):
                if input[1]-input[0] <0 :
                    raise ValueError
                self.shap=(input[1]-input[0],1)
                self.values=[]
                for i in range(input[0],input[1]):
                    values[i-input[0]]=[i]
                
            else:
                self.shap=(len(input),1)
                self.values=input
               
        else:
            self.shap=(input,1)
            self.values=[[0 for _ in range(self.shap[1])] for _ in range(self.shap[0])]
            
            for i in range(input):
                self.values[i]=[i]
    
        
    def __add__(self, other):
        
        if isinstance(other,vector):
            # Addition with another vector
            if self.shap!=other.shap:
                raise ValueError("the two dimentions are diffrents!!")
            values=[[0 for _ in range(self.shap[1])] for _ in range(self.shap[0])]
            for i in range(self.shap[0]):
                for j in range(self.shap[1]):
                    values[i][j]=self.values[i][j]+other.values[i][j]
            return vector(values)
        else:
            raise TypeError("Unsupported operand type for +")

    def __radd__(self, other):
        # Implement right addition (reverse order) with self and other
        return self.__add__(other)

    def __sub__(self, other):
        
        if isinstance(other,vector):
            # Addition with another vector
            if self.shap!=other.shap:
                raise ValueError("the two dimentions are diffrents!!")
            values=[[0 for _ in range(self.shap[1])] for _ in range(self.shap[0])]
            
            for i in range(self.shap[0]):
                for j in range(self.shap[1]):
                    values[i][j]=self.values[i][j]-other.values[i][j]
            return vector(values)
        else:
            raise TypeError("Unsupported operand type for +")

    def __rsub__(self, other):
        # Implement right addition (reverse order) with self and other
        if isinstance(other,vector) and other.shap==self.shap:
        
            for i in range(self.shap[0]):
                for j in range(self.shap[1]):
                    self.values[i][j]=-self.values[i][j]
                    other.values[i][j]=-other.values[i][j]
                    
        return self.__sub__(other)
    
    def __truediv__(self,other):
        if isinstance(other,int) or isinstance(other,float):
            if other == 0:
                ZeroDivisionError
            values=[[0 for _ in range(self.shap[1])] for _ in range(self.shap[0])]
            
            for i in range(self.shap[0]):
                for j in range(self.shap[1]):
                    values[i][j]=self.values[i][j]/other
            return vector(values)
        else:
            raise  NotImplemented("Unsupported operand type for /")
            
    def __rtruediv__(self,other):
        raise NotImplemented("Unsupported operand type for /")
    
    def __mul__(self,other):
        if isinstance(other,int) or isinstance(other,float):
            values=[[0 for _ in range(self.shap[1])] for _ in range(self.shap[0])]
            
            for i in range(self.shap[0]):
                for j in range(self.shap[1]):
                    values[i][j]=self.values[i][j]*other
            return vector(values) 
        else:
            raise  NotImplemented("Unsupported operand type for *")
    def __str__(self):
        return f"Vector({self.values})"

    def __repr__(self):
        print(f"Vector({self.values})")
        
    def dot(self,other):
        if not isinstance(other,vector):
            NotImplemented("Unsupported operand for the dot product .")
        s=0
        if self.shap!=other.shap:
            ValueError("two diffrant shapes!!")
        for i in range(self.shap[0]):
            for j in range(self.shap[1]):
                s+=self.values[i][j]*other.values[i][j]

        return s

    def T(self):
        values=[[0 for _ in range(self.shap[0])] for _ in range(self.shap[1])]
        for i in range(self.shap[0]):
            for j in range(self.shap[1]):
                values[j][i]=self.values[i][j]
        
        return vector(values)

# Column vector of shape n * 1
v1 = vector([[0.0], [1.0], [2.0], [3.0]])
v2 = v1 * 5
print(v2)
# Expected output:
# Vector([[0.0], [5.0], [10.0], [15.0]])
# Row vector of shape 1 * n
v1 = vector([[0.0, 1.0, 2.0, 3.0]])
v2 = v1 * 5
print(v2)
# Expected output
# Vector([[0.0, 5.0, 10.0, 15.0]])
v2 = v1 / 2.0
print(v2)
# Expected output
# Vector([[0.0], [0.5], [1.0], [1.5]])
print(vector(9))


v1 = vector([[0.0], [1.0], [2.0], [3.0]])
v2 = vector([[2.0], [1.5], [2.25], [4.0]])
print(v1.dot(v2))
# Expected output:
# 18.0
v3 = vector([[1.0, 3.0]])
v4 = vector([[2.0, 4.0]])
print(v3.dot(v4))
# Expected output:
# 13.0
v1
# Expected output: to see what __repr__() should do
# [[0.0, 1.0, 2.0, 3.0]]
print(v1)
# Expected output: to see what __str__() should do
# [[0.0, 1.0, 2.0, 3.0]]

# Example 1:
v1 = vector([[0.0], [1.0], [2.0], [3.0]])
print(v1.shap)
# Expected output:
(4,1)
print(v1.T())
# Expected output:
# Vector([[0.0, 1.0, 2.0, 3.0]])
print(v1.T().shap)
# Expected output:
# (1,4)
# Example 2:
v2 = vector([[0.0, 1.0, 2.0, 3.0]])
print(v2.shap)
# Expected output:
# (1,4)
print(v2.T())
# Expected output:
# Vector([[0.0], [1.0], [2.0], [3.0]])
print(v2.T().shap)
# Expected output