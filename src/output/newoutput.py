class PHPfile:
    def output(self, codigo):
        output_file = "phpclass/07.php"
        with open(output_file, 'w') as f:
            f.write(codigo)
