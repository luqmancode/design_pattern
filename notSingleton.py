import copy

class NotSingleton():
    names: []

ns1 = NotSingleton()
ns2 = NotSingleton()
ns3 = copy.deepcopy(ns1)
print(f"Address of memory: {id(ns1)}, {id(ns2)}, {id(ns3)}")

class Singleton():
    names: []

    def __new__(cls):
        '''__new__ method is always called before __init__'''
        return cls

s1 = Singleton()
s2 = Singleton()
s3 = copy.deepcopy(s1)
print(f"Address of memory: {id(s1)}, {id(s2)}, {id(s3)}")

    

