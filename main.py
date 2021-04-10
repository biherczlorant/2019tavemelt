adatok = []
# 1. feladat
with open('autok.txt', 'r') as f:
    for line in f:
        bonto = line.strip().split(' ')
        ap = {
            'nap': bonto[0],
            'hajtora': bonto[1][:2],
            'hajtperc': bonto[1][3:],
            'rendszam': bonto[2],
            'szemid': bonto[3],
            'kmcnt': int(bonto[4]),
            'kibe': 'ki' if bonto[5] == '0' else 'be'
        }
        adatok.append(ap)

# 2. feladat
print('2. feladat')
for i in reversed(adatok):
    if i['kibe'] == 'ki':
        print(f'{i["nap"]}. nap rendszám: {i["rendszam"]}')
        break

# 3. feldat
print('3. feladat')
bekernap = input("Nap:")
print(f'Forgalom a(z) {bekernap}. napon:')
for i in adatok:
    if i['nap'] == bekernap:
        print(f'{i["hajtora"]}:{i["hajtperc"]} {i["rendszam"]} {i["szemid"]} {i["kibe"]}')

# 4. feladat
print('4. feladat')
be = 0
ki = 0
for i in adatok:
    if i['kibe'] == 'ki':
        ki+=1
    else:
        be+=1
print(f'A hónap végén {ki-be} autót nem hoztak vissza.')

# 5. feladat
autok = set()
for i in adatok:
    autok.add(i['rendszam'])
for auto in sorted(autok):
    kmora = [i['kmcnt'] for i in adatok if i['rendszam'] == auto]
    print(f'{auto} {kmora[-1]-kmora[0]} km')

# 6. feladat
print('6. feladat')
vegtav = 0
maxtav = 0
indtav = 0

# itt meguntam majd folytatom
# print(f'Leghosszabb út: {vegtav} km,')