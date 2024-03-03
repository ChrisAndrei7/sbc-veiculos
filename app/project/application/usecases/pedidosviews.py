import sys
sys.path.append("../../entities/pedidos")
from rest_framework.response import Response
from rest_framework.decorators import api_view
from entities.pedidos.pedidosmodels import Pedido
from entities.produtos.produtosmodels import Produto
from entities.usuarios.usuariosmodels import User
from infrastructure.presenters.pedidosserializers import PedidoSerializer
from django.db.models import Case, When, Value, IntegerField
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def getData(request):
    pedidos = Pedido.objects.all()
    # Defina as regras de ordenação
    status_order = Case(
        When(status='PRONTO', then=Value(1)),
        When(status='EM_PREPARACAO', then=Value(2)),
        When(status='RECEBIDO', then=Value(3)),
        output_field=IntegerField()
    )
    # Consulta para obter os pedidos ordenados conforme as regras
    pedidos = Pedido.objects.exclude(status='FINALIZADO').order_by(status_order)

    serializer = PedidoSerializer(pedidos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getPedido(request, pk):
    pedidos = Pedido.objects.get(id=pk)
    serializer = PedidoSerializer(pedidos, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getPedidoPorStatus(request, pk):
    pedidos = Pedido.objects.get(status=pk)
    serializer = PedidoSerializer(pedidos, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addPedido(request):
    # Validação de dados antes de criar o Pedido
    produto_id = request.data.get('produto_id')
    cliente_id = request.data.get('cliente_id')

    # Verifica se os IDs de produto e cliente existem no banco de dados
    if not Produto.objects.filter(pk=produto_id).exists():
        return Response({'error': 'Produto não encontrado'}, status=status.HTTP_400_BAD_REQUEST)

    if not User.objects.filter(pk=cliente_id).exists():
        return Response({'error': 'Cliente não encontrado'}, status=status.HTTP_400_BAD_REQUEST)

        # Validação de dados
    if not produto_id or not cliente_id:
        return Response({'error': 'IDs de produto e cliente são obrigatórios'}, status=status.HTTP_400_BAD_REQUEST)

    # Prossegue com a criação do pedido se os IDs existirem
    serializer = PedidoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updatePedido(request, pk):
    pedido = Pedido.objects.get(id=pk)
    serializer = PedidoSerializer(instance=pedido, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deletePedido(request, pk):
    pedido = Pedido.objects.get(id=pk)
    pedido.delete()
    return Response('Produto deletado com sucesso!')