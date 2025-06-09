import json

def executa_masina_turing(configuratie, sir, limita_pasi=300):
    banda = list(sir) if sir else [configuratie["simbol_vid"]]
    pointer = 0
    stare = configuratie["stare_initiala"]
    stari_finale = set(configuratie["stari_finale"])
    reguli = configuratie["reguli"]
    simbol_vid = configuratie["simbol_vid"]

    pasi_efectuati = 0

    while pasi_efectuati < limita_pasi:
        if pointer < 0:
            banda.insert(0, simbol_vid)
            pointer = 0
        elif pointer >= len(banda):
            banda.append(simbol_vid)

        simbol_curent = banda[pointer]

        if stare in stari_finale:
            return True, "".join(banda), f"ACCEPTAT în starea finală: {stare}"

        aplicat = False
        for tranzitie in reguli:
            if tranzitie["st_actuala"] == stare and tranzitie["citit"] == simbol_curent:
                stare = tranzitie["st_urmatoare"]
                banda[pointer] = tranzitie["scris"]

                if tranzitie["mutare"] == "D":
                    pointer += 1
                elif tranzitie["mutare"] == "S":
                    pointer -= 1

                aplicat = True
                break

        if not aplicat:
            return False, "".join(banda), f"BLOCAT în starea {stare} la simbolul '{simbol_curent}'"

        pasi_efectuati += 1

    if stare in stari_finale:
        return True, "".join(banda), f"ACCEPTAT (limită de pași atinsă) în starea {stare}"

    return False, "".join(banda), f"Respins: s-a depășit limita de {limita_pasi} pași. Stare finală: {stare}"


# Încărcăm configurația MT din fișier JSON
config_path = 'palindromecheck.json'
with open(config_path, 'r') as f:
    masina_turing = json.load(f)

# Citim șirul de la utilizator
sir_intrare = input("Introduceți șirul de testat: ")

# Rulăm simularea MT
acceptat, banda_finala, mesaj = executa_masina_turing(masina_turing, sir_intrare)

# Afișăm rezultatele
print("\n==== REZULTAT ====")
print("Status:", "ACCEPTAT" if acceptat else "RESPINS")
print("Mesaj:", mesaj)
print("Conținut bandă finală:", banda_finala)
