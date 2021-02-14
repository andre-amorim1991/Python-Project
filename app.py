from flask import Flask, render_template, request

#por padrão render_template renderiza documentos no diretorio templates.
#para alterar a pasta padrão usamos template_folder e passamos o caminho desejado
app = Flask(__name__, template_folder="./src/views")


@app.route("/", methods=["GET", "POST"])
def home():
    if(request.method == "GET"):
        return render_template("index.html")
    else:
        if (request.form["num1"] != "" and request.form["num2"] != ""):
            if(request.form["opcao"] == "soma"):
                #os valores enviados pelo formularios são retornados como string.
                #foi feito a converssão com INT para que fosse feito a soma entre eles.
                soma = int(request.form['num1']) + int(request.form['num2'])
                #o navegador so imprime strings, aqui é feita a conversão da soma para string para que seja renderizado na pagina.
                return str(soma)
            
            elif(request.form["opcao"] == "subtracao"):
                sub = int(request.form['num1']) - int(request.form["num2"])
                return str(sub)
            
            #um exemplo para exiber o valor em json
            # elif(request.form["opcao"] == "subtracao"):
            #     sub = int(request.form['num1']) - int(request.form["num2"])
            #     return{
            #    "resultado": str(sub)

            #} 

            elif(request.form["opcao"] == "divisao"):
                #Uma barra para divisão ira exibir valor float
                # É inserido duas barra para que seja exibido um valor int.
                divi = int(request.form["num1"]) // int(request.form["num2"])
                return str(divi)

            else:
                multi = int(request.form['num1']) * int(request.form['num2'])
                return str(multi)

        else:
            return render_template('valorInvalido.html')

@app.route("/<int:id>")
def home_id(id):
    return str(id + 5)

@app.errorhandler(404)
def not_found(error):
    return render_template("erro.html")

@app.errorhandler(405)
def routeerror(error):
    return "method não encontrado"


#por padrão a porta é 5000, aqui foi definido para porta 8080.
#também é inserido debug=True para que não seja necessário restartar a o servidor.
app.run(port=8080, debug=True)