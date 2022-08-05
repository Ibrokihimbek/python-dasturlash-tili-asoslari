# 1.Text nomli string va harf nomli stringlarni input orqali kiriting
# va ushbu harf Textdagi 2-chisini indeksini toping va chiqaring

a ,b, c = input("T: "), input("L: "), 1
for i in range(len(a)):
    if a[i] == b:
        if c == 0:
            print(i)
            break
        else: c -= 1
else: print('None')