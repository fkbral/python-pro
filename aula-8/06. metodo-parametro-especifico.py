# Podemos utilizar métodos com parâmetros específicos para eles, cujos valores não poderão ser usados em nenhum outro método
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

# Neste caso utilizaremos um parâmetro exclusivo do método exponencial, portanto só poderá ser utilizado dentro dele
    def exponencial(self, e):
        self.resultado = self.n1**e
        return self.resultado


a = CalculadoraCompleta(10, 1)
# Agora é necessário passar o parâmetro 'e' para o método exponencial. Caso contrário haverá alerta de erro
print(a.exponencial(3))
