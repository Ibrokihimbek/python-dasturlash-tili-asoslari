#1.Dictionaryda MORSE azbukasi berilgan. Ushbu shifrlangan ma'lumotni chiqarib bering.

a = {"-----": "0",
     ".----": "1",
     "..---": "2",
     "...--": "3",
     "....-": "4",
     ".....": "5",
     "-....": "6",
     "--...": "7",
     "---..": "8",
     "----.": "9" }

for x in (b:=input().split()): 
    print(a.get(x), end='')