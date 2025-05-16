class Classe:
    def __init__(self, nome):
        self.nome = nome
        self.atributos = []  # Lista de atributos
        self.metodos = []    # Lista de métodos
        self.relatorios = []  # Lista de relações (composição, agregação)

    def adicionar_atributo(self, tipo, nome):
        self.atributos.append((tipo, nome))

    def adicionar_metodo(self, nome, retorno):
        self.metodos.append((nome, retorno))

    def adicionar_relacao(self, tipo, origem, destino):
        self.relatorios.append((tipo, origem, destino))

    def __str__(self):
        return f"Classe: {self.nome}, Atributos: {self.atributos}, Métodos: {self.metodos}, Relações: {self.relatorios}"
