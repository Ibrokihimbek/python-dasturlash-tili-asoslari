# 3.	Kitob nomli class berilgan. Ushbu
# classning elementlari quyidagicha: 1) Kitob nomi; 2) Kitob mualliflari; 3) Kitob narxi; 4) Kitob nashriyoti;
# Bu classda kiritish va chiqarish methodlarini ishlating. 5ta obyektlar ichidan Kitob nashriyoti 
# Alfavitning ‘A’ harfidan ‘H’gacha bo’lgan harflar bilan boshlanadigan obyektlar haqida ma’lumot chiqaring.



class Kitob:
    # konstruktorni kiritish uchun
    def __init__(self, nomi, mualifi, price, nashriyoti):
        self.nomi = nomi
        self.mualifi = mualifi
        self.price = price
        self.nashriyoti = nashriyoti
        
    def __str__(self):
        return f"Npmi: {self.nomi}. Mualifi: {self.mualifi}. Price: {self.price}. Nashriyoti: {self.nashriyoti}."
    
obArr = []
 
for j in range(5):
    nomi, mualifi, price, nashriyoti = input('Info: ').split()
    ob = Kitob(nomi, mualifi, price, nashriyoti)
    obArr.append(ob)

print("\n------------------info-----------------\n")

for i in obArr:
    if i.nashriyoti[0].upper() >= 'A' and i.nashriyoti[0].upper() <= 'H': 
        print(i)