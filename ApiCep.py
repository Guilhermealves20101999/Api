import requests
import os

#limpar o terminal

os.system("clear") 

# Api Cep
cep = input("Digite O CEP: ")

# Variavel R para usar a Biblioteca Request
r = requests.get("https://viacep.com.br/ws/{}/json/".format(cep))

# Puxar os Dados da Api
data = r.json()

# Imprimir dados
print('Dados a Baixo: ')
print()
print('cep: {}'.format(data['cep']))
print('logradouro: {}'.format(data['logradouro']))
print('complemento: {}'.format(data['complemento']))
print('Bairro: {}'.format(data['bairro']))
print('localidade: {}'.format(data['localidade']))
print('UF: {}'.format(data['uf']))
print('IBGE: {}'.format(data['ibge']))
print('Gia:{}'.format(data['gia']))
print('DDD: {}'.format(data['ddd']))
print('siafi: {}'.format(data['siafi']))



