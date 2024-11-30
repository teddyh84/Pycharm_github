from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""
    erreur = ""
    num1 = ""
    num2 = ""
    result = ""
    if request.method == 'POST':
        if 'calculer' in request.form:
            try:
                # Récupérer les valeurs des champs du formulaire
                num1 = int(request.form['num1'])
                num2 = int(request.form['num2'])
                result = num1 + num2
                message = "Le résultat est : "
            except ValueError:
                erreur = "Erreur : veuillez entrer des nombres valides."

    return render_template('index.html', message=message, erreur=erreur, result=result, num1=num1, num2=num2)

if __name__ == '__main__':
    app.run(debug=True)
