from flask import Flask, render_template

app = Flask(__name__)
# route -> hashtagtreinamentos.com/
# função -> o que você quer exibir naquela página
# template

@app.route("/")
def homepage():
    return "<p>Minha página</p><a href='/contatos'>Contatos</a>"

@app.route("/contatos")
def contatos():
    return "<h1>Contatos básicos</h1><p>Teste</p>"

@app.route("/produtos")
def produtos():
    return render_template("pagina1.html")

@app.route("/servicos/<nomeservico>")
def servicos(nomeservico):
    return render_template("pagina2.html",nome=nomeservico)
app.run(debug=True)







#@app.route("/usuarios/<nome_usuario>")
#def usuarios(nome_usuario):
#    return render_template("pagina1.html", nome_usuario=nome_usuario)

# colocar o site no ar
#if __name__ == "__main__":


    # servidor do heroku