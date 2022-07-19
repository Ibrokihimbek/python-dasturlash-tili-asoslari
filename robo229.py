a, b = input().split()
a = int(a)
b = int(b)
if (a+b)/2 > pow(a*b, 0.5):
    print('>')
elif ((a+b)/2) == pow(a*b, 0.5):
      print('=')
else:
      print("<")