# 3-list ichidagi cheksiz listlarni yaxlit list holatiga keltirish

# abc = [1, [4, [5], 5], [4, 5, [7, 9, 5], [1, 5, 9]], [3, 5, 7]]
# [[3,4,5],3,[4,[3,[5,[3],[4]],[4],[2]]]]


lst = [x for x in input().split()]
lst1 = str(lst)
opend = []

for x in lst1:
    if x.isdigit(): opend.append(int(x))
print(opend)