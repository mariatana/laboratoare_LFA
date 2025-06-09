#NFA
import json

def inchidere_epsilon(automat, stare_initiala):
    rezultat = set(stare_initiala)
    modificat = True

    while modificat:
        modificat = False
        for stare in list(rezultat):
            for tranzitie in automat["routes"]:
                if tranzitie["inc"] == stare and tranzitie["state"] == "ε":
                    for urmatoare in tranzitie["fin"]:
                        if urmatoare not in rezultat:
                            rezultat.add(urmatoare)
                            modificat = True
    return rezultat

def ruleaza_nfa(automat, cuvant):
    stari_active = inchidere_epsilon(automat, set(automat["start"]))

    for caracter in cuvant:
        stari_urmatoare = set()
        for stare in stari_active:
            for tranzitie in automat["routes"]:
                if tranzitie["inc"] == stare and tranzitie["state"] == caracter:
                    stari_urmatoare.update(tranzitie["fin"])
        stari_active = inchidere_epsilon(automat, stari_urmatoare)

    return any(stare in automat["final"] for stare in stari_active)

# Citire NFA din fișier JSON
with open("NFA.json", "r") as fisier_json:
    automat_nfa = json.load(fisier_json)

# Citire input de la utilizator
cuvant = input("Dă un șir de intrare: ")

# Verificare și afișare rezultat
rezultat = ruleaza_nfa(automat_nfa, cuvant)
print("ACCEPTAT" if rezultat else "RESPINS")


