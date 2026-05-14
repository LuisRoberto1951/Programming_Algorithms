def calcular_fatura(minutos):
    """
    Calcula o valor da fatura com base em uma taxa fixa e um custo por minuto.
    Esta é uma função afim: C(m) = 0.50*m + 20.00
    """
    TAXA_FIXA = 20.00
    CUSTO_POR_MINUTO = 0.50
    
    custo_total = (CUSTO_POR_MINUTO * minutos) + TAXA_FIXA
    return custo_total

try:
    minutos_consumidos = float(input("Digite a quantidade de minutos utilizados: "))
    
    valor_a_pagar = calcular_fatura(minutos_consumidos)
    
    print(f"O valor total da fatura é: R$ {valor_a_pagar:.2f}")
except ValueError:
    print("Erro: Por favor, digite um valor numérico para os minutos.")