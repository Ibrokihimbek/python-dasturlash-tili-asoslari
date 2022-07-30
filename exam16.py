# 2.Funksiya parametri sifatida string ma'lumoti berilgan va ushbu 
# stringda nechta raqam qatnahsganini aniqlovchi funksiya tuzing.

def digit(a):
    b = 0
    for i in a:
        if i.isnumeric():
            b += 1
    print(b)    

a = input()
digit(a)