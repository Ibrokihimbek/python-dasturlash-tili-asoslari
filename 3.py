# 2.	Funksiya parametri sifatida string va so'zlardan iborat list berilgan va sizning vazifangiz 
# ushbu stringda listdagi 
# so'zlar nechi marta takrorlanganligini aniqlab, ma'lumotlarni dictionary 
# ko'rinishida chiqaruvchi funksiya tuzing.

def w(s, l):
    t = [word for word in s.split()]
    d = {}
    for word in l:
        d[word] = t.count(word)
    print(d)
text = '''When I was one I had just 
begun Whwn I was two I was nearly new'''
w(text,['I', 'was', 'three', 'near'])