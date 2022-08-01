#1.Dictionaryda MORSE azbukasi berilgan. Ushbu shifrlangan ma'lumotni chiqarib bering.

MORSE = {".-": "a", "-...": "b", "-.-.": "c",
        "-..": "d", ".": "e", "..-.": "f",
        "--.": "g", "....": "h", "..": "i",
        ".---": "j", "-.-": "k", ".-..": "l",
        "--": "m", "-.": "n", "---": "o",
        ".--.":"p", "--.-": "q", ".-.": "r", 
        "...": "s", "-": "t", "..-": "u",
        "...-": "v", ".--": "w", "-..-": "x",
        "-.--": "y", "--..": "z", "_": " "}

inp = input().split("  ")

print((' '.join(list(map(lambda x: ''.join(list(map(lambda z: MORSE.get(z), x.split()))), inp)))).capitalize())