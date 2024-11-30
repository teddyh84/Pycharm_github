import streamlit as st

def main():
    st.title("Calculatrice")
    premier_nombre = st.number_input(
        "Premier nombre ?",
        step=1,  # Incrément sans décimales
        format="%d"
    )
    deuxieme_nombre = st.number_input(
        "Deuxième nombre ?",
        step=1,  # Incrément sans décimales
        format="%d"
    )
    result_adi = premier_nombre + deuxieme_nombre
    st.write("Le resultat de l'addition est " + str(result_adi))
    result_sous = premier_nombre - deuxieme_nombre
    st.write("Le resultat de la soustraction est " + str(result_sous))
    result_multi = premier_nombre * deuxieme_nombre
    st.write("Le resultat de la multiplication est " + str(result_multi))
    if premier_nombre and deuxieme_nombre != 0:
        result_divi = premier_nombre / deuxieme_nombre
        st.write("Le resultat de la division est " + str(result_divi))
    else:
        st.write("Il ne faut pas mettre de zéro pour une division !")

    # try:
    #     match premier_nombre:
    #         case 1:
    #             premier_nombre_lettre = "un"
    #         case 12:
    #             premier_nombre_lettre = "douze"
    #     st.write("coucou" + premier_nombre_lettre)
    # except:
    #     st.write("ah bah bouah !")