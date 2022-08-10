# poliy kvadrati

a = {'a': '11', 'b': '21', 'c': '31', 'd': '41', 'e': '51',
     'f': '12', 'g': '22', 'h': '32', 'i': '42', 'j': '42', 'k': '52',
     'l': '13', 'm': '23', 'n': '33', 'o': '43', 'p': '53',
     'q': '14', 'r': '24', 's': '34', 't': '44', 'u': '54',
     'v': '15', 'w': '25', 'x': '35', 'y': '45', 'z': '55'}

print('-'.join(map(lambda x: a.get(x.lower()) if x.isalpha() else x, list(input("So'z kiriting:  ")))))