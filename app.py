from flask import Flask
# pega o nome do arquivo que está sendo executado
app = Flask(__name__) 

# Utiliza um decorator. A fusão logo abaixo dele.
@app.route("/")
def home():
    return "Hello flask 01!"

# Executa o código
# app.run()
app.run (debug=True, port=3000, host='0.0.0.0')