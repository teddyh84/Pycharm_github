import streamlit as st

def main():
    st.title("Page avec onglets")
    st.write("En cours de construction")
    # Titre de l'application
    st.title("Application avec Onglets")

    # Onglets
    tabs = st.tabs(["Accueil", "À propos", "Contact"])

    with tabs[0]:
        st.subheader("Bienvenue sur la page d'accueil")
        st.write("Contenu de la page d'accueil.")

    with tabs[1]:
        st.subheader("À propos")
        st.write("Ici, vous pouvez ajouter des informations sur l'application.")

    with tabs[2]:
        st.subheader("Contact")
        st.write("Formulaire ou informations de contact.")