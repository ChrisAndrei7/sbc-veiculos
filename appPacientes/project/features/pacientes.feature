Feature: Gerenciamento de pacientes

  Scenario: Adicionar um novo Paciente
    Given que eu tenho os detalhes do Paciente
    When eu faço o cadastro de um Paciente
    Then eu devo receber uma resposta com o código de status 200

  Scenario: Consultar um Paciente
    When eu faço a consulta dos pacientes cadastros
    Then eu devo receber uma resposta com o código de status 200

  Scenario: Editar um Paciente existente
    Given que eu tenho os detalhes atualizados do Paciente
    When eu faço uma atualização de um Paciente
    Then eu devo receber uma resposta com o código de status 200

  Scenario: Consultar um Paciente pelo CPF
    When eu faço a consulta de um Paciente pelo CPF
    Then eu devo receber uma resposta com o código de status 200