from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", menu_cursos=False)

@app.route("/arquitetura")
def arquitetura():
    return render_template("arquitetura.html", menu_cursos=True)

@app.route("/webdesign")
def webdesign():
    return render_template("webdesign.html", menu_cursos=True)

@app.route("/logica")
def logica():
    return render_template("logica.html", menu_cursos=True)

@app.route("/ingles")
def ingles():
    return render_template("ingles.html", menu_cursos=True)

@app.route("/metodologia")
def metodologia():
    return render_template("metodologia.html", menu_cursos=True)

@app.route("/sistemasop")
def sistemasop():
    return render_template("sistemasop.html", menu_cursos=True)

@app.route("/contato")
def contato():
    return render_template("sistemasop.html", menu_cursos=True)

if __name__ == "__main__":
    app.run(debug=True)
