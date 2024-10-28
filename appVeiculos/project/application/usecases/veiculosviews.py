import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from entities.veiculos.veiculosmodels import Veiculo
from infrastructure.presenters.veiculosserializers import VeiculoSerializer


@api_view(['GET'])
def getData(request):
    veiculos = Veiculo.objects.all()
    serializer = VeiculoSerializer(veiculos, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getVeiculo(request, pk):
    veiculos = Veiculo.objects.get(id=pk)
    serializer = VeiculoSerializer(veiculos, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getVeiculoPlaca(request, placa):
    veiculos = Veiculo.objects.get(placa=placa)
    serializer = VeiculoSerializer(veiculos, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def addVeiculo(request):
    serializer = VeiculoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def updateVeiculo(request, pk):
    veiculo = Veiculo.objects.get(id=pk)
    serializer = VeiculoSerializer(instance=veiculo, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteVeiculo(request, pk):
    veiculo = Veiculo.objects.get(id=pk)
    veiculo.delete()
    return Response('Veiculo deletado com sucesso!')
