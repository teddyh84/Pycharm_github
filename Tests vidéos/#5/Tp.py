# tp : Jeu du Juste Prix
# choisir un nombre entre 1 et 1000
# tant que le jeu n'est pas fini
# -> demander à l'utilisateur "entrer un prix"
# -> si il trouve le juste prix "c'est gagné !"
# -> sinon on affiche "c'est moins" ou "c'est plus"

import random
nombre = random(1:1000)
def main():
    reponse_utilisateur = int(input("Entrer un prix"))
    if reponse_utilisateur == nombre:
        print("Bravo !")
    else:
        if reponse_utilisateur < nombre:
            print("C'est plus")
            main()
        else:
            print("C'est moins")
            main()