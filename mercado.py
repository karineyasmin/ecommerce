from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mercado.db"
db.init_app(app)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(length=30), nullable=False, unique=True)
    preco = db.Column(db.Integer, nullable=False)
    cod_barra = db.Column(db.String(length=12), nullable=False, unique=True)
    descricao = db.Column(db.String(length=1024), nullable=False, unique=True)


@app.route("/")
def page_home():
    return render_template("home.html")


@app.route("/produtos")
def page_produto():
    itens = [
        {"id": 1, "nome": "Celular", "cod_barra": "3213123123", "preco": 1200},
        {"id": 2, "nome": "Notebook", "cod_barra": "43423423", "preco": 3500},
    ]
    return render_template("produtos.html", itens=itens)


if __name__ == "__main__":
    app.run(debug=True)
