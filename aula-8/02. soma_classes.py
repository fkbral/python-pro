# Resolvendo o mesmo problema com classes
class CalculadoraCompleta:
    def soma_numeros(self, numero1, numero2):
        n1 = numero1
        n2 = numero2
        resultado = n1 + n2
        return resultado
# As classes são nomeadas usualmente com letras maiúsculas de inciais

a = CalculadoraCompleta() # Chamada da classe 'CalculadoraCompleta'
b = a.soma_numeros(10, 1) # Chamada do método 'soma_numeros' dentro da classe com através do a.
print(b)

'''
CONCEITOS

Método: Nome dado a uma função dentro de uma classe. No nosso caso o método é 'soma_numeros'
Atributo: Nome dado a uma variável dentro de uma classe. No nosso caso os atributos são 'n1' e 'n2'
'''

# Porém ao tentar acessar o atributo n1 novamente dará o erro de que o 'n1' não foi definido
print(n1)