# Utilizando o 'self'

class CalculadoraCompleta:
    def soma_numeros(self, numero1, numero2):
        self.n1 = numero1
        self.n2 = numero2
        self.resultado = self.n1 + self.n2
        return self.resultado
# Repare na diferença de que agora todos os meus atributos dentro do método possuem um acesso através do 'self.' 
# para que todos eles tenham um valor associado a eles

a = CalculadoraCompleta()
b = a.soma_numeros(10, 1)
print(b)

# Agora sim eu posso acessar o atributo 'n1' da mesma forma que acessamos o método
print(a.n1)