import requests
import json

link = "https://webhook.site/c651d69f-46bb-4e29-8c94-9f40bb8b8d0d"

dicionario = {
    "nome": "candrei",
    "Valor": "10.50",
    "Parcelas": "2",
}

dicionario_ajustado = json.dumps(dicionario)
requests.post(link, data=dicionario_ajustado)