class A:
    def __init__(self):
        print('A init executed')
class B(A):
    def __init__(self):
        super().__init__()
        print("B init executed")
abc=B()
##MRO(method resolution order):
class A:
    pass
class B(A):
    pass
class C(B):
    x=5
class D(A):
    x=10
class E(C, D):
    pass
e=E()
print(e.x)
class A:
    X=5
class B(A):
    pass
class C(B):
    pass
class D(A):
    x=10
class E(C,D):
    pass
e=E()
print(e.x)
#order followed:
print(E.mro())

##Ieration Protocol
#for any object to be an iterable, it should have 2 dunders-
#"__iter__" and "__next__"
#protocol- 
#object's '__iter__' method should return an iterator
#iterator's '__next__' metod should return the new value on every call
#if the iterator reaches the end,it should raise an StopIteration exception
a=range(5)
it=a.__iter__()
print(it)
print(it.__next__())
class myrange:
    def __init__(self,n):
        self.n=n
    def __iter__(self):
        return myrange_iterator(self)
class myrange_iterator:
    def __init__(self,myrange):
        self.myrange = myrange
        self.i=0
    def __next__(self):
        ret=self.i
        self.i+=1
        if ret>= self.myrange.n:
            raise StopIteration
        return ret
a=myrange(5)
it=iter(a)
print(next(it))  