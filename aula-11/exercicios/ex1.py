import random
import requests

invalidAnswers = [
  'unremarkable number',
  'boring number',
  'uninteresting number',
  'is a number for which we\'re missing a fact'
]

numero = random.randrange(1, 1001)
resposta = requests.get(f'http://numbersapi.com/{numero}')
respostaValida = False

while not respostaValida :
  respostaValida = True
  
  for invalidAnswer in invalidAnswers:
    if invalidAnswer in resposta.text:
      respostaValida = False
      numero = random.randrange(1, 1001)
      resposta = requests.get(f'http://numbersapi.com/{numero}')

print(resposta.text)
