# import random
# import time
import streamlit as st


# def init():
#     st.session_state.mots_anglais_a_trouver = ['Apple', 'Ball', 'Cat', 'Dog', 'Fish', 'House', 'Tree', 'Book', 'Chair', 'Table',
#                     'Car', 'Bike', 'Sun', 'Moon', 'Water', 'Fire', 'Food', 'Hand', 'Foot',
#                     'King', 'Queen', 'Boy', 'Girl', 'Baby', 'Happy (Indice : H...)', 'Sad', 'Love', 'Good', 'Bad',
#                     'Day', 'Night', 'Rain', 'Snow', 'Wind', 'Sky', 'Light', 'Dark', 'River', 'Beach',
#                     'Bread', 'Milk', 'Tea', 'Sugar', 'Cake', 'Phone', 'Bag', 'Pen', 'Door', 'Window']
#     st.session_state.mots_francais_a_trouver = ['Pomme', 'Balle', 'Chat', 'Chien', 'Poisson', 'Maison', 'Arbre', 'Livre', 'Chaise', 'Table',
#                      'Voiture', 'Vélo', 'Soleil', 'Lune', 'Eau', 'Feu', 'Nourriture', 'Main', 'Pied',
#                      'Roi', 'Reine', 'Garçon', 'Fille', 'Bébé', 'Heureux', 'Triste', 'Amour', 'Bon', 'Mauvais',
#                      'Jour', 'Nuit', 'Pluie', 'Neige', 'Vent', 'Ciel', 'Lumière', 'Sombre', 'Rivière', 'Plage',
#                      'Pain', 'Lait', 'Thé', 'Sucre', 'Gâteau', 'Téléphone', 'Sac', 'Stylo', 'Porte', 'Fenêtre']
#     st.session_state.mot_choisi = -1
#     st.session_state.mot_a_afficher = ""
#     st.session_state.reponse_utilisateur = ""
#     st.session_state.message = ""
#     st.session_state.nb_bonnes_reponses = 0
#     st.session_state.nb_reponses = 0
#     st.session_state.etat = "init"
#
# def generer_mot():
#     st.session_state.mot_choisi = random.randint(0, len(st.session_state.mots_anglais_a_trouver) - 1)
#     st.session_state.mot_a_afficher = st.session_state.mots_anglais_a_trouver[st.session_state.mot_choisi]
#     st.session_state.reponse_attendue = st.session_state.mots_francais_a_trouver[st.session_state.mot_choisi]
#     st.session_state.reponse_utilisateur = ""
#     st.session_state.etat = "attente_reponse"
#
# def tester_reponse():
#     if st.session_state.reponse_utilisateur.lower() == st.session_state.reponse_attendue.lower():
#         st.session_state.message = "Bravo ! 😊" + " (" + st.session_state.mot_a_afficher + " = " + st.session_state.reponse_utilisateur + ")"
#         st.session_state.nb_bonnes_reponses += 1
#         st.session_state.etat = "reponse_donnee"
#     else:
#         st.session_state.message = "La bonne réponse était : " + st.session_state.reponse
#         st.session_state.etat = "reponse_donnee"
#     st.session_state.score = "Tu as " + st.session_state.nb_bonnes_reponses + "/ " + st.session_state.nb_reponses
#     st.session_state.nb_reponses += 1
#     del st.session_state.mots_anglais_a_trouver[st.session_state.mot_choisi]
#     del st.session_state.mots_francais_a_trouver[st.session_state.mot_choisi]
#     # time.sleep(1.25)
#
# def afficher():
#     st.write(st.session_state.mot_a_afficher)
#     # time.sleep(0.75)
#     match st.session_state.etat:
#         case "init":
#             if st.button("Commencer"):
#                 generer_mot()
#         case "attente_reponse":
#             st.text_input("Et en français ?", key="reponse_utilisateur")
#             if st.button("Valider"):
#                 tester_reponse()
#             st.session_state.etat = "attente_reponse"
#         case "reponse_donnee":
#             if st.button("Nouveau mot"):
#                 generer_mot()
#             st.write(st.session_state.message)
#             st.write(st.session_state.score)
#             st.session_state.etat="attente_reponse"
#
#
# def main():
#     if "action" not in st.session_state:
#         init()
#     afficher()


def init():
    if "etat" not in st.session_state:
        st.session_state.etat = "init"


def afficher():
    # Définir les messages et les textes des boutons selon l'état
    messages = {
        "init": "Bienvenue ! Cliquez sur le bouton pour passer à l'étape 1.",
        "etape_1": "Vous êtes à l'étape 1. Cliquez pour continuer à l'étape 2.",
        "etape_2": "Bravo, vous êtes arrivé à l'étape finale ! Vous pouvez revenir à l'accueil."
    }
    boutons = {
        "init": "Étape 1",
        "etape_1": "Étape 2",
        "etape_2": "Revenir à l'accueil"
    }

    # Afficher le message correspondant à l'état actuel
    st.write(messages[st.session_state.etat])

    # Bouton dynamique avec gestion des clics
    if st.button(boutons[st.session_state.etat], key="button"):
        # Mise à jour de l'état en fonction de l'état actuel
        if st.session_state.etat == "init":
            st.session_state.etat = "etape_1"
        elif st.session_state.etat == "etape_1":
            st.session_state.etat = "etape_2"
        elif st.session_state.etat == "etape_2":
            st.session_state.etat = "init"

    # Afficher l'état actuel pour feedback
    st.write(f"**État actuel : {st.session_state.etat}**")


def main():
    init()
    afficher()


if __name__ == "__main__":
    main()