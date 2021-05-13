import requests
import json

resposta = requests.get('https://api.github.com/')

# segurança: vamos descartar os dados se a conexão não for um sucesso
if resposta.status_code == 200:
    # print(resposta.text)

    api_github = resposta.json()
    # alternativamente poderiamos converter os dados da reposta (response.text)
    # para dicionário utilizando o método json.loads
    # api_github = json.loads(resposta.text)

    print(api_github["user_repositories_url"])