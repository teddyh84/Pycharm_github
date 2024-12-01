from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
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
    return render_template('index.html',
       message_html=message_py,
       erreur_html=erreur_py,
       result_html=result_py,
       num1_html=num1_py,
       num2_html=num2_py
    )

if __name__ == '__main__':
    app.run(debug=True)
