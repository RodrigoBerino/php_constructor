from model.classe import Classe

class UMLParser:
    def parse(self, uml_text):
        uml_text = uml_text.replace("@startuml", "").replace("@enduml", "").strip()
        lista_classe = []
        classe_atual = None

        for linha in uml_text.splitlines():
            linha = linha.strip()
            if linha.lower().startswith("class"):
                if classe_atual:
                    lista_classe.append(classe_atual)
                nome_classe = linha.split()[1]
                classe_atual = Classe(nome_classe)
            elif linha == "}":
                if classe_atual:
                    lista_classe.append(classe_atual)
                    classe_atual = None
            else:
                if ":" in linha:
                    tipo, nome = linha.split(":")
                    classe_atual.adicionar_atributo(tipo.strip(), nome.strip())
                elif "void" in linha:
                    nome_metodo = linha.split()[1].split("(")[0].strip()
                    classe_atual.adicionar_metodo(nome_metodo, "void")
        
        return lista_classe
