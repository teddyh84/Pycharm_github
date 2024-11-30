from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add', methods=['POST'])
def add():
    try:
        # Récupérer les valeurs des champs du formulaire
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        result = num1 + num2
    except ValueError:
        # Gérer les erreurs de conversion
        return render_template('result.html', result="Erreur : veuillez entrer des nombres valides.")

    return render_template('result.html', result=f"Le résultat est : {result}")


if __name__ == '__main__':
    app.run(debug=True)
