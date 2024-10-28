Feature: Gerenciamento de veiculos

  Scenario: Adicionar um novo Veiculo
    Given que eu tenho os detalhes do Veiculo
    When eu faço o cadastro de um Veiculo
    Then eu devo receber uma resposta com o código de status 200

  Scenario: Consultar um Veiculo
    When eu faço a consulta dos veiculos cadastros
    Then eu devo receber uma resposta com o código de status 200

  Scenario: Editar um Veiculo existente
    Given que eu tenho os detalhes atualizados do Veiculo
    When eu faço uma atualização de um Veiculo
    Then eu devo receber uma resposta com o código de status 200

  Scenario: Consultar um Veiculo pela placa
    When eu faço a consulta de um Veiculo pela placa
    Then eu devo receber uma resposta com o código de status 200