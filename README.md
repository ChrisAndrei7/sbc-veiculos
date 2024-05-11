<h1 align="center"> TCFoodSystem - Sistema de pedidos para lanches </h1>
Bem-vindo ao Sistema de Pedidos para Lanchonete! Este projeto está em desenvolvimento como atividade do Tech Challenge para a FIAP, curso Software Architecture.	
<br/>
:construction: Projeto em construção :construction:
<br/>

# :computer: Endpoint base da aplicação
http://localhost:31000/
<br/>
<br/>

# :hammer: Subida da aplicação
### Subida completa da aplicação, seguir os 2 procedimentos(`docker e kubernetes`) apenas se for a primeira vez, a subida docker é necessária apenas para carregar imagem da aplicação django. Caso já tenha efetuado a subida em outro momento, seguir passos apenas da segunda parte(Kubernetes).
<br/>

#### - Subida pelo docker:
1. Entre no diretório do projeto: `cd app`
2. Efetue a criação/subida do banco de dados: `docker compose up -d db`
3. Efetue a criação da aplicação: `docker compose build`                                                                                                                                                                                                                                                     
      <b>Nota Importante:
      Ao realizar a primeira inicialização, ocasionalmente pode ocorrer o erro "No installed app with label 'pagamentos'". Como solução temporária, sugerimos a seguinte abordagem: caso o erro mencionado ocorra na primeira subida, modifique o arquivo "django.sh" na linha       3, substituindo "pagamentos" por "pedidos" e efetue novamente o passo 3 antes de seguir para o passo 4.</b>
4. Efetue a subida da aplicação: `docker compose up`
<br/>

<b>============ Parar aplicação do docker ============</b>

#### - Subida kubernetes(Após desligar docker):
1. Subir a secret: `kubectl apply -f app/kubernetes/secret.yml`
2. Subir o configmap: `kubectl create -f app/kubernetes/config_map.yml`
3. Subir o deployment do banco de dados: `kubectl apply -f app/kubernetes/db_deployment.yml`
4. Subir o service do banco de dados: `kubectl apply -f app/kubernetes/db_service.yml`
5. Subir o deployment da aplicação: `kubectl apply -f app/kubernetes/app_deployment.yml`
6. Subir o service da aplicação: `kubectl apply -f app/kubernetes/app_service.yml`
7. Subir as métricas para escalabilidade: `kubectl apply -f app/kubernetes/metrics.yml`
8. Subir HPA para escalabilidade:`kubectl apply -f app/kubernetes/hpa.yml`
<br/>

<b>Video explicativo: https://www.youtube.com/watch?v=Dq_JQejMNWk
<br/>
  
# :arrow_forward: Uso 
Abaixo, fluxo principal com processo e endpoint. Para maior detalhe dos campos, temos em anexo o arquivo do Postman com a collection estruturando todos as APIs com descrição e valores a serem informados no json.

1 - Criar o usuário: http://localhost:31000/users/create

2 - Consultar usuário criado: http://localhost:31000/users

3 - Criar o produto: http://localhost:31000/produtos/create

4 - Consultar produto criado: http://localhost:31000/produtos

5 - Criar o pedido: http://localhost:31000/pedidos/create

6 - Consultar pedido criado: http://localhost:31000/pedidos

7 - Criar o pagamento: http://localhost:31000/pagamentos/create

8 - Consultar pagamento criado: http://localhost:31000/pagamentos/
<br/>
<br/>

# :warning: Documentação
Os documentos se encontram dentro da pasta `app > documentos`.

# DDD
O arquivo referente ao Domain driven design encontra-se em anexo, com título `DDD Fase 1 - Tech Challenge`, dentro da pasta `app > documentos`. Deixamos 2 opções para visualização, imagens para visualizar estaticamente, e as versões .eng para visualizar como editável.
Criamos pelo site Egon.io, por favor, utilizar a última versão, link abaixo:
https://egon.io/app-latest/

Foi separado em 2 partes conforme solicitado, a primeira simulando a interação entre o cliente e o sistema, e a segunda detém a maior parte focada na interação entre 
o atendente e a cozinha, atualizando o status do pedido e sendo enviado para o monitor.

# Collection
Disponibilizamos uma collection do postman para ajudar na utilização, contendo todas as APIs da aplicação e com os campos necessários para preenchimento. 

Arquivo `TechChallengeApp.postman_collection` em anexo dentro da pasta `app > documentos`.

# Desenhos arquitetura
Foram disponibilizados também os desenhos de arquitetura, `requisitos de infraestrutura` e `requisitos do negocio`. Ambos estão com seus respectivos títulos no formato PNG dentro da pasta `app > documentos`.
<br/>
<br/>

# :hammer: Parar aplicação
Para efetuar a parada total da aplicação, e deletar todos os inclusos na subida, seguir passos abaixo:

1. `kubectl delete deployment postgres-deployment`
2. `kubectl delete deployment django-postgre-deploy`
3. `kubectl delete service django-service`
4. `kubectl delete service db`
5. `kubectl delete ConfigMap app-variables`
6. `kubectl delete secret postgres-credentials`
7. `kubectl delete persistentvolumeclaim postgres-pvc`
8. `kubectl delete -f app/kubernetes/metrics.yml`
9. `kubectl delete hpa tcfoodsystem-hpa`
