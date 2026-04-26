# 1. Abre o arquivo para ESCRITA ("w")
arquivo = open("novo_poema.txt", "w", encoding="utf-8")

# 2. Escreve o texto
arquivo.write(" No meio do caminho tinha uma pedra \n tinha uma pedra no meio do caminho \n tinha uma pedra \n no meio do caminho tinha uma pedra")

# 3. FECHA o arquivo (Isso é essencial para salvar no Windows)
arquivo.close()

print("Arquivo 'novo_poema.txt' criado com sucesso!")

# 4. Agora, vamos abrir para LER e mostrar no terminal
with open("novo_poema.txt", "r", encoding="utf-8") as leitura:
    print("\nConteúdo do arquivo criado:")
    print(leitura.read())