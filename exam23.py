# 1.List elementlarini input orqali Nta ma'lumot bilan to'ldiring. Ushbu List elementlari orasida faqat 
# so'zlardagi unli harflarni (*)yulduzchaga almashtiruvchi method(funksiya) yarating.

n = int(input())
a = input().split(',')
b = ','.join(a).replace('a', '*')
c = ''.join(b).replace('A', '*')
d = ''.join(c).replace('e', '*')
e = ''.join(d).replace('E', '*')
f = ''.join(e).replace('i', '*')
g = ''.join(f).replace('I', '*')
h = ''.join(g).replace('o', '*')
i = ''.join(h).replace('O', '*')
j = ''.join(i).replace('u', '*')
k = ''.join(j).replace('U', '*')
l = ''.join(k).replace("o'", '*')
m = ''.join(l).replace("O'", '*')
print(m)

# 2-usul

# n=input()
# for i in ['a','e','i','o','u',]:n = n.replace(i, '*')
# print(n)

