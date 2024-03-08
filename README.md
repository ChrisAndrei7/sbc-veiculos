<h1 align="center"> Sistema de pedidos para lanches </h1>
Bem-vindo ao Sistema de Pedidos para Lanchonete! Este projeto foi desenvolvido como parte do Tech Challenge para fase 1.	

> :construction: Projeto em construção :construction:
<br/>

# :computer: Endpoint base da aplicação
http://localhost:31000/
<br/>
<br/>


# :hammer: Subida da aplicação

1. Entre no diretório do projeto: `cd app`
2. Efetue a criação/subida do banco de dados: `docker-compose up -d db`
3. Efetue a criação da aplicação: `docker compose build`
4. Efetue a subida da aplicação: `docker compose up`
<br/>

# :warning: DDD
O arquivo referente ao Domain driven design encontra-se em anexo, com título `DDD Fase 1 - Tech Challenge`, dentro da pasta `app > documentos`. Deixamos 2 opções para visualização, imagens para visualizar estaticamente, e as versões .eng para visualizar como editável.
Criamos pelo site Egon.io, por favor, utilizar a última versão, link abaixo:
https://egon.io/app-latest/

Foi separado em 2 partes conforme solicitado, a primeira simulando a interação entre o cliente e o sistema, e a segunda detém a maior parte focada na interação entre 
o atendente e a cozinha, atualizando o status do pedido e sendo enviado para o monitor.
<br/>
<br/>

# :arrow_forward: Uso 
Abaixo, fluxo principal com processo e endpoint. Para maior detalhe dos campos, temos em anexo o arquivo do Postman com a collection estruturando todos as APIs com descrição e valores a serem informados no json.

1 - Criar o usuário: http://localhost:31000/users/create

2 - Consultar usuário criado: http://localhost:31000/users

3 - Criar o produto: http://localhost:31000/produtos/create

4 - Consultar produto criado: http://localhost:31000/produtos

5 - Criar o pedido: http://localhost:31000/pedidos/create

6 - Consultar pedido criado: http://localhost:31000/pedidos
<br/>
<br/>

# :warning: Collection
Disponibilizamos uma collection do postman para ajudar na utilização, contendo todas as APIs da aplicação e com os campos necessários para preenchimento. 

Arquivo `TechChallengeApp.postman_collection` em anexo dentro da pasta `app > documentos`.
