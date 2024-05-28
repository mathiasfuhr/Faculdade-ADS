arquivo = open('pessoas.txt', 'w')

arquivo.write("Mathias Fuhr\n")
arquivo.write("Josiane Gass\n")

arquivo.close()

with open('pessoas.txt', 'r+') as arquivoLeitura:
    for linha in arquivoLeitura:
        print(linha)