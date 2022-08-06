# 3.	Sport nomli klassda sport turlari Listga kiritilgan. Ushbu klass 2ta vorisga ega: Koptokli klassida 
# faqat koptokli sport turlari va Boshqa klassida esa koptoksiz sport turlarini chiqaring.

class Sport:
    def __init__(self):
        self.arr = []
        
    def add(self,val):
        self.arr.append(val)

class Koptokli(Sport):
    def __init__(self):
        super().__init__()
           
class Boshqa(Sport):
    def __init__(self):
        super().__init__()
        
s = ['Football', 'Basketball', 'Gimnastika', 'Voleyball', 'Kurash', 'Sambo', 'Tennis']       
k,b = Koptokli(),Boshqa()
for i in s:
    if 'ball' in i or "Tennis" in i: 
        k.add(i)
    else:
        b.add(i)
        
print('koptokli => ',k.arr)
print('boshqa => ',b.arr)