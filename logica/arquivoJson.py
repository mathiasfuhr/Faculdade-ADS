import json

pessoas = [
    {'nome': 'Mathias', 'telefone': '(55) 997282539', 'endereco': 'Jardim das Acacias'},
    {'nome': 'Josiane', 'telefone': '(55) 995239222', 'endereco': 'Jardim das Flores'},
    {'nome': 'Megui', 'telefone': '(55) 991725547', 'endereco': 'Jardim das Morangas'}
]

with open('pessoas.json', 'w') as arquivo:
    json.dump(pessoas, arquivo, indent=4)