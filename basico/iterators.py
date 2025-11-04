# ================================================================
# Usando funções iteradoras (enumerate, zip, iter e next)
# ================================================================


def main():
    # Definindo a lista de dias da semana em Português e Inglês:
    dias = ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sab"]
    dias_en = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    # Usando a função iter para criar um iterador sobre a lista
    iterador_dias = iter(dias)
    print(next(iterador_dias))  # Dom
    print(next(iterador_dias))  # Seg
    print(next(iterador_dias))  # Ter
    print(next(iterador_dias))  # Qua
    print(next(iterador_dias))  # Qui
    print(next(iterador_dias))  # Sex
    print(next(iterador_dias))  # Sab


    # Usando a função para iterar sobre um arquivo
    with open('C:\\Users\Public\\Projetos\\python-estudos\\utilitarios\\dados_iterators.txt', 'r') as fp:
        for linha in iter(fp.readline, ''):
            print(linha)
  
    # Usando a função iter com range sobre a lista dias
    for numero in range(len(dias)):
        print(numero, dias[numero])

    # Usando a função enumerate para reduzir a quantidade de código
    for i, m in enumerate(dias, start=1):
        print(i, m)

    # Usando a função zip para combinar as listas
    for m in zip(dias, dias_en):
        print(m)

    # Combinando zip com enumerate para formatar o resultado
    for i, m in enumerate(zip(dias, dias_en), start=1):
        print(i, m[0], "=", m[1], "em Inglês")

# Executa a função main() apenas quando o script é executado diretamente
if __name__ == "__main__":
    main()
