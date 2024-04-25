class ClassicSingleton:
    # class-level variable to store single class instance
    _instance = None 
 
    # override the __init__ method to control initialization
    def __init__(self): 
        print('<init> called...')
        # raise an error to prevent constructor utilization 
        raise RuntimeError('Call get_instance() instead')

    @classmethod
    def get_instance(cls):
        print('<get_instance> called...')
        if not cls._instance: 
            # create new instance of the class 
            cls._instance = cls.__new__(cls)  
        # return the single instance of the class, either 
        # newly created one or existing one
        return cls._instance 

# Run CLassic __init__ first to show the RuntimeError   
#s0 = ClassicSingleton()
# then comment s0 and run the code below
s1 = ClassicSingleton.get_instance()
s2 = ClassicSingleton.get_instance()

print(f" My s1 = {s1}")
print(f" My s2 = {s2}")
print(f"Testing Singleton so s1 is s2 = {s1 is s2}")