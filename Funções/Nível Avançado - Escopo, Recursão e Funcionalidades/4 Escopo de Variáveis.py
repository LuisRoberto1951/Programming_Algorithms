# Variável Global
global_user = input("Digite algo para a variável GLOBAL: ")

def testar_escopo():
    # Variável Local
    local_user = input("Digite algo para a variável LOCAL: ")
    
    print("\n--- Dentro da Função ---")
    print(f"Eu consigo ver a Global: {global_user}")
    print(f"Eu consigo ver a Local: {local_user}")

# Executando a função
testar_escopo()

print("\n--- Fora da Função ---")
print(f"Global continua viva: {global_user}")

# Tentar imprimir a local aqui fora causaria um erro
try:
    print(f"Tentando ver a Local: {global_user}")
except NameError:
    print("Erro: A variável 'local_user' não existe fora da função!")