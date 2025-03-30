import sys
import os
     
def generate_php_class(uml):
    # Remove as linhas de início e fim do UML
    uml = uml.replace("@startuml", "").replace("@enduml", "").strip()

    linha = input()
    lista_classe = []
    classe_atual = None
    corpo_classe = []


    for item in linha:
        item = linha.strip()
        if item.startswith("Class" or "class"):
            if classe_atual:
                lista_classe.append((classe_atual, corpo_classe))
            classe_atual = linha.split()[1]
            corpo_classe = []
        elif linha == "}":
            lista_classe.append((classe_atual, corpo_classe))
            classe_atual = None
            corpo_classe = []
            
    php_classes = []

    for class_name, body in lista_classe:
        php_class = f"<?php\nclass {class_name} {{\n"
        atributos = []
        methods = []
        
        for line in body:
            if ":" in line: 
                parts = line.split(":")
                tipo_atributo = parts[0].strip()
                nome_atributo = parts[0].strip()
                atributos.append((tipo_atributo, nome_atributo))
            elif "void" in line:
                method_name = line.split()[1].split("(")[0].strip()
                methods.append((method_name, "void"))
                
                
        for tipo_atributo, nome_atributo in atributos:
            php_class += f"$private {nome_atributo};\n"
            
        for method_name, tipo_retorno in methods:
            php_class += f" public function: {method_name}() {{\n"
            php_class += f"}}\n"
        
        for _, nome_atributo in atributos:
            php_class += f"\n public function get{nome_atributo.capitalize()}() {{\n"
            php_class += f" return $this-> {nome_atributo}; \n }} \n"
            php_class += f"public function set {nome_atributo.capitalize()}() {{\n"
            php_class += f" $this-> {nome_atributo} = $value \n }} \n"
            
        php_class += "}\n"
        php_classes.append(php_class)
        
    return "\n".join(php_classes) 
    }}

uml_input = input 

php_code = generate_php_class (uml_input)
print(php_code)

'''linha = input()
lista = []

for item in linha.split():
    lista.append(str(item))
print(lista)'''



# str = "cortezia.php" 
# with open(str,'x') as f:
#    f.write('teste')