carro1 = {
    "modelo": "Fiesta",
    "estilo": "hatch",
    "cor": "prata",
}

carro2 = {
    "modelo": "Civic",
    "estilo": "sedan",
    "cor": "preto",
    "assegurado": True
}

print(carro1.keys())
print(carro1.values())
print(carro2.keys())
print(carro2.values())

for chave in carro1.keys():
    print(chave)
for chave in carro1:
    print(chave)

print("="*30)

for valor in carro1.values():
    print(valor)
for chave in carro1:
    print(carro1[chave])
