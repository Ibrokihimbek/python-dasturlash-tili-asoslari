# 1.Text nomli, A nomli va B nomli string ma'lumotlarni input orqali kiriting. Ushbu Textda A va B 
# belgilar orasidagi so'zni chiqaring.
# INPUT(Kiruvchi ma'lumotlar): Text='What is >apple<'  A='>'   B='<'
# OUTPUT(Chiquvchi ma'lumotlar):  "apple"

print('"', (text:=input())[text.find(input()) + 1:text.find(input())], '"', sep = '')