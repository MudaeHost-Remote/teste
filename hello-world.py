from flask import Flask

# Criação do app Flask
app = Flask(__name__)

# Definindo uma rota para o servidor
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Rodando o app
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
