class Classe:
    def __init__(self, nome):
        self.nome = nome
        self.atributos = []
        self.metodos = []

    def adicionar_atributo(self, tipo, nome):
        self.atributos.append((tipo, nome))

    def adicionar_metodo(self, nome, retorno):
        self.metodos.append((nome, retorno))