from behave import given, when, then
import requests

BASE_URL = 'http://localhost:8003'

@given('que eu tenho os detalhes do Paciente')
def step_impl(context):
    context.paciente_data = {
        'name': 'Paciente a',
        'cpf': '12871569088',
        'email': 'ba@ba.com.br',
        'senha': 'pass!paciente01@',
    }

@given('que eu tenho os detalhes atualizados do Paciente')
def step_impl(context):
    context.updated_paciente_data = {
        'name': 'Paciente aZ',
        'cpf': '12871569088',
        'email': 'baZ@baZ.com.br',
        'senha': 'pass!paciente01@',
    }

@when('eu faço o cadastro de um Paciente')
def step_impl(context):
    context.response = requests.post(f"{BASE_URL}/pacientes/create", json=context.paciente_data)

@when('eu faço uma atualização de um Paciente')
def step_impl(context):
    context.response = requests.put(f"{BASE_URL}/pacientes/update/1", json=context.updated_paciente_data)

@when('eu faço a consulta dos pacientes cadastros')
def step_impl(context):
    context.response = requests.get(f"{BASE_URL}/pacientes")

@when('eu faço a consulta de um Paciente pelo CPF')
def step_impl(context):
    context.response = requests.get(f"{BASE_URL}/pacientes/readcpf/12871569088")

@when('eu faço a exclusão de um Paciente')
def step_impl(context):
    context.response = requests.delete(f"{BASE_URL}/pacientes/delete/1")

@then('eu devo receber uma resposta com o código de status 201')
def step_impl(context):
    assert context.response.status_code == 201

@then('eu devo receber uma resposta com o código de status 200')
def step_impl(context):
    assert context.response.status_code == 200
