# We are trying to make a generic addition class that can add string as well as number
class Addition:
    def add_num(self,obj1, obj2):
        print("Integer addition")
        return obj1+obj2
    def add_str(self,obj1,obj2): # adding two string
        print("String addition")
        return str(obj1)+" Some str "+str(obj2)
    def __init__(self,obj1,obj2):
        self.obj1 = obj1
        self.obj2 = obj2
        if isinstance(obj1, int) and isinstance(obj2,int):
            self.add_num(obj1,obj2)
        if isinstance(obj1, str) and isinstance(obj2,str):
            self.add_str(obj1,obj2)
# a1 = Addition(2,3)
# print(a1)
# a2 = Addition('a','b')
# print(a2)