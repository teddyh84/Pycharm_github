import streamlit as st
import pandas as pd

def main():
    st.title("Commentaires")
    with st.form("comment_form"):
        # Widgets du formulaire
        jeu = st.selectbox("Choisissez un jeu", ["Pendu", "Simon Says", "Yams", "Mastermind"])
        nom = st.text_input("Votre nom")
        remarque = st.text_area("Vos commentaires")

        # Bouton de soumission
        submitted = st.form_submit_button("Envoyer")

    # Action après la soumission
    if submitted:
        if nom and remarque:  # Vérification que le nom et le commentaire sont remplis
            # Sauvegarder les résultats dans un fichier texte
            with open("./commentaires.txt", "a") as f:
                f.write(f"{jeu};{nom};{remarque}\n")

            # Confirmation pour l'utilisateur
            st.success("Merci pour votre commentaire !")
        else:
            st.error("Veuillez remplir tous les champs.")

    try:
        # Lire le fichier texte et transformer en DataFrame
        comments_df = pd.read_csv("./commentaires.txt", sep=";", names=["Jeu", "Nom", "Commentaire"])

        # Afficher le tableau
        st.subheader("Tableau des commentaires")
        st.dataframe(comments_df)
    except FileNotFoundError:
        st.warning("Aucun commentaire n'a encore été enregistré.")