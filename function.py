def func(a):
    if (a>0):
        return (a)
    else:
        return("spam", 7.3)
print (func(1))
print (func(-1))
print (func(-1)[0])
print (func("-1")) #TypeError: '>' not supported between instances of 'str' and 'int'