# 3.	List berilgan. Base klassi 2ta voris klassga ega: 
# Derived1 va Derived2. Sizning vazifangiz Derived1 klassida Listdagi juft uzunlikdagi so’zlar va
# Derived2da esa Listdagi toq uzunlikdagi so’zlarni chiqarish.


class Base:
    def __init__(self):
        self.arr = []
        
    def add(self,val):
        self.arr.append(val)

class Derived1(Base):
    def __init__(self):
        super().__init__()
           
class Derived2(Base):
    def __init__(self):
        super().__init__()
        
s = input().split() 
# s =  ["osmon", "salom", "dunyo", "kola", "qand", "somsa", "xonim", "shorva"]       
d1,d2 = Derived1(),Derived2()
for soz in s:
    if len(soz)%2:
        d2.add(soz)
    else:
        d1.add(soz)
        
print('d1 => ',d1.arr)
print('d2 => ',d2.arr)