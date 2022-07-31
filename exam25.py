# 2.Set va n soni funksiya parametri sifatida berilgan. Ushbu 
# setda n soniga yaqin bo’lgan sonni chiqaruvchi funksiya yarating.

def son(sett, a): 
    return min(sett, key = lambda i: abs(a - i))

n = int(input())
s = {-1, 7, 10, 11, 12, 17, 100}
print(son(s, n))