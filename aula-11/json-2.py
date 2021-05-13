import json

jogador = {}
jogador = {
  'nome': 'Mario',
  'pontuacao' : 0,
}
# jogador['nome']  = 'Mario'
# jogador['pontuacao'] = 0

stringjson = json.dumps(jogador)

print(stringjson)