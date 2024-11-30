import threading

class Singleton(object):
    _lock = threading.Lock()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            with cls._lock:  # Ensure thread safety
                if not hasattr(cls, 'instance'):
                    cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

s1 = Singleton()
s2 = Singleton()
print(s1 is s2, id(s1), id(s2))