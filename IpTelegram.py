import os
import subprocess
import requests
import json

# Defina a chave de API do Google Maps
API_KEY = 'sua_chave_de_api_aqui'

# Função para obter o endereço IP do usuário do Telegram usando tshark
def get_ip_address():
    # Comando tshark para capturar pacotes do Telegram
    command = "sudo tshark -f 'tcp port 443 and host telegram.org' -T fields -e ip.src -a duration:10"

    # Executa o comando e retorna a saída
    output = subprocess.check_output(command, shell=True).decode('utf-8')

    # Separa a saída em linhas
    lines = output.strip().split('\n')

    # Retorna o último endereço IP capturado
    return lines[-1]

# Função para obter a localização do endereço IP usando a API do Google Maps
def get_location(ip_address):
    # URL da API do Google Maps
    url = f'https://maps.googleapis.com/maps/api/geocode/json?latlng={ip_address}&key={API_KEY}'

    # Envia uma solicitação GET para a API
    response = requests.get(url)

    # Analisa a resposta JSON
    data = json.loads(response.text)

    # Obtém o endereço formatado e retorna-o
    return data['results'][0]['formatted_address']

# Obtém o endereço IP do usuário do Telegram
ip_address = get_ip_address()

# Obtém a localização do endereço IP
location = get_location(ip_address)

# Exibe o endereço IP e a localização
print(f'Endereço IP: {ip_address}')
print(f'Localização: {location}')
