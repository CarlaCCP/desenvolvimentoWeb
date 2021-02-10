

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

##### Unidade  1: 

- Protocolo HTTP 

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