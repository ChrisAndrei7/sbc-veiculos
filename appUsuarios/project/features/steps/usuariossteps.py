from behave import given, when, then
import requests

BASE_URL = 'http://localhost:8004'

@given('que eu tenho os detalhes do usuario')
def step_impl(context):
    context.user_data = {
        'name': 'usuario a',
        'email': 'ba@ba.com.br',
        'cpf': '9876543210',
    }

@given('que eu tenho os detalhes atualizados do usuario')
def step_impl(context):
    context.updated_user_data = {
        'name': 'usuario aZ',
        'email': 'baZ@baZ.com.br',
        'cpf': '7777777777',
    }

@when('eu faço o cadastro de um usuario')
def step_impl(context):
    context.response = requests.post(f"{BASE_URL}/users/create", json=context.user_data)

@when('eu faço uma atualização de um usuario')
def step_impl(context):
    context.response = requests.put(f"{BASE_URL}/users/update/1", json=context.updated_user_data)

@when('eu faço a consulta dos usuarios cadastros')
def step_impl(context):
    context.response = requests.get(f"{BASE_URL}/users")

@when('eu faço a consulta de um usuario pelo CPF')
def step_impl(context):
    context.response = requests.get(f"{BASE_URL}/users/readcpf/7777777777")

@when('eu faço a exclusão de um usuario')
def step_impl(context):
    context.response = requests.delete(f"{BASE_URL}/users/delete/1")

@then('eu devo receber uma resposta com o código de status 201')
def step_impl(context):
    assert context.response.status_code == 201

@then('eu devo receber uma resposta com o código de status 200')
def step_impl(context):
    assert context.response.status_code == 200
