a=5
print(isinstance(a,object))
print(a+4)
print(isinstance(a,int))
class A:
    pass
print(type(A))
def func():
    pass
print(type(func))
print(isinstance(func,object))
class A:
    name="jatin"
    marks=50
print(type(A))
A=5
print(type(A))
print(type(int))
print(type(object))
class A:
    def __call__(self):
        print('You called me')
a=A()
print(type(a)) 
a() 

def func():
    print("Hello")
func()
func.__call__()
for i in range(5):
    print(i)
a={"name":"Jatin"}
print(a["name"])
print(a.__getitem__("name"))
class  Exponent:
    def __init__(self,n):
        self.n=n
    def __getitem__(self,x):
        return x**self.n
e=Exponent(3)
print(e[6])
class A:
    name="jatin"
    def __init__(self,n):
        self.n=n
a=A(2)
print(a.name)
print(a.n)
class Dog:
    kind="canine"
    def __init__(self,name):
        self.name=name
a=Dog('Maxx')
print(a.name)
print(a.kind)
