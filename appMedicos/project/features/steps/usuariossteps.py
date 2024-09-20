from behave import given, when, then
import requests

BASE_URL = 'http://localhost:8004'

@given('que eu tenho os detalhes do Medico')
def step_impl(context):
    context.medico_data = {
        'name': 'Medico a',
        'cpf': '74964674053',
        'crm': '398877',
        'email': 'ba@ba.com.br',
        'senha': 'pass!medico01@',
    }

@given('que eu tenho os detalhes atualizados do Medico')
def step_impl(context):
    context.updated_medico_data = {
        'name': 'Medico aZ',
        'cpf': '74964674053',
        'crm': '398877',
        'email': 'baZ@baZ.com.br',
        'senha': 'pass!medico01@',
    }

@when('eu faço o cadastro de um Medico')
def step_impl(context):
    context.response = requests.post(f"{BASE_URL}/medicos/create", json=context.medico_data)

@when('eu faço uma atualização de um Medico')
def step_impl(context):
    context.response = requests.put(f"{BASE_URL}/medicos/update/1", json=context.updated_medico_data)

@when('eu faço a consulta dos medicos cadastros')
def step_impl(context):
    context.response = requests.get(f"{BASE_URL}/medicos")

@when('eu faço a consulta de um Medico pelo CPF')
def step_impl(context):
    context.response = requests.get(f"{BASE_URL}/medicos/readcpf/74964674053")

@when('eu faço a exclusão de um Medico')
def step_impl(context):
    context.response = requests.delete(f"{BASE_URL}/medicos/delete/1")

@then('eu devo receber uma resposta com o código de status 201')
def step_impl(context):
    assert context.response.status_code == 201

@then('eu devo receber uma resposta com o código de status 200')
def step_impl(context):
    assert context.response.status_code == 200
