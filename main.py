import sys
import os
     
#colocar em diagrama de classe (ok)
#criar relações através do codigo 
#separar as classes em arquivos
#procurar sobre o factyory no php (ok)

def generate_php_class(uml):

    uml = uml.replace("@startuml", "").replace("@enduml", "").strip()

    #linha = input
    lista_classe = []
    classe_atual = None
    corpo_classe = []
#    classe_relationship = []


    for linha in uml.splitlines(): #percorrer a linha 
        linha = linha.strip()
#        if linha == "<|--":
 #           classe_relationship = []     
        if linha.lower().startswith("Class") or linha.startswith("class"):
            if classe_atual:
                lista_classe.append((classe_atual, corpo_classe))
            classe_atual = linha.split()[1]
            corpo_classe = []
        elif linha == "}":
            lista_classe.append((classe_atual, corpo_classe))
            classe_atual = None
            corpo_classe = []
        else:
            corpo_classe.append(linha)
            
    php_classes = []

    for class_name, body in lista_classe:
        php_class = f"<?php\nclass {class_name} {{\n"
        atributos = []
        methods = []
        
         # processamento dos atributos e métodos
        for line in body:
            if ":" in line: 
                parts = line.split(":")
                tipo_atributo = parts[0].strip()
                nome_atributo = parts[1].strip()
                atributos.append((tipo_atributo, nome_atributo))
            elif "void" in line:
                method_name = line.split()[1].split("(")[0].strip()
                methods.append((method_name, "void"))
                
        #atributos
        for tipo_atributo, nome_atributo in atributos:
            php_class += f"$private {nome_atributo};\n"
        #metodos
        for method_name, tipo_retorno in methods:
            php_class += f" public function: {method_name}() {{\n"
            php_class += f"}}\n"
        
     #   for _, nome_atributo in atributos:
      #      php_class += f"\n public function get{nome_atributo.capitalize()}() {{\n"
       #     php_class += f" return $this-> {nome_atributo}; \n }} \n"
        #    php_class += f"public function set {nome_atributo.capitalize()}() {{\n"
         #   php_class += f" $this-> {nome_atributo} = $value \n }} \n"
            
        php_class += "}\n"
        php_classes.append(php_class)
        
    return "\n".join(php_classes)

uml_input = '''@startuml
class Dummy {
  String : data
  void : methods()
}
@enduml'''

php_code = generate_php_class (uml_input)

str = "index.php" 
with open(str,'w') as f:
    f.write(php_code)

print(php_code)