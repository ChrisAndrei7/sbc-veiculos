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

@api_view(['GET'])
def getVeiculosParaVenda(request):
    # Consultando MS de Veiculos
    veiculos_response = requests.get('http://veiculos:8003/veiculos')
    if veiculos_response.status_code != 200:
        return Response({"erro": "Erro ao conectar com o serviço de veículos"}, status=500)

    # Consultando MS de Sales
    sales_response = requests.get('http://sales:8002/sales')
    if sales_response.status_code != 200:
        return Response({"erro": "Erro ao conectar com o serviço de vendas"}, status=500)

    try:
        veiculos = veiculos_response.json()
        sales = sales_response.json()
    except ValueError:
        return Response({"erro": "Erro ao processar as respostas dos serviços"}, status=500)

    # Coletar as placas dos veículos vendidos
    placas_vendidas = {sale['placa'] for sale in sales}

    # Filtrar veículos disponíveis para venda e ordenar por valor
    veiculos_disponiveis = [
        {"veiculo": veiculo["veiculo"], "placa": veiculo["placa"], "valor": veiculo["valor"]}
        for veiculo in veiculos
        if veiculo["placa"] not in placas_vendidas
    ]
    veiculos_disponiveis.sort(key=lambda x: x["valor"])

    return Response({"veiculos_para_venda": veiculos_disponiveis})


@api_view(['GET'])
def getVeiculosvendidos(request):
    # Consultando MS de Veiculos
    veiculos_response = requests.get('http://veiculos:8003/veiculos')
    if veiculos_response.status_code != 200:
        return Response({"erro": "Erro ao conectar com o serviço de veículos"}, status=500)

    # Consultando MS de Sales
    sales_response = requests.get('http://sales:8002/sales')
    if sales_response.status_code != 200:
        return Response({"erro": "Erro ao conectar com o serviço de vendas"}, status=500)

    try:
        veiculos = veiculos_response.json()
        sales = sales_response.json()
    except ValueError:
        return Response({"erro": "Erro ao processar as respostas dos serviços"}, status=500)

    # Coletar as placas dos veículos vendidos
    placas_vendidas = {sale['placa'] for sale in sales}

    # Filtrar veículos vendidos e ordenar por valor
    veiculos_vendidos = [
        {"veiculo": veiculo["veiculo"], "placa": veiculo["placa"], "valor": veiculo["valor"]}
        for veiculo in veiculos
        if veiculo["placa"] in placas_vendidas
    ]
    veiculos_vendidos.sort(key=lambda x: x["valor"])

    return Response({"veiculos_vendidos": veiculos_vendidos})