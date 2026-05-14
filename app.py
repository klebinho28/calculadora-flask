from flask import Flask, render_template, request,redirect,session

app =  Flask(__name__)

app.secret_key = "123456"

EMAIL = "admin@gmail.com"
SENHA = "123"


@app.route("/")
def login():
    return render_template("index.html")

@app.route("/login", methods=["post"])
def logar():

    email = request.form["email"]
    senha = request.form["senha"]

    if EMAIL == email and SENHA==senha:
        session["usuario"] = email
        return redirect("/calculadora")
    else:
        return"Email ou senha inválidos"

@app.route("/calculadora")
def calculadora():

    if "usuario" in session:

        return render_template("Calculadora.html")

    else:
        return redirect("/")
    

@app.route("/logout")
def logout():
    session.pop("usuario")

    return redirect("/")

@app.route("/somar", methods=["post"])
def somar():

    n1=int(request.form["n1"])
    n2=int(request.form["n2"])

    resultado = n1+n2

    return f"A soma dos resultados é {resultado}"

@app.route("/subtrair", methods=["post"])
def subtrair():

    n1=int(request.form["n1"])
    n2=int(request.form["n2"])

    resultado = n1-n2

    return f"A soma dos resultados é {resultado}"

@app.route("/multiplicar", methods=["post"])
def multiplicar():

    n1=int(request.form["n1"])
    n2=int(request.form["n2"])

    resultado = n1*n2

    return f"A soma dos resultados é {resultado}"
    
@app.route("/dividir", methods=["post"])
def dividir():

    n1=int(request.form["n1"])
    n2=int(request.form["n2"])

  
    if n2 == 0:
        return "Não é possível divdr por zero"

    resultado = n1/n2

    return f"A soma dos resultados é {resultado}"
    


if __name__=="__main__":
    app.run(debug=True)