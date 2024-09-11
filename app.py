from flask import Flask, render_template

app = Flask(__name__)


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
