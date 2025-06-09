def incarca_matrice(nume_fisier):
    try:
        with open(nume_fisier, 'r') as f:
            matrice = []
            for linie in f:
                try:
                    rand = [int(val) for val in linie.strip().split()]
                    matrice.append(rand)
                except ValueError:
                    print(f"Eroare: linia '{linie.strip()}' conține valori nevalide!")
                    return None
    except FileNotFoundError:
        print(f"Eroare: fișierul '{nume_fisier}' nu există!")
        return None

    if not matrice:
        print("Eroare: fișierul este gol sau nu are conținut valid.")
        return None

    lungime_rand = len(matrice[0])
    for rand in matrice:
        if len(rand) != lungime_rand:
            print("Eroare: liniile nu au aceeași lungime. Nu este o matrice validă.")
            return None

    return matrice


def salveaza_matrice(fisier_salveaza, fisier_citire):
    matrice = incarca_matrice(fisier_citire)
    if matrice is None:
        return

    try:
        with open(fisier_salveaza, 'w') as f_out:
            for rand in matrice:
                linie_text = ' '.join(str(x) for x in rand)
                f_out.write(linie_text + '\n')
    except IOError:
        print(f"Eroare: nu am putut scrie în fișierul '{fisier_salveaza}'.")


# Exemplu de utilizare
mat = incarca_matrice('matrice')
print(mat)
salveaza_matrice('fn', 'matrice')

