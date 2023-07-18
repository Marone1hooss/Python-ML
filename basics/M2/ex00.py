def ft_map(function_to_apply, iterable):
    
    for i in range(len(iterable)):
        yield function_to_apply(iterable[i])



def ft_filter(function_to_apply, iterable):
    for i in iterable:
        if function_to_apply(i):
            yield i


def ft_reduce(function_to_apply, iterable):
    s=iterable[0]
    for i in range(1,len(iterable)):
        s=function_to_apply(s,iterable[i])
    return s

x = [1, 2, 3, 4, 5]
print(ft_map(lambda dum: dum + 1, x))

print(list(ft_map(lambda t: t + 1, x)))

print(ft_filter(lambda dum: not (dum % 2), x))

print(list(ft_filter(lambda dum: not (dum % 2), x)))

lst = ["h", "e", "l","l","o" , " ", "w", "o", "r", "l", "d"]

print(ft_reduce(lambda u, v: u + v, lst))