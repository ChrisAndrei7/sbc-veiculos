import sys

from rest_framework import status

sys.path.append("../../entities/pagamentos")
from rest_framework.response import Response
from rest_framework.decorators import api_view
from entities.pagamentos.pagamentosmodels import Pagamento
from infrastructure.presenters.pagamentosserializers import PagamentoSerializer
from entities.pedidos.pedidosmodels import Pedido

# Create your views here.
@api_view(['GET'])
def getData(request):
    pagamentos = Pagamento.objects.all()
    serializer = PagamentoSerializer(pagamentos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getPagamento(request, pk):
    pagamentos = Pagamento.objects.get(id=pk)
    serializer = PagamentoSerializer(pagamentos, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getPagamentoPorStatus(request, pk):
    pagamentos = Pagamento.objects.get(status=pk)
    serializer = PagamentoSerializer(pagamentos, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addPagamento(request):
    # Validação de dados antes de criar o Pagamento
    pedido_id = request.data.get('pedido_id')

    # Verifica se o ID do pedido existe no banco de dados
    if not Pedido.objects.filter(pk=pedido_id).exists():
        return Response({'error': 'Pedido não encontrado'}, status=status.HTTP_400_BAD_REQUEST)

    # Prossegue com a criação do pagamento se o ID existir
    serializer = PagamentoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
@api_view(['PUT'])
def updatePagamento(request, pk):
    pagamentos = Pagamento.objects.get(id=pk)
    serializer = PagamentoSerializer(instance=pagamentos, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deletePagamento(request, pk):
    pagamentos = Pagamento.objects.get(id=pk)
    pagamentos.delete()
    return Response('Pagamento deletado com sucesso!')