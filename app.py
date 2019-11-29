from flask import Flask, request, Response
# pega o nome do arquivo que está sendo executado
app = Flask(__name__) 


@app.route("/home")
def home():
    # return Response("Home page",200,{})
    return "Home page",200



# Utiliza um decorator. A fusão logo abaixo dele.
@app.route("/")
def showName():
    #pegar um valor do query string
    name = request.args.get("name")
    return f'Name: {name}'
    # return "Name:"

@app.route('/name')
@app.route('/name/<name>')
def showName_param(name = None):
    if name:
        return name
    return "Objeto name não foi definido"


# Executa o código
# app.run()
app.run (debug=True, port=5000, host='0.0.0.0')