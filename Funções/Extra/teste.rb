# Cria um método chamado medida_temp que exibe a temperatura do ambiente.
# Versão melhorada que aceita a temperatura e a unidade como parâmetros.
def medida_temp(temperatura, unidade = "Celsius")
    # Usamos interpolação de string para incluir os valores das variáveis na frase.
    puts "A temperatura do ambiente é de #{temperatura} graus #{unidade}."
end

# Pede ao usuário para digitar a temperatura.
input_temp = "Por favor, digite a temperatura: "
print input_temp

# Lê o que o usuário digitou, remove a quebra de linha (.chomp) e converte para um número (.to_f).
temperatura_lida = gets.chomp.to_f

# Agora chamamos o método, passando o valor fornecido pelo usuário.
medida_temp(temperatura_lida)
