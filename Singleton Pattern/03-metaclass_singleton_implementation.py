#
# Metaclass definition of a Singleton
#
class SingletonMeta(type):
    """
    We can implement a Singleton class in different ways in Python. Some
    possible ways include: base class, decorator, metaclass. The
    metaclass is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        print('<call meta> calling...')
        if cls not in cls._instances:
            instance = super().__call__()
            cls._instances[cls] = instance
        return cls._instances[cls]

#
# Actual Singleton with specific functionality as derived from the metaclass
#
class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        """
        The nice thing about this approach is that this Singleton can define any business 
        logic separately
        from the actual Singleton definition/implementation 
        (which is in the SingletonMeta class)
        """

        # ...

#s1 = Singleton()
#s2 = Singleton()
#print(f" My s1 = {s1}")
#print(f" My s2 = {s2}")
#print(f"Testing Singleton so s1 is s2 = {s1 is s2}")