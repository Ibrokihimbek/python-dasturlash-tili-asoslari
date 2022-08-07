# 3.	Kompyuter nomli class berilgan. Ushbu classning elementlari quyidagicha: 
# 1) Kompyuter nomi; 2) Kompyuter RAMi; 3) Kompyuter narxi; 
# 4) Kompyuter protsessori;
# Bu classda kiritish va chiqarish methodlarini ishlating. 4ta obyektlar ichidan 
# RAMi 4dan ko’p va 16dan kichik obyektlar haqida ma’lumot chiqaring.

class Kompyuter:
    # konstruktorni kiritish uchun
    def __init__(self, name, ram, price, protsessor):
        self.name = name
        self.ram = ram
        self.price = price
        self.protsesssor = protsessor
        
    def __str__(self):
        return f"Name: {self.name}. RAM: {self.ram}. Price: {self.price}. Processor: {self.protsesssor}."
    
obArr = []
 
for x in range(4):
    name, ram, price, processor = input('Info: ').split()
    ob = Kompyuter(name, ram, price, processor)
    obArr.append(ob)

print("\n------------------info-----------------\n")

for x in obArr:
    if 4 < int(x.ram) < 16: print(x)