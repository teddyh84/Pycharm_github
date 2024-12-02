from django.template.defaultfilters import lower
from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/traduction', methods=['GET', 'POST'])
def traduction():
    message_py = ""
    erreur_py = ""
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
    mot_choisi = random.randint(0, len(mots_anglais) - 1)
    mot_a_afficher = mots_anglais[mot_choisi]
    mot_a_trouver = traduction_fr[mot_choisi]
    question_py = mot_a_afficher # "hello"
    reponse_attendue_py = mot_a_trouver # "bonjour"
    reponse_py = ""
    if request.method == 'POST':
        if 'repondre' in request.form:
            try:
                # Récupérer les valeurs des champs du formulaire
                reponse_py = request.form['reponse']
                reponse_attendue_py = request.form['reponse_attendue']
                if lower(reponse_py)==lower(reponse_attendue_py):
                    message_py = "Bravo !"
                else:
                    message_py = "La bonne réponse était :" + reponse_attendue_py
                reponse_attendue_py = mot_a_trouver
                reponse_py = ""
            except:
                erreur_py = "Erreur : veuillez entrer une réponse valide."
    return render_template('traduction.html',
                           message_html=message_py,
                           erreur_html=erreur_py,
                           question_html=question_py,
                           reponse_attendue_html=reponse_attendue_py,
                           reponse_html=reponse_py
                           )

@app.route('/calculatrice', methods=['GET', 'POST'])
def calculatrice():
    message_py = ""
    erreur_py = ""
    num1_py = ""
    num2_py = ""
    result_py = ""
    if request.method == 'POST':
        if 'effacer' in request.form:
            message_py = "Tout a été effacé"
        if 'calculer' in request.form:
            try:
                # Récupérer les valeurs des champs du formulaire
                num1_py = int(request.form['num1'])
                num2_py = int(request.form['num2'])
                result_py = num1_py + num2_py
                message_py = "Le résultat est : "
            except ValueError:
                erreur_py = "Erreur : veuillez entrer des nombres valides."
    return render_template('calculatrice.html',
                           message_html=message_py,
                           erreur_html=erreur_py,
                           result_html=result_py,
                           num1_html=num1_py,
                           num2_html=num2_py
                           )

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html',
       message_html="",
       erreur_html="",
       result_html="",
       num1_html="",
       num2_html=""
       )

if __name__ == '__main__':
    app.run(debug=True)
