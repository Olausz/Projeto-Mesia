from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def program():
    return render_template("index.html")


@app.route('/contasto')
def contato():
    return render_template("contato.html")

if __name__ == "__main__":
    app.route(debug=True)