class Evaluator:

    def zip_evaluate(worlds,coefs):
        s=0
        n=len(worlds)
        if n!=len(coefs):
            return -1
        temp=list(zip(worlds,coefs))
        for i in range(n):
            s+=len(temp[i][0])*temp[i][1]
        return s
    def enumerate_evaluate(worlds,coefs):
        n=len(worlds)
        if n!=len(coefs):
            return -1
        temp=[0 for i in range(n)]
        for i in range(n):
            temp[i]=len(worlds[i])
        temp=list(enumerate(temp))
        s=0
        for i in range(n):
            s+=coefs[temp[i][0]]*temp[i][1]
        return s    
    
    
Evaluator.zip_evaluate=staticmethod(Evaluator.zip_evaluate)
Evaluator.enumerate_evaluate=staticmethod(Evaluator.enumerate_evaluate)


words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
print(Evaluator.zip_evaluate(words,coefs))

words = ["Le", "Lorem", "Ipsum","n", "est", "pas", "simple"]
coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
print(Evaluator.enumerate_evaluate(words,coefs))

        
