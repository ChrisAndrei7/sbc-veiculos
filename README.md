<h1 align="center"> H&MSystem - Sistema para agendamentos de consultas médicas </h1>
Bem-vindo ao Sistema para agendamento de consultas da Health&Med! Este projeto está em desenvolvimento como atividade do hackaton para a FIAP, curso Software Architecture.	
<br/>
<b>Neste repositório, temos o microsserviço de cadastro dos médicos</b>
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
1. Entre no diretório do projeto: `cd appMedicos`
2. Efetue a criação/subida do banco de dados: `docker compose up -d dbMedicos`
3. Efetue a criação da aplicação: `docker compose build`                                                                                                                                                                                                                                                     
      <b>Nota Importante:
      Ao realizar a primeira inicialização, ocasionalmente pode ocorrer o erro "No installed app with label 'medicos'". Como solução temporária, sugerimos a seguinte abordagem: caso o erro mencionado ocorra na primeira subida, modifique o arquivo "django.sh" na linha       3, substituindo "medicos" por "application" e efetue novamente o passo 3 antes de seguir para o passo 4.</b>
4. Efetue a subida da aplicação: `docker compose up`
<br/>
  
# :arrow_forward: Uso 
Abaixo, fluxos principais com processo e endpoint desse microsserviço. Para maior detalhe dos campos, temos no projeto(Na pasta appMedicos/Documentos) o arquivo do Postman com a collection estruturando todos as APIs com descrição e valores a serem informados no json.

1 - Criar o cadastro de um médico: http://localhost:8004/medicos/create

2 - Consultar médicos cadastrados: http://localhost:8004/medicos/

3 - Atualizar cadastro de um médico: http://localhost:8004/medicos/update/{id_do_medico}

4 - Deletar o cadastro de um médico: http://localhost:8004/medicos/delete/{id_do_medico}

# :page_with_curl: Collection
Disponibilizamos uma collection do postman para ajudar na utilização, contendo todas as APIs deste microserviço e com os campos necessários para preenchimento, <b>localizado na pasta appMedicos/Documentos com nome "hk-medicos.postman_collection".</b>

# :dancer: Padrão Saga - Coreografia
:construction: Em construção :construction:

# :lock: Relatório RIPD
Relatório RIPD gerado se encontra junto com todos os outros documentos do projeto dentro do projeto, na pasta pasta **appMedicos/Documentos**, com nome **H&MSystem - RIPD**.

# :test_tube: Testes
Para executar os testes, localizados dentro da pasta "feature", deve ser processado o comando behave abaixo após aplicação estar no ar.
OBS: BDD está dentro do arquivo "medicos.feature"

#### behave appMedicos/project/features/medicos.feature

# Evidência dos testes:

![image](https://github.com/user-attachments/assets/6a44a78b-61cb-4bdf-b416-a7027ff8ba5c)
