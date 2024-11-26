import streamlit as st
import random

st.title("Le pendu de Jules")
##### Etape 1 #####
# Créer une variable contenant un mot mystère de 5 lettres en minuscule à deviner (ex : "jules")

mot_a_deviner = ['frere', 'soleil', 'grand', 'aimer', 'noire', 'vague', 'croix', 'repos', 'rire',  'jaune', 'livre', 'luire', 'chant', 'chaud', 'herbe', 'beaux', 'doux', 'banal',  'maison', 'monde', 'danse', 'zebre', 'porte', 'pomme', 'jouet', 'terre', 'chose',  'vache', 'fleur', 'maman', 'ocean', 'tigre', 'arbre', 'nuage', 'biber', 'vivre',  'panda', 'verre', 'petit', 'table']



if "mot_mystere" not in st.session_state:
    st.session_state.mot_mystere = random.choice(mot_a_deviner) # Le mot à deviner
if "essais" not in st.session_state:
    st.session_state.essais = 0  # Nombre de tentatives
if "lettres" not in st.session_state:
    st.session_state.lettres = ["_", "_", "_", "_", "_"]  # Liste des lettres découvertes
if "lettres_loupees" not in st.session_state:
    st.session_state.lettres_loupees = []

##### Etape 2 #####
# Créer une variable numérique qui permet de compter le nombre de tentatives (mettre à 0 au début)
##### Etape 3 #####
# Créer une liste avec 5 valeurs identiques (qui est un underscore "_")

##### Etape 4 #####
# Demander une lettre à l'utilisateur
## Etape 4 et Etape 5 en une étape

##### Etape 5 #####
# Stocker la lettre renseignée dans une variable
st.session_state.lettre_donnee = st.text_input("Donne moi une lettre")

##### Etape 6 #####
# Faire une boucle for permet de récupérer chaque lettre du mot mystère ainsi que sa place (indice)
# Aide : pour cela il est possible d'utiliser la fonction "for indice, lettre in enumerate(mot_mystere):"
# Cette fonction for permet de boucler en récupérant l'indice et la lettre du mot mystère

def tester():
    nombre_essais = 10
    st.session_state.essais += 1
    trouve = 0
    for position, lettre in enumerate(st.session_state.mot_mystere):
        if lettre == st.session_state.lettre_donnee.lower():
            st.session_state.lettres[position] = lettre
            trouve = 1
    if trouve == 0:
        st.session_state.lettres_loupees.append(st.session_state.lettre_donnee.lower())
    st.header(" ".join(st.session_state.lettres))
    st.progress(st.session_state.essais * 10)
    st.write(st.session_state.essais, "/", nombre_essais)
    st.warning(" ".join(st.session_state.lettres_loupees))
    if "".join(st.session_state.lettres) == st.session_state.mot_mystere:
        st.success("T'es trop fort ✅ 😎 !!")
    elif st.session_state.essais == nombre_essais:
        st.error("T'es trop nul !!!!!!")
        st.info(st.session_state.mot_mystere)


if st.button("Valider"):
    tester()
##### Etape 7 #####
# Dans la boucle, ajouter une condition pour tester si la lettre est identique à la valeur saisie par l'utilisateur
# Si c'est identique, alors il faut remplacer dans la liste le "_" par la lettre au bon endroit (indice)

##### Etape 8 #####
# Ajouter 1 au compteur de tentative

##### Etape 9 #####
# Afficher la liste et le compteur de tentative

##### Etape 10 #####
# En bonus : redemander une nouvelle lettre et recommencer => Pas facile à faire !

