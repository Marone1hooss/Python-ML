import random
def generator(text, sep=" ", option=None):
    if not isinstance(text,str) :
        raise ValueError
    arr=text.split(sep)
    n=len(arr)
    if option=="shuffle":
        for i in range(n):
            j = random.randint(0,n-1)
            arr[i], arr[j] = arr[j], arr[i]
    elif option=="unique":
        arr=set(arr)
    elif option=="ordered":
        arr=sorted(arr)
        
    for i in arr:
        yield i
        
text = "Lorem Ipsum Lorem Ipsum"
    
for word in generator(1, sep=" ", option="unique"):
    print(word)