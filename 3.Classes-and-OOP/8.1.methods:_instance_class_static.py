class Myclass:
    def method(self): #can modify the class state
        return 'instance  method called', self

    @classmethod
    def classmethod(cls): #can modify class state only across all instances. No object instance
        return 'class method called', cls
    
    @staticmethod
    def staticmethod(): #can'tt modify object or class state
        return 'static method called'


obj = Myclass()

print(obj.method()) 
#instance  method called', <__main__.Myclass object at 0x7f24c10de780>

print(obj.classmethod) 
#class method called', <class '__main__.Myclass'>)

