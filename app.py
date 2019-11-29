from flask import Flask, request, Response
import routes

def bootstrap():
    # pega o nome do arquivo que está sendo executado
    app = Flask(__name__) 

    routes.load(app)

    # Retorna o próprio app
    return app

app = bootstrap()
app.run (debug=True, port=5000, host='0.0.0.0')

