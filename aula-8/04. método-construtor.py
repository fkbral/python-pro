# Agora vamos utilizar o método construtor

class CalculadoraCompleta:
    def __init__(self, numero1, numero2):
        self.n1 = numero1
        self.n2 = numero2

    def soma_numeros(self):
        self.resultado = self.n1 + self.n2


# Utilizamos o método __init__ para construir os atributos que serão utilizados em comum com diversos métodos
# Dessa vez eu precisei já passar os valores dos atributos porque estão no meu método construtor
a = CalculadoraCompleta(10, 1)
a.soma_numeros()
print(a.resultado)
