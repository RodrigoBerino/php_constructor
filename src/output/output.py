class PHPfile:
    def output(self, codigo):
        output_file = "phpclass/NewDDummy.php"
        with open(output_file, 'w') as f:
            f.write(codigo)