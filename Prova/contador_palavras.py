# Solicita a palavra e normaliza para minúsculas (case-insensitive)
palavra_alvo = input("Digite a palavra a ser buscada: ").lower()

try:
    # Gerenciamento seguro do arquivo com o gerenciador de contexto 'with'
    with open("votos.txt", "r", encoding="utf-8") as arquivo:
        # Lê todo o conteúdo e normaliza para minúsculas
        conteudo = arquivo.read().lower()
        
        # O método .split() isola os tokens por espaços em branco,
        # garantindo que busquemos a palavra exata e não substrings.
        palavras = conteudo.split()
        
        # Conta as ocorrências exatas da palavra_alvo na lista de palavras
        total = palavras.count(palavra_alvo)

    print("A palavra '%s' foi encontrada %d vezes." % (palavra_alvo, total))

except FileNotFoundError:
    print("Erro: O arquivo 'votos.txt' não foi encontrado.")

    