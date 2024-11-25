
def addition(n = 12):
    # n = 12 est le chiffre par défault
    nb_plus_5 = 5+n
    return nb_plus_5
def soustraction(n = 13):
    return n - 5

print("Le reultat du calcul est", addition(5))
print("Le reultat du calcul est", addition())
# J'ai pas mis de chiffre en parrentèses donc il prend le chiffre par défault
print("Le reultat du calcul est", addition(7))
print("Le reultat du calcul est", soustraction(7))
