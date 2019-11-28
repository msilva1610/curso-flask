from flask import Flask, request
# pega o nome do arquivo que está sendo executado
app = Flask(__name__) 

# Utiliza um decorator. A fusão logo abaixo dele.
@app.route("/")
def showName():
    #pegar um valor do query string
    name = request.args.get("name")
    return f'Name: {name}'
    # return "Name:"

@app.route('/name/<name>')
def showName_param(name):
    return name


# Executa o código
# app.run()
app.run (debug=True, port=5000, host='0.0.0.0')