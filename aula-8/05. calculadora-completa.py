# A vantagem de utilizar classes é poder concatenar diversas funções de uma vez só e poder chamá-las por uma única classe, como por exemplo:

class CalculadoraCompleta:
    def __init__(self, numero1, numero2):
        self.n1 = numero1
        self.n2 = numero2
        
    def soma_numeros(self):
        self.resultado = self.n1 + self.n2
        return self.resultado
    
    def subtrai_numeros(self):
        self.resultado = self.n1 - self.n2
        return self.resultado
    
    def multiplica_numeros(self):
        self.resultado = self.n1 * self.n2
        return self.resultado
    
    def divide_numerso(self):
        self.resultado = self.n1/self.n2
        return self.resultado

'''    
Agora sim se torna útil utilizar o init para reaproveitar os atributos em diversos métodos diferentes. 
Neste caso estamos utilizando os parâmetros dados 'n1' e 'n2' em todos os 4 métodos.
'''

# Com uma chamada única da Classe CalculadoraCompleta..
a = CalculadoraCompleta(10, 1)

# Eu posso utilizar qualquer um dos métodos acessando por meio do 'a.'
print(a.subtrai_numeros())

print(a.multiplica_numeros())