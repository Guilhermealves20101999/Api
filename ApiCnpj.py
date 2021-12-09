import requests
import os

import requests
import os

os.system('clear')

cnpj = input("Digite seu CNPJ: ")
r = requests.get('https://www.receitaws.com.br/v1/cnpj/{}'.format(cnpj))

data = r.json()

print('Dados:'
)
print('CNPJ: {}'.format(data['cnpj']))
print('Razão Social: {}'.format(data['nome']))
print('Nome Fantasia:{}'.format(data['fantasia']))
print('Data de Abertura: {}'.format(data['data_situacao']))
print('Telefone: {}'.format(data['telefone']))
print('Email: {}'.format(data['email']))
print('Endereço'
)
print('cep: {}'.format(data['cep']))
print('logradouro: {}'.format(data['logradouro']))
print('complemento: {}'.format(data['complemento']))
print('Numero: {}'.format(data['numero']))
print('Municipio: {}'.format(data['municipio']))

