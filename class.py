class somevector (object):
        def __init__(self): 
            self.x=0.0
            self.y=0.0
            self.z=0.0
        def __str__(self):
            return('(%s %s %s)' %(self.x, self.y, self.z))

a=somevector()
b=somevector
a.x=3.0
b.x=3.0
c=b()
print(a)
print(b)
print(c)