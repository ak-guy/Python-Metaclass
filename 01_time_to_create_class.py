import time
# type.__new__()

class LoadPerformanceMeta(type):
    _start_time = time.perf_counter()

    def __new__(self, name, bases, namespace):
        print("obj = {}, name = {}, bases = {}, namespace = {}".format(self, name, bases, namespace))
        end_time = time.perf_counter()
        namespace['__time_to_create__'] = end_time - LoadPerformanceMeta._start_time
        return super().__new__(self, name, bases, namespace)

class A(metaclass=LoadPerformanceMeta):
    pass

class B(A):
    pass

print(f'Time to create A = {A.__time_to_create__}')
print(f'Time to create B = {B.__time_to_create__}')