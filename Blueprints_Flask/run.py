from aplicacao import app

app.secret_key = "MINHA-CHAVE-SECRETA"
if __name__ == '__main__':
    app.run()