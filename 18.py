# 1.	Sringda son berilgan va ushbu 
# sonning boshida nechta 0(nol) qatnashganini aniqlang.

a = input()
b = 0
for i in a:
    if i == '0':
        b+=1
    else:
        break
print(b)
    