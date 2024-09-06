<h1 align="center"> TCFoodSystem - Sistema de pedidos para lanches </h1>
Bem-vindo ao Sistema de Pedidos para Lanchonete! Este projeto está em desenvolvimento como atividade do Tech Challenge para a FIAP, curso Software Architecture.	
<br/>
<b>Neste repositório, temos o microsserviço de usuarios</b>
<br/>
:construction: Projeto em construção :construction:
<br/>

# :computer: Endpoint base da aplicação
http://localhost:8004/
<br/>
<br/>

# :hammer: Subida da aplicação
### Subida completa da aplicação via docker:

#### - Subida no docker:
1. Entre no diretório do projeto: `cd appUsuarios`
2. Efetue a criação/subida do banco de dados: `docker compose up -d dbUsuarios`
3. Efetue a criação da aplicação: `docker compose build`                                                                                                                                                                                                                                                     
      <b>Nota Importante:
      Ao realizar a primeira inicialização, ocasionalmente pode ocorrer o erro "No installed app with label 'pagamentos'". Como solução temporária, sugerimos a seguinte abordagem: caso o erro mencionado ocorra na primeira subida, modifique o arquivo "django.sh" na linha       3, substituindo "usuarios" por "application" e efetue novamente o passo 3 antes de seguir para o passo 4.</b>
4. Efetue a subida da aplicação: `docker compose up`
<br/>
  
# :arrow_forward: Uso 
Abaixo, fluxos principais com processo e endpoint desse microsserviço. Para maior detalhe dos campos, temos no projeto(Na pasta appUsuarios/Documentos) o arquivo do Postman com a collection estruturando todos as APIs com descrição e valores a serem informados no json.

1 - Criar o pagamento: http://localhost:8004/usuarios/create

2 - Consultar pagamentos: http://localhost:8004/usuarios/

3 - Atualizar pagamento: http://localhost:8004/usuarios/update/{id_do_usuario}

4 - Deletar pagamento: http://localhost:8004/usuarios/delete/{id_do_usuario}

# :page_with_curl: Collection
Disponibilizamos uma collection do postman para ajudar na utilização, contendo todas as APIs deste microserviço e com os campos necessários para preenchimento. 

# :dancer: Padrão Saga - Coreografia
### Justificativa da Escolha do Padrão Saga - Coreografia
Optamos pelo **padrão Saga com coreografia** devido à sua capacidade de promover **descentralização** e **autonomia** entre microserviços. Nesse padrão, cada serviço reage a eventos relevantes de forma assíncrona, evitando a necessidade de um orquestrador central. Isso proporciona **menor acoplamento**, melhora a **escalabilidade** e facilita a **evolução e manutenção** do sistema, já que cada serviço pode ser desenvolvido e atualizado de forma independente, sem impactar os demais. 

**Foram desenvolvidas 3 filas:**

      1. pedido_criado
      
      2. pagamento_pendente
      
      3. pagamento_confirmado

Para acompanhar filas, acessar o rabbitMQ com aplicação no ar:

**Link:** http://localhost:15672

**User:** guest

**Password:** guest

Abaixo, demonstrando arquitetura coreografada:

![Arquitetura_Saga_Coreografia drawio](https://github.com/user-attachments/assets/7981e294-3f45-4d4d-b2bd-ed785d0b1fbd)

# :test_tube: Testes
Para executar os testes, localizados dentro da pasta "feature", deve ser processado o comando behave abaixo após aplicação estar no ar.
OBS: BDD está dentro do arquivo "usuarios.feature"

#### behave appUsuarios/project/features/usuarios.feature

# Evidência dos testes:

![image](https://github.com/user-attachments/assets/9cd1eabb-3628-4f2c-aa83-425e035d4843)
