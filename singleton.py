import copy

class NotSingleton():
    # class attribute is shared across all instances
    names = []

ns1 = NotSingleton()
print(id(ns1.names))
ns1.names.append(1)
print(id(ns1.names))
ns2 = NotSingleton()
ns2.names.append(2)
print(id(ns2.names))
ns3 = copy.deepcopy(ns1)
print(id(ns3.names))
ns2.names.append(3)
print(id(ns3.names))
print(f"Address of object memory: {id(ns1)}, {id(ns2)}, {id(ns3)}")
print(ns1.names)
print(25 * "_")


class Singleton():
    names = []

    def __new__(cls):
        '''__new__ method is always called before __init__'''
        return cls

s1 = Singleton()
print(id(s1.names))
s2 = Singleton()
print(id(s2.names))
s3 = copy.deepcopy(s1)
print(id(s3.names))
print(f"Address of object memory: {id(s1)}, {id(s2)}, {id(s3)}")

    

