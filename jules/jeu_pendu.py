import streamlit as st
import random

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


def main():
    st.title("Le pendu de Jules")
    mot_a_deviner = ['frere', 'soleil', 'grand', 'aimer', 'noire', 'vague', 'croix', 'repos', 'rire', 'jaune', 'livre',
                     'luire', 'chant', 'chaud', 'herbe', 'beaux', 'doux', 'banal', 'maison', 'monde', 'danse', 'zebre',
                     'porte', 'pomme', 'jouet', 'terre', 'chose', 'vache', 'fleur', 'maman', 'ocean', 'tigre', 'arbre',
                     'nuage', 'biber', 'vivre', 'panda', 'verre', 'petit', 'table']

    if "mot_mystere" not in st.session_state:
        st.session_state.mot_mystere = random.choice(mot_a_deviner)  # Le mot à deviner
    if "essais" not in st.session_state:
        st.session_state.essais = 0  # Nombre de tentatives
    if "lettres" not in st.session_state:
        st.session_state.lettres = ["_", "_", "_", "_", "_"]  # Liste des lettres découvertes
    if "lettres_loupees" not in st.session_state:
        st.session_state.lettres_loupees = []

    st.session_state.lettre_donnee = st.text_input("Donne moi une lettre")

    if st.button("Valider"):
        tester()

