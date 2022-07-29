n = int(input())                              
i = list(map(int, input().split(' ')[:n]))
if i ==  sorted(i):
    print("YES")
else:
    print("NO")