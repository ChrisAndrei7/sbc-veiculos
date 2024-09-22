import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from entities.pacientes.pacientesmodels import Paciente
from infrastructure.presenters.pacientesserializers import PacienteSerializer


@api_view(['GET'])
def getData(request):
    pacientes = Paciente.objects.all()
    serializer = PacienteSerializer(pacientes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getPaciente(request, pk):
    pacientes = Paciente.objects.get(id=pk)
    serializer = PacienteSerializer(pacientes, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getPacienteCPF(request, cpf):
    pacientes = Paciente.objects.get(cpf=cpf)
    serializer = PacienteSerializer(pacientes, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def addPaciente(request):
    serializer = PacienteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def updatePaciente(request, pk):
    paciente = Paciente.objects.get(id=pk)
    serializer = PacienteSerializer(instance=paciente, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deletePaciente(request, pk):
    paciente = Paciente.objects.get(id=pk)
    paciente.delete()
    return Response('Paciente deletado com sucesso!')


@api_view(['GET'])
def getMedicosDisponiveis(request, data, horario):
    # Consultando MS de médicos para obter a lista de médicos cadastrados
    medicos_response = requests.get('http://medicos:8004/medicos')

    if medicos_response.status_code != 200:
        return Response({"erro": "Erro ao conectar com o serviço de médicos"}, status=500)

    try:
        medicos = medicos_response.json()
    except ValueError:
        return Response({"erro": "Erro ao processar a resposta de médicos"}, status=500)

    # Consultando MS de agendamentos para verificar médicos ocupados na data e horário
    agendamentos_response = requests.get(f'http://agendamentos:8002/agendamentos/readdata/{data}')

    if agendamentos_response.status_code == 500:
        # Se houver erro no serviço de agendamentos, retorna todos os médicos
        return Response({'medicos_disponiveis': [medico['name'] for medico in medicos]})

    try:
        agendamentos = agendamentos_response.json()
    except ValueError:
        return Response({"erro": "Erro ao processar a resposta de agendamentos"}, status=500)

    # Verificar se "agendamentos" é uma lista ou dicionário
    if isinstance(agendamentos, dict):  # Caso seja um único agendamento (dicionário)
        medicos_ocupados = {agendamentos['nomemedico']}
    elif isinstance(agendamentos, list):  # Caso seja uma lista de agendamentos
        medicos_ocupados = {agendamento['nomemedico'] for agendamento in agendamentos}
    else:
        return Response({"erro": "Formato inválido de resposta de agendamentos"}, status=500)

    # Filtrar médicos disponíveis
    medicos_disponiveis = [medico['name'] for medico in medicos if medico['name'] not in medicos_ocupados]

    return Response({'medicos_disponiveis': medicos_disponiveis})
