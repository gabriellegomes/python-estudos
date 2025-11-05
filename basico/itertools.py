# =========================================================================
# Usando funções Iteradoras: cycle, count, chain, dropwhile e takewhile
# =========================================================================

import itertools


def condicao(x):
    return x < 30


def main():
    # Iterador cycle usado para iterar sobre uma lista
    pessoas = ["Gabi", "Gabrielle", "Bia"]
    ciclo = itertools.cycle(pessoas)
    print(next(ciclo))
    print(next(ciclo))
    print(next(ciclo))
    print(next(ciclo)) # Ciclo: quando sequencia acaba retorna ao primeiro

    # Usando count para criar um contador 
    contador = itertools.count(50, 10)
    print(next(contador))
    print(next(contador))
    print(next(contador))
    print(next(contador))
    print(next(contador))
    print(next(contador))

    # Usando a função accumulate. Cria um iterador que acumula valores
    valores = [15, 25, 30, 35, 50, 40, 55]
    acumulado = itertools.accumulate(valores, max)
    print(list(acumulado))

    # Usando a função chain para conectar listas
    x = itertools.chain("AEIOU", "12345")
    print(list(x))

    # Usando asa funções dropwhile e takewhile que retornam valores até que uma condição seja atingida
    # Funções complementares. dropwhile retorna só valores quando chegar no valor da condição. Já o
    # takewhile faz o contrário, retorna todos até a condição
    print(list(itertools.dropwhile(condicao, valores)))
    print(list(itertools.takewhile(condicao, valores)))

# Executa a função main() apenas quando o script é executado diretamente
if __name__ == "__main__":
    main()
