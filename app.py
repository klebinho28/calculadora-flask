from flask import Flask ,render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/somar", methods=["post"])
def somar():

    n1 = int(request.form["n1"])
    n2 = int(request.form["n2"])

    resultado1 = n1+n2
   
    return f"O resultado da soma de n1+n2 é {resultado1}"

@app.route("/subtrair" , methods=["post"])
def subtrair():

    n1 = int(request.form["n1"])
    n2 = int(request.form["n2"])

    resultado2 = n1-n2
   
    return f"O resultado da subtração de n1-n2 é {resultado2}"

@app.route("/multiplicar" , methods=["post"])
def multiplicar():

    n1 = int(request.form["n1"])
    n2 = int(request.form["n2"])

    resultado3 = n1*n2
   
    return f"O resultado da soma de n1*n2 é {resultado3}"


@app.route("/dividir" , methods=["post"])
def dividir():

    n1 = int(request.form["n1"])
    n2 = int(request.form["n2"])

    resultado4 = n1/n2
   
    return f"O resultado da soma de n1+n2 é {resultado4}"



if __name__==("__main__"):
    app.run(debug=True)