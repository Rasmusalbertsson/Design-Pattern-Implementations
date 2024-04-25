class Singleton:
    # class-level variable to store the single
    # instance of the class
    _instance = None

    # override the __new__ method to
    # control how new objects are created
    def __new__(cls):
        # check if instance of the class has
        # been created before. NOTE: lazy instantiation
        print('<new> creating...')
        if not cls._instance: 
            # create new instance of the class
            # and store it in _instance
            cls._instance = super().__new__(cls)
        # return the single instance of the class, either
        # newly created one or existing one
        return cls._instance
    
    # override the __init__ method to control initialization
    def __init__(self):
        print('<init> called...')

#OBS. run this before overriding of __init__

s1 = Singleton()
s2 = Singleton()
print(f" My s1 = {s1}")
print(f" My s2 = {s2}")
print(f"Testing Singleton so s1 is s2 = {s1 is s2}")