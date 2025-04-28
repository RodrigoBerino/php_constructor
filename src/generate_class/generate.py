class PHPGenerator:
    def gerar_classe_php(self, classe):
        php = f"<?php\nclass {classe.nome} \n{{\n"

        for _, nome in classe.atributos:
            php += f"    private ${nome};\n"

        for nome, _ in classe.metodos:
            php += f"\n    public function {nome}() {{\n        // TODO\n    }}\n"

        php += "}\n"
        return php

    def gerar_php(self, classes):
        return "\n".join([self.gerar_classe_php(classe) for classe in classes])