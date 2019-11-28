from flask import flask
# pega o nome do arquivo que está sendo executado
app = FLASK(__name__) 

# Utiliza um decorator. A fusão logo abaixo dele.
@app.route("/")
def home():
    return "Hello word!"

# Executa o código
app.run()