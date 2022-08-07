# 2.Funksiya parametri sifatida sonlardan iborat list berilgan va ushbu listda faqat
# takrorlanadigan sonlarni saqlab, qolgan sonlarni o'chiruvchi funksiya tuzing.

def son(a):
    b = []
    for _ in a:
        if a.count(_) > 1:
            b.append(_)
    else:
        return b


a = [int(i) for i in input().split()]
print(son(a))