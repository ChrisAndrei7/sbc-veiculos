from rest_framework.response import Response
from rest_framework.decorators import api_view
from entities.produtos.produtosmodels import Produto
from infrastructure.presenters.produtosserializers import ProdutoSerializer

# Create your views here.
@api_view(['GET'])
def getData(request):
    produtos = Produto.objects.all()
    serializer = ProdutoSerializer(produtos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProduto(request, pk):
    produtos = Produto.objects.get(id=pk)
    serializer = ProdutoSerializer(produtos, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getProdutoCategoria(request, cat):
    produtos = Produto.objects.get(categoria=cat)
    serializer = ProdutoSerializer(produtos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addProduto(request):
    serializer = ProdutoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PUT'])
def updateProduto(request, pk):
    produto = Produto.objects.get(id=pk)
    serializer = ProdutoSerializer(instance=produto, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteProduto(request, pk):
    produto = Produto.objects.get(id=pk)
    produto.delete()
    return Response('Produto deletado com sucesso!')