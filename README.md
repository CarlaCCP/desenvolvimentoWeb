

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

#### **Manipulação do DOM**

Quando o HTML é carregado pelo navegador na requisição inicial, começa a fase de **análise e tradução do código HTML** (chamado em inglês de *HTML parsing*), onde o navegador lê linha a linha do código HTML, entendendo as tags e traduzindo-as para os elementos que aparecerão no navegador (visuais ou de configuração). Esses elementos são representados por objetos em memória dentro do navegador e como o HTML é uma representação hierárquica de elementos (tags dentro de tags), o navegador representa essa estrutura usando uma árvore de objetos na memória. Essa representação em árvore dos elementos HTML de um documento HTML é chamada de **Document Object Model (DOM)**.

O método mais simples para buscar um elemento na árvore é o **document.getElementById(id)**, outros exemplos:

- getElementsByTagName: volta um vetor de elementos pela sua tag.
- getElementsByClassName: volta um vetor com elementos contendo a classe passada.

Para ter mais flexibilidade é recomendado os querySelectors: **querySelector** e **querySelectorAll**. A deferença entre os dois é que o  querySelector volta o primeiro elemento no DOM que obedecer o seletor passado (ou null se não houver) e o querySelectorAll sempre volta um nodeList (similar ao vetor) com os elementos que obedecem ao seletor passado (ou vazio caso nenhum obedeça).

Obs: Para evitar dos scripts serem lidos logo no começo do recebimento HTML, usa-se **async** e o **defer**

- async: torna todo o processo de baixar e traduzir o JavaScript em um processo assíncrono, ou seja, o navegador faz ambas as coisas ao mesmo tempo em que termina de analisar o código HTML. Esse atributo é recomendado para scripts que não precisam do DOM já estar carregado para funcionar, pois é possível que o script acabe de executar antes do DOM esteja pronto.
- defer: faz com que o processo de baixar os arquivos de JavaScript seja assíncrono (assim como o **async**), mas sua tradução e execução são feitas após o carregamento completo do HTML e o DOM esteja pronto.



Alterando e acessando **propriedades**

- textContent: ignora tags HTML que estejam no conteúdo.
- innerHTML: não ignora tags.



Alterando e acessando **estilos**

```
<p style="color: red; font-weight="bold">Isso é um parágrafo!</p>
```

- Alterando

```
p.style.textTransform = 'uppercase'
```

- Acessando

```
p.style.color
p.style.fontWeight
```



Alterando e acessando **classes**

Outra propriedade que funciona de uma maneira diferente é o **class**. Como ele é multivalorado (permite vários valores diferentes) podemos manipular ele por suas propriedades diferentes: **className** e **classList**. A primeira (**className**) utiliza uma representação em string. Toda alteração (inclusão ou remoção de classes) só pode ser feita com operações de string, não sendo muito prático para manipulações mais complexas.

Já a **classList** representa as classes como um vetor especial [DOMTokenList ] com todas as classes definidas no elemento HTML e alguns métodos práticos para manipular seus valores: **add** (adiciona uma classe nova), **remove** (remove uma classe específica, se existir) e **contains** (verifica se uma classe existe no vetor).



Alterando **elementos internos**

Exemplo de lista não ordenada

```
const item = document.createElement('li')
item.textContent = "Minas Gerais"
ul.appendChild(item) 

<!-- Se quisermos adicionar em um posição especifica
, podemos usar o insertBefore e se quisermos remover
no próprio elemento item.remove() -->
```



Escutando eventos com JS

```
<button type="button">
Isso é um botão
</button>
```

```
const botao = document.querySelector('button')

/* A associação entre um listener e o seu evento
é chamado de registtro de listener. Ocorre com o 'on' e 'addElementListener' */

botao.onclick = function(event){
	alert("Evento pelo onclick")
}

botao.addEventListener('click', function(event){
	alert('Evento pelo addEventListener')
})
```

A diferença entre as duas maneiras é que o método **addEventListener** permite que registremos quantas funções quisermos em um único evento, já as propriedades **on\*** permitem apenas um *listener* por evento. Podemos usar ambas as formas em conjunto, sendo que ao clicar no botão, primeiro a função do **onclick** é executada e depois as que foram registradas no **addEventListener**, por ordem de registro.



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



#### URL's e Mapeamento de Rotas

O *Domain Driven Design* (**DDD**), ou projeto orientado ao domínio, foi consolidado no livro de mesmo nome, escrito por Eric Evans em 2003 [Evans, E., 2003]. O DDD não é um padrão, arquitetura ou tecnologia, é um conjunto de boas práticas e estratégias para lidar com a alta complexidade de aplicações em termos de negócio. Ele está baseado em três grandes pilares: linguagem ubíqua, delimitação de contextos e mapeamento de contextos.



**Modularização no Flask- Blueprints**

Exemplo:  Temos três domínios nesse exemplo: o catálogo de cursos, que é o domínio principal da aplicação, motivo da sua criação; o sistema de usuários, um domínio auxiliar na utilização do sistema, para garantir o acesso correto de pessoas no cadastro dos cursos; e a área administrativa, domínio principal para o cadastro tanto de usuários quanto para administradores.

**1- Primeiro módulo: Aplicação** 

- A pasta aplicação terá um arquivo **__init__.py** e terá o flask importado

```
from flask import Flask
from admin import admin_bp
from catalogo import catalogo_bp


app = Flask('aplicacao')
app.config.from_object('aplicacao.config.Configuracao')

app.register_blueprint(catalogo_bp)
app.register_blueprint(admin_bp, url_prefix='/admin')
```

- Crie um pasta chamada config.py, lá vamos possibilitar o export da Aplicação. O debug = true fará com que a aplicação reinicie em qualquer alteração salva.

```
class Configuracao(object):
    DEBUG = True
```



**2- Segundo módulo: Catálogo**

Os Blueprints funcionam como pequenas aplicações Flask dentro de uma maior. Um módulo criado como Blueprint além de separar as funcionalidades em áreas, pode ser exportado para uso em outra aplicação Flask, ampliando sua capacidade de reaproveitamento de código.

- init.py
  - 'catalogo' : nome do módulo
  - __name__: nome a ser usado na importação, indicando o uso do nome atual do módulo
  -  template_folder: indicando qual diretório estará a pasta do html

obs: Por padrão, as variáveis ficam com o nome do módulo sufixado por _bp.

```
from flask import Blueprint

catalogo_bp = Blueprint(
    'catalogo',
    __name__,
    template_folder='templates'
)

from . import controles
```



**3 - Terceiro módulo: Área Administrativa**

A diferença estará no registro do Blueprint na aplicação. Como já temos um Bp principal (catalogo), precisamos diferenciar as URLs para que o Flask não confunda para onde vai cada requisição. O mais comum é que módulos diferentes da principal possuam um caminho de prefixo, ou **base path**. No caso do admin, queremos que todos os seus controles fiquem com o prefixo /admin na URL. 

```
app.register_blueprint(catalogo_bp)
app.register_blueprint(admin_bp, url_prefix='/admin')
```

**Parametrização de Rotas**

A ideia dos Path Parameter é criar regiões na parte do caminho (path) da URL que virem parâmetros de entrada nos nossos controles. O **slug** é a última parte da URL (como se fosse o recurso), identificando o conteúdo que será mostrado, usando um texto amigável para URLs (tudo em minúsculas, sem espaços e acentos). Por exemplo,  o curso Desenvolvimento Web terá a URL **/curso/desenvolvimento-web**, onde o **/curso** é apenas o prefixo indicando a categoria do que será mostrado e **/desenvolvimento-web** é o nome do curso de uma maneira amigável para a URL (novamente, tudo minúsculo e o hífen no lugar do espaço), ou seja, o **slug** do curso.

```
@catalogo_bp.route('/curso/<slug>')
def curso(slug):
    return render_template(
        'curso.html',
        curso=obter_curso(slug)
    )
```

Por padrão esses parâmetros são interpretados como Strings, mas se quisermos tipar de outra maneira, podemos colocar o tipo na frente do nome, separado por dois pontos:

**<int:param>:** para inteiros positivos.

**<float:param>:** para decimais positivos.

**<path:param>:** igual a string, mas aceitas barras no meio.

**<uuid:param>:** aceita objetos do tipo UUID.

Independente do tipo, para cada **PathParameter** definido na rota, a função do controle receberá o parâmetro de mesmo nome como entrada da função, então a rota **'/curso/<slug>'** precisa estar com a função definida como **def curso(slug)**. Já uma rota '/**blog/<int:ano>/<int:mes>/<int:dia>/<slug>'** teria uma função com a seguinte assinatura: **def blog_post(ano, mes, dia, slug)**.



**Controle de Sessão: Autenticação e Autorização**

![img](https://lh4.googleusercontent.com/mMWX8qxGGa6CY5IFPIl4a9uTS8AJIyQuQ2a1YGg6waJpog_Ri-LJ_adr_R7nhd09l3v2jwuoQWhwPMx4UB62TvcjILqaXM0u3pmxnwG3TRXWgCWHvGKMD9eDn2-JyXebtmzrpKEB)