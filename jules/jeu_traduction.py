import random
import time
import streamlit as st

def main():
    mots_anglais = ['Apple', 'Ball', 'Cat', 'Dog', 'Fish', 'House', 'Tree', 'Book', 'Chair', 'Table',
                    'Car', 'Bike', 'Sun', 'Moon', 'Water', 'Fire', 'Food', 'Hand', 'Foot',
                    'King', 'Queen', 'Boy', 'Girl', 'Baby', 'Happy (Indice : H...)', 'Sad', 'Love', 'Good', 'Bad',
                    'Day', 'Night', 'Rain', 'Snow', 'Wind', 'Sky', 'Light', 'Dark', 'River', 'Beach',
                    'Bread', 'Milk', 'Tea', 'Sugar', 'Cake', 'Phone', 'Bag', 'Pen', 'Door', 'Window']
    traduction_fr = ['Pomme', 'Balle', 'Chat', 'Chien', 'Poisson', 'Maison', 'Arbre', 'Livre', 'Chaise', 'Table',
                     'Voiture', 'Vélo', 'Soleil', 'Lune', 'Eau', 'Feu', 'Nourriture', 'Main', 'Pied',
                     'Roi', 'Reine', 'Garçon', 'Fille', 'Bébé', 'Heureux', 'Triste', 'Amour', 'Bon', 'Mauvais',
                     'Jour', 'Nuit', 'Pluie', 'Neige', 'Vent', 'Ciel', 'Lumière', 'Sombre', 'Rivière', 'Plage',
                     'Pain', 'Lait', 'Thé', 'Sucre', 'Gâteau', 'Téléphone', 'Sac', 'Stylo', 'Porte', 'Fenêtre']

    # Pour le premier lancement on crée les variables
    if "mots_anglais_a_trouver" not in st.session_state:
        st.session_state.mots_anglais_a_trouver = mots_anglais
    if "mots_francais_a_trouver" not in st.session_state:
        st.session_state.mots_francais_a_trouver = traduction_fr
    if "nb_bonnes_reponses" not in st.session_state:
        st.session_state.nb_bonnes_reponses = 0
    if "nb_reponses" not in st.session_state:
        st.session_state.nb_reponses = 0
    #while True:

    mot_choisi = random.randint(0, len(st.session_state.mots_anglais_a_trouver)-1)
    mot_a_afficher = st.session_state.mots_anglais_a_trouver[mot_choisi]
    st.write(mot_a_afficher)
    reponse = traduction_fr[mot_choisi]
    time.sleep(0.75)
    reponse_utilisateur = st.text_input("Et en français ?")
    if st.button ("Valider"):
        if reponse_utilisateur.lower() == reponse.lower():
            st.write("Bravo ! 😊")
            st.session_state.nb_bonnes_reponses += 1
        else:
            st.write("La bonne réponse était : ", reponse)
        st.session_state.nb_reponses += 1
        st.write("Tu as ", st.session_state.nb_bonnes_reponses, "/ ", st.session_state.nb_reponses)
        del st.session_state.mots_anglais_a_trouver[mot_choisi]
        del st.session_state.mots_francais_a_trouver[mot_choisi]
        time.sleep(1.25)

