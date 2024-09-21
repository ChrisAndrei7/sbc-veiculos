#from django.shortcuts import render

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

