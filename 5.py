# Funksiya parametri sifatida int son va list berilgan. Listda mahsulot nomi va narxi dictionary orqali berilgan. 
# Sizning vazifangiz ushbu int songa mos eng qimmat mahsulotlarni chiqaruvchi funksiya tuzing.

def son(a):

    a = sorted(a, key = lambda x: x['price'], reverse=True)

    for i in range(int(input())):
        for j in a:
            n = max(a, key=lambda y: y['price'])['price']
            if n == j['price']:
                print(j)
                j['price'] = 0
                break

a = [{"name": "bread", "price": 100},
    {"name": "wine", "price": 138},
    {"name": "meat", "price": 15},
    {"name": "water", "price": 1}]

son(a)