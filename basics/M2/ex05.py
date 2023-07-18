

def mean(arr):
    result=0
    for i in arr:
        result+=i
    result=result/len(arr)
    return result

def median(arr):
    arr=sorted(arr)
    n=len(arr)
    if n%2==1:
        return arr[int(n/2)]
    else:
        a=arr[n/2-1]
        b=arr[(n/2)]
        return (a+b)/2
def quartiles(data):
    data = sorted(data)
    n = len(data)
    a = int(n * 0.25)
    b = int(n * 0.75)
    q1 = data[a]
    q3 = data[b]
    return q1, q3
def var(arr):
    N=mean(arr)
    result=0
    for i in arr:
        result+=(i-N)**2
    return result/len(arr)

def std(arr):
    return var(arr)**(0.5)

a = [1, 42, 300, 10, 59]
print(mean(a))
# Expected result: 82.4
print(median(a))
# Expected result: 42.0
print(quartiles(a))
# Expected result: [10.0, 59.0]
print(var(a))
# Expected result: 12279.439999999999
print(std(a))
# Expected result: 110.81263465868862