#from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from entities.medicos.medicosmodels import Medico
from infrastructure.presenters.medicosserializers import MedicoSerializer

@api_view(['GET'])
def getData(request):
    medicos = Medico.objects.all()
    serializer = MedicoSerializer(medicos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getMedico(request, pk):
    medicos = Medico.objects.get(id=pk)
    serializer = MedicoSerializer(medicos, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getMedicoCPF(request, cpf):
    medicos = Medico.objects.get(cpf=cpf)
    serializer = MedicoSerializer(medicos, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addMedico(request):
    serializer = MedicoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PUT'])
def updateMedico(request, pk):
    medico = Medico.objects.get(id=pk)
    serializer = MedicoSerializer(instance=medico, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteMedico(request, pk):
    medico = Medico.objects.get(id=pk)
    medico.delete()
    return Response('Médico deletado com sucesso!')

