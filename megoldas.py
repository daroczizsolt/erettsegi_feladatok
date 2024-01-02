# Először definiálom a szavak listát
szavak = ["fuvola", "csirke", "adatok", "asztal", "fogoly", "bicska", "farkas", "almafa", "babona", "gerinc",
          "dervis", "bagoly", "ecetes", "angyal", "boglya"]

import random

# Inicializálom a tippeléseim számát
tsz = 0

# Véletlenszerűen választok egy szót a szavak listából
talaldki = random.choice(szavak)

while True:
    # Bekérem a tippemet
    tipp = input("Kérem a tippet! ")

    # Növelem a tippeléseim számát
    tsz += 1

    # Ha eltaláltam a szót, akkor kiírom a tippeléseim számát és kilépek a ciklusból
    if tipp == talaldki:
        print(f"{tsz} tippeléssel sikerült eltalálni.")
        break

    # Ha megadtam a "stop" szót, akkor kilépek a ciklusból
    elif tipp == 'stop':
        break

    # Ellenkező esetben ellenőrzöm, hogy mely karakterek egyeznek meg a tippemben és a kiválasztott szóban
    else:
        for i in range(len(talaldki)):
            if talaldki[i] == tipp[i]:
                print(tipp[i], end='')
            else:
                print('.', end='')
        print("")
