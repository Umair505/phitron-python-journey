# if you want a new instance, you will get the old one (already created ) instance

class Singleton:
    __instance = None
    def __init__(self) -> None:
        if Singleton.__instance is None:
            Singleton.__instance = self
        else:
            raise Exception('This is Singleton. Already have an instance, use that one by calling get_instance method')
    
    @staticmethod
    def get_instance():
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance

first = Singleton.get_instance()
print(first)