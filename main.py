import os
from parser.uml_parser import UMLParser
from generator.php_generator import PHPGenerator

uml_input = '''@startuml
class Dummy {
  String : data
  void : methods()
}
@enduml'''

parser = UMLParser()
classes = parser.parse(uml_input)

gerador = PHPGenerator()
codigo_php = gerador.gerar_php(classes)

output_file = "Dummy.php"
with open(output_file, 'w') as f:
    f.write(codigo_php)

print(f"Arquivo gerado: {output_file}\n")
print(codigo_php)
