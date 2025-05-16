class PHPGenerator:
    def gerar_classe_php(self, classe, associations):
        php = f"<?php\nclass {classe.nome} \n{{\n"

        # Gerar atributos
        for _, nome in classe.atributos:
            php += f"    private ${nome};\n"

        # Gerar métodos
        for nome, _ in classe.metodos:
            php += f"\n    public function {nome}() {{\n        // TODO\n    }}\n"

        # Gerar composição e agregação
        for relacao, origem, destino in associations:
            if origem == classe.nome:
                if relacao == "composicao":
                    php += f"\n    private ${destino.lower()};  // Composição\n"
                    php += f"    public function __construct() {{\n"
                    php += f"        $this->{destino.lower()} = new {destino}();\n"
                    php += f"    }}\n"
                elif relacao == "agregacao":
                    php += f"\n    private ${destino.lower()};  // Agregação\n"
                    php += f"    public function __construct({destino} ${destino.lower()}) {{\n"
                    php += f"        $this->{destino.lower()} = ${destino.lower()};\n"
                    php += f"    }}\n"

        php += "}\n"
        return php

    def gerar_php(self, classes, associations):
        return "\n".join([self.gerar_classe_php(classe, associations) for classe in classes])
