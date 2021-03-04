

# Desenvolvimento web (Python)

Olá, tudo bem? :call_me_hand:

Este repositório serve de guia de estudo da disciplina de Desenvolvimento Web da Faculdade Impacta de Tecnologia. 

Objetivos da disciplina: 

- Entender como está estruturada a comunicação cliente x servidor;
- Entender a estrutura geral do protocolo HTTP;
- Aprender a estruturar páginas na web com HTML;
- Aprender a estilizar páginas na web com CSS;
- Aprender a utilizar o JavaScript moderno nas páginas Web;
- Aprender a programar no servidor, usando o Python e o framework Flask.



#### Protocolo HTTP 

O caminho de uma requisição: 



![img](https://lh5.googleusercontent.com/C_Gh_tIvxGsYUO-s2z4Ps-bOv6LCbtUuquMyT4aQ-FccLFTzzTqfoj7ChXQKKaYp4W7iCFrwHggQ4bI1x-N62AnOGgVwJt51DmgmG7fYA-McUEFCDS9m5KK5VpZ3s55O4qNSVaIX)

- SIGLAS: 
  - HTTP (HyperText Transfer Protocol): protocolo de aplicação usada na comunicação da web e transferência de dados textuais. 
  - DNS (Domain Name System): sistema de tradução de domínios para endereços de IP's.
  - URL (Uniform Resorce Locator): mecanismo de localização de recursos/ arquivos usados na web.
  - UDP (User Datagram Protocol): protocolo de transporte de dados entre dois computadores, sem garantia de recebimento dos dados. 
  - TCP(Transfer Control Protocol): protocolo de transporte de dados entre dois computadores, com garantia de recebimento dos dados
  - IPv4/v6 (Internet Protocol): protocolo de endereçamento de aparelhos na internet.  

- Método HTTP
  - Métodos seguros: são aqueles que indicam que a requisição apenas trará alguma informação do servidor, sem alterar nada lá (GET, HEAD, OPTIONS e TRACE). 
  - Métodos idempotentes: são aqueles que diversas requisições iguais resultam a mesma coisa que apenas uma, ou seja, uma sequencia de GET para a mesma URL volta a mesma resposta todas as vezes (PUT e DELETE).



#### Padrão MVC e Programação no Servidor

Padrões de projeto (Design Patterns) foram divididos em três categorias:

- Padrões de criação (creational): são aqueles construídos para ajudar na criação de objetos. Dependendo do nível de complexidade de uma classe, a criação do objeto pode ser uma tarefa muito complicada ou depender de muitos dados, padrões como o **Factory Method** existem para facilitar esta tarefa. 
- Padrões estruturais (structural): estabelece maneiras mais flexíveis de trabalhar com composições de objetos, de forma a criar grandes estruturas de objetos. Exemplo: **Decorator**.
- Padrões comportamentais: tem como objetivo facilitar a comunicação e a passagem de dados entre objetos. Exemplo: **Observer**.

Padrão MVC

O padrão consiste nas três camadas que dão o seu nome: Model, View e Controller, cada camada é responsável por uma responsabilidade no sistema. 

- Model: representa o negócio que a aplicação foi construída para controlar. Desde modelos de dados (como classes de domínio e tabelas de banco de dados) a códigos de lógica de negócio, o modelo é o que traz o valor e necessidade para o software. **Tudo que for decisão do ponto de vista do negócio modelado fica nesta camada**.
- View: é a camada responsável por interagir com o usuário diretamente. Ela tem a responsabilidade de mostrar os dados da melhor maneira para o usuário e de coletar informações e interações dele para mandar para aplicação. 
- Controller: é a camada do meio, entre o modelo e a visualização. Ela é responsável pelo fluxo de dados e de trabalha da aplicação. Ela recebe as informações e interações da visualização via requisições HTTP e escolhe qual funcionalidade do modelo responderá por essas interações. Ao final do processamento, o controle ainda é responsável por decidir o caminho da resposta do processamento, devolvendo dados para a camada de visualização montar suas páginas da melhor maneira. 

Flask Framework

O Flask é um micro framework escrito em Python para a construção de aplicações web. O Flask não impõe uma arquitetura específica a ser seguida no desenvolvimento de aplicações, deixando a organização e estruturação a cargo dos desenvolvedores. 

Iniciando o Flask

- A construção de uma aplicação Flask se resume basicamente a criação e execução de um objeto específico. Para criarmos uma pequena aplicação, vamos criar um arquivo app.py no nosso projeto, onde a aplicação será criada.

```
from flask import Flask

app = Flask(__name__)

from controllers import * 

if __name__ == '__main__':
    app.run(
        debug=True
    )

```

Construindo um controller.py

```
##Precisamos da variavel app, que possui uma referência da aplicação que estamos usando. Pegamos a variavel app do módulo app
from app import app 

from flask import render_template

@app.route('/ola') 
##é o caminho da URL que responderá esse controle.
def hello_world():
	return 'Olá mundo'

## Outra forma de lidar com elementos HTML
@app.route('/ola')
def ola():
    return '<h1> testando </h1>'
    
## Utilizando o render_template
##Obs: As paginas html precisam estar na pasta de 'templates' caso contrário o Flask não consegue puxar o html

@app.route('/ola')
def ola():
    return render_template('ola.html')
```

- O Flask por padrão utiliza a porta 5000, então para vermos o hello world é necessário acessar http://localhost:5000/ola no navegador.

Respondendo GET e POST

- Todos os controles no Flask, por padrão, respondem apenas pelo GET. Para responder para o POST (ou qualquer outro método HTTP), é necessário configurar na definição de rota. 

Exemplo: Crie um HTML de formulário

```
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    {% extends 'index.html' %}
    <h1>Formulário</h1>
    <form method="POST">
        <div>
            <label for="nome">Nome</label>
            <input name="nome" id="nome" />
        </div>
        <button type="submit">Enviar</button>
    </form>
</body>
</html>
```

E adicione o seguinte método no controller.py

```
@app.route('/form', methods=['GET', 'POST'])
def formularios():
    if request.method == 'POST':
        print("Isto é um POST feito por", request.form['nome'])
    else:
        print("Isto é um GET")
    return render_template('formulario.html')
```

