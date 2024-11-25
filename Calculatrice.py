print("Calculatrice")
premier_nombre = int(input("Premier nombre ?"))
deuxieme_nombre = int(input("Deuxième nombre ?"))
result_adi = premier_nombre + deuxieme_nombre
print("Le resultat de l'addition est " + str(result_adi))
result_sous = premier_nombre - deuxieme_nombre
print("Le resultat de la soustraction est " + str(result_sous))
result_multi = premier_nombre * deuxieme_nombre
print("Le resultat de la multiplication est " + str(result_multi))
if premier_nombre and deuxieme_nombre != 0:
    result_divi = premier_nombre / deuxieme_nombre
    print("Le resultat de la division est " + str(result_divi))
else:
    print("Il ne faut pas mettre de zéro pour une division !")
try:
    match premier_nombre:
        case 1:
            premier_nombre_lettre = "un"
        case 12:
            premier_nombre_lettre = "douze"
    print("coucou" + premier_nombre_lettre)
except:
    print("ah bah bouah !")