import streamlit as st

# Titre de l'application
st.title("Additionneur Simple")

# Instructions pour l'utilisateur
st.write("Entrez deux nombres et cliquez sur le bouton pour obtenir la somme.")

# Champs de saisie pour les deux nombres
num1 = st.number_input("Entrez le premier nombre :", value=0)
num2 = st.number_input("Entrez le deuxième nombre :", value=0)

# Bouton pour déclencher l'addition
if st.button("Calculer la somme"):
    somme = num1 + num2
    st.success(f"La somme de {num1} et {num2} est {somme}.")
else:
    st.error(f"ah bah boua")
