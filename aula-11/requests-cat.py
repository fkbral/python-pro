import requests

response = requests.get('https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=1')

print(f'O corpo da resposta é:{response.text}')
print(f'Os cabeçalhos da requisição são: {response.headers}')
print(f'O status de resposta à requisição http foi: {response.status_code}')


if response.status_code == 200:
  print(response.json()["text"])
  print(response.json()["user"])
  print(response.json()["createdAt"])