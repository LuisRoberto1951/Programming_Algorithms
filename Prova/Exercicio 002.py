# --- MODO INICIANTE ---

# Primeiro, definimos uma função. Uma função é um bloco de código que só é executado quando a chamamos.
# Ela recebe um valor 'x' (número de máquinas) e retorna a produção.
def calcular_producao(x):
    """
    Calcula a produção de uma fábrica com base no número de máquinas.
    """
    # A primeira regra é: se o número de máquinas for negativo, não há produção.
    if x < 0:
        return 0
    else:
        # Se o número de máquinas for 0 ou mais, calculamos a produção.
        # A fórmula é: -x² + 10x + 50
        producao = -x**2 + 10 * x + 50
        
        # Uma fábrica não pode ter produção negativa.
        # Então, se o cálculo resultar em um número negativo, consideramos a produção como 0.
        if producao < 0:
            return 0
        else:
            return producao

# --- Parte Principal do Programa ---

# Pedimos ao usuário para digitar o número de máquinas.
# O 'float()' converte o texto digitado em um número com casas decimais.
numero_maquinas = float(input("Digite o número de máquinas (x): "))

# Chamamos a função que criamos e guardamos o resultado na variável 'producao_total'.
producao_total = calcular_producao(numero_maquinas)

# Mostramos o resultado final para o usuário.
print(f"A produção para {numero_maquinas} máquinas é de {producao_total} unidades.")