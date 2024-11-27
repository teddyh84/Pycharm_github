import streamlit as st
import datetime

def main():
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
        # st.download_button(
        #    label="Téléchargez un exemple",
        #    data="Ceci est un exemple de fichier texte.",
        #    file_name="exemple.txt"
        # )

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