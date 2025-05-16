#from src.parser.parser import UMLParser
from src.parser.newparser import UMLParser
#from src.generate_class.generate import PHPGenerator
from src.generate_class.newgenerate import PHPGenerator
#from src.output.output import PHPfile
from src.output.newoutput import PHPfile

uml_input = '''class Departamento {
  nome: String
  exibirInfo(): void
}

class Funcionario {
  nome: String
  exibirInfo(): void
}

Departamento "1" o-- "1" Funcionario : tem
@enduml
'''

parser = UMLParser()

classes, associations = parser.parse(uml_input)

gerador = PHPGenerator()

codigo_php = gerador.gerar_php(classes, associations)

file = PHPfile()

saida = file.output(codigo_php)

print(codigo_php)
