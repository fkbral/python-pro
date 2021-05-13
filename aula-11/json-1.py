import json

# Esta seria a representação em string do nosso JSON
jogadorJSONString = '{"nome":"Mario","pontuacao":0}'

# Este seria o JSON real
# jogadorJSON = {
#   "nome": "Mario",
#   "pontuacao": 0
# }

dicionario = json.loads(jogadorJSONString)

print(dicionario)

print(dicionario['nome'])
print(dicionario['pontuacao'])