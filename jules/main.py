import streamlit as st

import jeu_pendu
import jeu_traduction
import Calculatrice
import jeu_mastermind
import jeu_simonsays
import jeu_yams
import commentaire
import formulaire
import onglets
# from streamlit_option_menu import option_menu
#
# with st.sidebar:
#     selected = option_menu(
#         menu_title="Jeux",
#         options=["Home", "Contacy"],
#         icons=["house-heart-fill", "envelope-heart-fill"],
#         menu_icon="heart-eyes-fill",
#         default_index=0,
        # orientation="horizontal",
        # styles={
        #     "container": {"padding": "5px", "background-color": "#f0f0f0"},
        #     "icon": {"color": "blue", "font-size": "25px"},
        #     "nav-link": {
        #         "font-size": "16px",
        #         "text-align": "left",
        #         "margin": "5px",
        #         "--hover-color": "#eee",
        #     },
        #     "nav-link-selected": {"background-color": "#02ab21"},
        # },
    #)

if "menu" not in st.session_state:
    st.session_state.menu = "Accueil"
    st.title("Choisissez un menu à gauche")
    st.write("Pour le moment, seul le Pendu et les commentaires sont disponibles")

st.sidebar.title("🎮 Jeux")
if st.sidebar.button("🪢 Pendu"):
    st.session_state.menu = "Pendu"
if st.sidebar.button("traducteur"):
    st.session_state.menu = "traducteur"
if st.sidebar.button("🧮 Calculatrice"):
    st.session_state.menu = "Calculatrice"
if st.sidebar.button("⚡ Simon says"):
    st.session_state.menu = "Simon"
if st.sidebar.button("🎲 Yams"):
    st.session_state.menu = "Yams"
if st.sidebar.button("🔵 Mastermind"):
    st.session_state.menu = "Mastermind"
st.sidebar.title("📧 Contact")
if st.sidebar.button("💬 Commentaires"):
    st.session_state.menu = "Commentaires"
st.sidebar.title("Exemples")
if st.sidebar.button("Page avec onglets"):
    st.session_state.menu = "Onglets"
if st.sidebar.button("Exemple de formulaire"):
    st.session_state.menu = "Formulaire"

# Affichage selon le menu sélectionné
match st.session_state.menu:
    case "Pendu":
        jeu_pendu.main()

    case "Calculatrice":
        Calculatrice.main()

    case "traducteur":
        jeu_traduction.main()

    case "Mastermind":
        jeu_mastermind.main()
        #st.title("Mastermind")
        #st.write("En cours de construction ...")

    case "Yams":
        jeu_yams.main()
        #st.title("Yams")
        #st.write("En cours de construction ...")

    case "Simon":
        jeu_simonsays.main()
        #st.title("Simon says")
        #st.write("En cours de construction ...")

    case "Commentaires":
        commentaire.main()

    case "Onglets":
        onglets.main()

    case "Formulaire":
        formulaire.main()