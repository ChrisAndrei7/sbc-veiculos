Feature: Gerenciamento de medicos

  Scenario: Adicionar um novo Medico
    Given que eu tenho os detalhes do Medico
    When eu faço o cadastro de um Medico
    Then eu devo receber uma resposta com o código de status 200

  Scenario: Consultar um Medico
    When eu faço a consulta dos Medicos cadastros
    Then eu devo receber uma resposta com o código de status 200

  Scenario: Editar um Medico existente
    Given que eu tenho os detalhes atualizados do Medico
    When eu faço uma atualização de um Medico
    Then eu devo receber uma resposta com o código de status 200

  Scenario: Consultar um Medico pelo CPF
    When eu faço a consulta de um Medico pelo CPF
    Then eu devo receber uma resposta com o código de status 200