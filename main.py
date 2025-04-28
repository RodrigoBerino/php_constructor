from src.parser.parser import UMLParser
from src.generate_class.generate import PHPGenerator
from src.output.output import PHPfile

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

file = PHPfile()

saida = file.output(codigo_php)

print(codigo_php)
