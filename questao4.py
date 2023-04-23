# Suponha que existe uma classe Question que possui
# um método que multiplica duas entradas

# Primeiramente, é demonstrado um método de instância,
# que são os que precisam de uma instância da classe para serem chamados,
# e recebem como primeiro parâmetro a instância (self)
class Question:
    def mult_instance(self, num1, num2):
        return num1*num2

# Agora, tem-se um método de classe que pode ser chamado sem precisar
# de uma instância da classe. Para tanto, usa-se o decorador @classmethod
# Tem-se o método de classe:
    @classmethod
    def mult_class(cls, num1, num2):
        return num1*num2

# Por fim, tem-se um método estático, o qual não depende
# nem de uma instância da classe, nem da classe em si.
# Para tanto, usa-se o decorador @staticmethod

    @staticmethod
    def mult_static(num1, num2):
        return num1*num2


# Exemplos de aplicação:
# Método de instância
res = Question()
result_instance = res.mult_instance(3, 9)
print(result_instance)
# Saída: 27

# Método de classe
result_class = Question.mult_class(7, 11)
print(result_class)
# Saída: 77

# Método estático
result_static = Question.mult_static(5, 17)
print(result_static)
# Saída: 85
