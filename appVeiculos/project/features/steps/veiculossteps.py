from behave import given, when, then
import requests

BASE_URL = 'http://localhost:8003'

@given('que eu tenho os detalhes do Veiculo')
def step_impl(context):
    context.veiculo_data = {
        'veiculo': 'Corsa',
        'placa': 'ABC-1A34',
        'marca': 'Chevrolet',
        'modelo': 'maxx 1.4 8v econoflex 4p',
        'ano': '2009',
        'cor': 'Preto',
        'valor': '19.900',
    }

@given('que eu tenho os detalhes atualizados do Veiculo')
def step_impl(context):
    context.updated_veiculo_data = {
        'veiculo': 'Corsa',
        'placa': 'ABC-1A34',
        'marca': 'Chevrolet',
        'modelo': 'maxx 1.4 8v econoflex 4p',
        'ano': '2009',
        'cor': 'Preto',
        'valor': '18.500',
    }

@when('eu faço o cadastro de um Veiculo')
def step_impl(context):
    context.response = requests.post(f"{BASE_URL}/veiculos/create", json=context.veiculo_data)

@when('eu faço uma atualização de um Veiculo')
def step_impl(context):
    context.response = requests.put(f"{BASE_URL}/veiculos/update/1", json=context.updated_veiculo_data)

@when('eu faço a consulta dos veiculos cadastros')
def step_impl(context):
    context.response = requests.get(f"{BASE_URL}/veiculos")

@when('eu faço a consulta de um Veiculo pela placa')
def step_impl(context):
    context.response = requests.get(f"{BASE_URL}/veiculos/readplaca/ABC-1A34")

@when('eu faço a exclusão de um Veiculo')
def step_impl(context):
    context.response = requests.delete(f"{BASE_URL}/veiculos/delete/1")

@then('eu devo receber uma resposta com o código de status 201')
def step_impl(context):
    assert context.response.status_code == 201

@then('eu devo receber uma resposta com o código de status 200')
def step_impl(context):
    assert context.response.status_code == 200
