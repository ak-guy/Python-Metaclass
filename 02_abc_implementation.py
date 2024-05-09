'''
in this module we will see implementation of ABC (Abstract Base Class)
what ABC does is if a class has even single abstractmethod then it does not allow
its instance to be formed
'''
def abstractmethod(func):
    func.__is_abstract__ = True
    return func

def all_abstactmethods(cls):
    visited = set()
    abstract = []
    while isinstance(cls, ABCMeta):
        for key, val in vars(cls).items():
            if key in visited:
                continue
            visited.add(key)
            if getattr(val, '__is_abstract__', False):
                abstract.append(key)
        cls = cls.__mro__[1]
    return abstract

class ABCMeta(type):
    def __call__(self, *args, **kwargs):
        abstract = all_abstactmethods(self)
        print(abstract)
        if abstract:
            raise TypeError("Cannot create new object")
        print("obj created")
        return super().__call__(*args, **kwargs)
    
class ABC(metaclass=ABCMeta):
    pass

class A(ABC):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    @abstractmethod
    def f1(self):
        pass

    @abstractmethod
    def f2(self):
        pass

class B(A):
    def f1(self):
        return 10
    
    def f2(self):
        return 20

a_obj = A()