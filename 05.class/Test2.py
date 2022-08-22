
class Util():
    c1=1
    _c1=2
    __c3=3
    
    def add(self,a:int,b:int)->int:
        return a+b
    
    def yunsuan(self):
        print("this is a yunsuan")
        def add(a,b):
            return a+b
        def dec(a,b):
            return a-b

u = Util()
u1=u.yunsuan()
print(u.add(1,2))
print(u._c1)

    
