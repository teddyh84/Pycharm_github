import streamlit as st

st.title("Bienvenue sur mon application")
st.write("Ceci est une application Streamlit simple.")


premier_nombre = int(input("Premier nombre ?"))
deuxieme_nombre = int(input("Deuxième nombre ?"))
result_adi = premier_nombre + deuxieme_nombre
print("Le resultat de l'addition est " + str(result_adi))

st.write("Le resultat de l'addition est " + str(result_adi))
