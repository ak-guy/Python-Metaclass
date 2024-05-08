'''
this is how we create a class
'''
class A:
    a = 'ha'
    b = 1

    def f(self):
        return 4
    
'''
internally how we make classes, but less accuratly
'''
def make_class_A():
    actual_class_name = 'A'
    bases = () # this will be a tuple containing bases it is inheriting from

    a = 'ha'
    b = 1

    def f():
        return 4

    namespace = {'a': a, 'b': b, 'f': f}
    A = type(actual_class_name, bases, namespace)
    return A

A_obj = make_class_A()

print(A_obj.a)
    

'''
this is more accurate way of creating class
'''
def make_more_accurate_class_A():
    actual_class_name = 'A'
    bases = () # this will be a tuple containing bases it is inheriting from
    namespace = type.__prepare__(actual_class_name, bases)

    body = (
'''
a = 'haha'
b = 1

def f():
    return 4
'''
)

    exec(body, globals(), namespace)
    A = type(actual_class_name, bases, namespace)
    return A

A_obj = make_more_accurate_class_A()
print(A_obj.a)
