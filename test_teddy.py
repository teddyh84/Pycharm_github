import streamlit as st
import random
import datetime
import pandas as pd

# Initialisation de la session
if "menu" not in st.session_state:
    st.session_state.menu = "Accueil"

# Menu latéral
st.sidebar.title("🎮 Jeux")
if st.sidebar.button("🪢 Pendu"):
    st.session_state.menu = "Pendu"
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
        st.title("Le pendu de Jules")
        mot_a_deviner = ['frere', 'soleil', 'grand', 'aimer', 'noire', 'vague', 'croix', 'repos', 'rire',  'jaune', 'livre', 'luire', 'chant', 'chaud', 'herbe', 'beaux', 'doux', 'banal',  'maison', 'monde', 'danse', 'zebre', 'porte', 'pomme', 'jouet', 'terre', 'chose',  'vache', 'fleur', 'maman', 'ocean', 'tigre', 'arbre', 'nuage', 'biber', 'vivre',  'panda', 'verre', 'petit', 'table']

        if "mot_mystere" not in st.session_state:
            st.session_state.mot_mystere = random.choice(mot_a_deviner) # Le mot à deviner
        if "essais" not in st.session_state:
            st.session_state.essais = 0  # Nombre de tentatives
        if "lettres" not in st.session_state:
            st.session_state.lettres = ["_", "_", "_", "_", "_"]  # Liste des lettres découvertes
        if "lettres_loupees" not in st.session_state:
            st.session_state.lettres_loupees = []

        st.session_state.lettre_donnee = st.text_input("Donne moi une lettre")

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

    case "Commentaires":
        st.title("Commentaires")
        with st.form("comment_form"):
            # Widgets du formulaire
            jeu = st.selectbox("Choisissez un jeu", ["Pendu", "Autre"])
            nom = st.text_input("Votre nom")
            remarque = st.text_area("Vos commentaires")

            # Bouton de soumission
            submitted = st.form_submit_button("Envoyer")

        # Action après la soumission
        if submitted:
            if nom and remarque:  # Vérification que le nom et le commentaire sont remplis
                # Sauvegarder les résultats dans un fichier texte
                with open("commentaires.txt", "a") as f:
                    f.write(f"Jeu: {jeu};Nom: {nom};Commentaire: {remarque}\n")

                # Confirmation pour l'utilisateur
                st.success("Merci pour votre commentaire !")
            else:
                st.error("Veuillez remplir tous les champs.")

        try:
            # Lire le fichier texte et transformer en DataFrame
            comments_df = pd.read_csv("commentaires.txt", sep=";", names=["Jeu", "Nom", "Commentaire"])

            # Afficher le tableau
            st.subheader("Tableau des commentaires")
            st.dataframe(comments_df)
        except FileNotFoundError:
            st.warning("Aucun commentaire n'a encore été enregistré.")

    case "Onglets":
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

    case "Formulaire":
        st.title("Formulaire Complet")

        # Formulaire principal
        with st.form("full_form"):
            # 1. Champs de Texte
            name = st.text_input("Nom")
            message = st.text_area("Message")

            # 2. Entrées Numériques
            age = st.number_input("Âge", min_value=0, max_value=120, value=25)
            price = st.number_input("Prix estimé", min_value=0.0, max_value=10000.0, value=100.0, step=0.5)

            # 3. Cases à Cocher
            agree = st.checkbox("J'accepte les conditions générales")

            # 4. Sélecteurs
            option = st.selectbox("Choisissez une option", ["Option A", "Option B", "Option C"])
            choices = st.multiselect("Choisissez plusieurs options", ["Option 1", "Option 2", "Option 3"])

            # 5. Boutons
            st.write("Cliquez sur le bouton ci-dessous si vous voulez saluer.")
            greeting_clicked = st.form_submit_button("Dire Bonjour")

            # 6. Curseurs
            single_value = st.slider("Réglez une valeur", min_value=0, max_value=100, value=50)
            range_values = st.slider("Sélectionnez une plage", min_value=0, max_value=100, value=(20, 80))

            # 7. Dates et Temps
            selected_date = st.date_input("Sélectionnez une date", datetime.date.today())
            selected_time = st.time_input("Sélectionnez une heure", datetime.time(8, 0))

            # 8. Téléchargement de Fichiers
            uploaded_file = st.file_uploader("Téléchargez un fichier")

            # 9. Téléchargement de Fichiers (Lien)
            #st.download_button(
            #    label="Téléchargez un exemple",
            #    data="Ceci est un exemple de fichier texte.",
            #    file_name="exemple.txt"
            #)

            # 10. Widgets Riches
            selected_color = st.color_picker("Choisissez une couleur", "#00f900")

            # Bouton de soumission
            submitted = st.form_submit_button("Soumettre")

            # Actions après la soumission
        if submitted:
            st.write("### Résultats")
            st.write(f"Nom : {name}")
            st.write(f"Message : {message}")
            st.write(f"Âge : {age}")
            st.write(f"Prix estimé : {price} €")
            st.write(f"Conditions acceptées : {'Oui' if agree else 'Non'}")
            st.write(f"Option choisie : {option}")
            st.write(f"Options multiples choisies : {choices}")
            st.write(f"Valeur sélectionnée : {single_value}")
            st.write(f"Plage sélectionnée : {range_values}")
            st.write(f"Date choisie : {selected_date}")
            st.write(f"Heure choisie : {selected_time}")
            if uploaded_file:
                st.write(f"Fichier téléchargé : {uploaded_file.name}")
            else:
                st.write("Aucun fichier téléchargé.")
            st.write(f"Couleur choisie : {selected_color}")

        if greeting_clicked:
            st.write("Bonjour ! Merci d'avoir cliqué !")