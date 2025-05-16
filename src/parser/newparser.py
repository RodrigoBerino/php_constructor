import re
from src.model.newclasse import Classe

class UMLParser:
    def __init__(self):
        self.classes = []

    def parse(self, uml_input):
        # Divida o UML de entrada em linhas
        linhas = uml_input.splitlines()
        current_class = None
        associations = []  # Para armazenar relações de agregação/composição

        for linha in linhas:
            # Detectar classe
            match_class = re.match(r'class (\w+)', linha)
            if match_class:
                if current_class:
                    self.classes.append(current_class)  # Adicionar a classe anterior
                current_class = Classe(match_class.group(1))

            # Detectar atributos
            match_atributo = re.match(r'\s*(\w+)\s*:\s*(\w+)', linha)
            if match_atributo and current_class:
                tipo, nome = match_atributo.groups()
                current_class.adicionar_atributo(tipo, nome)

            # Detectar métodos
            match_metodo = re.match(r'\s*(\w+)\s*\(\)\s*', linha)
            if match_metodo and current_class:
                nome = match_metodo.group(1)
                current_class.adicionar_metodo(nome, "void")

            # Detectar associações de agregação e composição
            match_association = re.match(r'(\w+)\s+"1"\s*([*o]+)--\s*"1"\s*(\w+)\s*:\s*(.*)', linha)
            if match_association:
                origem, tipo, destino, relacao = match_association.groups()
                if tipo == '*--':
                    associations.append(("composicao", origem, destino))
                elif tipo == 'o--':
                    associations.append(("agregacao", origem, destino))

        # Adicionar a última classe
        if current_class:
            self.classes.append(current_class)

        return self.classes, associations
