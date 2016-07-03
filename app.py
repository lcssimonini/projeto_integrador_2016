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

# questionarios

@app.route("/logica/questionario")
def logica_form():
    return render_template("forms/logica_form.html")

@app.route("/arquitetura/questionario")
def arquitetura_form():
    return render_template("forms/arquitetura_form.html")

@app.route("/ingles/questionario")
def ingles_form():
    return render_template("forms/ingles_form.html")

@app.route("/sistemasop/questionario")
def sistemasop_form():
    return render_template("forms/sistemasop_form.html")

@app.route("/webdesign/questionario")
def webdesign_form():
    return render_template("forms/webdesign_form.html")

@app.route("/metodologia/questionario")
def metodologia_form():
    return render_template("forms/metodologia_form.html")

# certificados

@app.route("/metodologia/certificado")
def metodologia_cert():
    return render_template("certs/metodologia_cert.html")

@app.route("/arquitetura/certificado")
def arquitetura_cert():
    return render_template("certs/arquitetura_cert.html")

@app.route("/sistemasop/certificado")
def sistemasop_cert():
    return render_template("certs/sistemasop_cert.html")

@app.route("/ingles/certificado")
def ingles_cert():
    return render_template("certs/ingles_cert.html")

@app.route("/logica/certificado")
def logica_cert():
    return render_template("certs/logica_cert.html")

@app.route("/webdesign/certificado")
def webdesign_cert():
    return render_template("certs/webdesign_cert.html")

if __name__ == "__main__":
    app.run(debug=True)
