Feature: Gerenciamento de usuarios

  Scenario: Adicionar um novo usuario
    Given que eu tenho os detalhes do usuario
    When eu faço o cadastro de um usuario
    Then eu devo receber uma resposta com o código de status 200

  Scenario: Consultar um usuario
    When eu faço a consulta dos usuarios cadastros
    Then eu devo receber uma resposta com o código de status 200

  Scenario: Editar um usuario existente
    Given que eu tenho os detalhes atualizados do usuario
    When eu faço uma atualização de um usuario
    Then eu devo receber uma resposta com o código de status 200

  Scenario: Consultar um usuario pelo CPF
    When eu faço a consulta de um usuario pelo CPF
    Then eu devo receber uma resposta com o código de status 200