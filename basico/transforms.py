# ================================================================
# Usando funções transformadoras: sorted, filter, map
# ================================================================


def filtro_numeros(x):
    if x % 2 == 0:
        return True
    return False


def filtro_caracteres(x):
    if x.islower():
        return False
    return True


def numero_ao_quadrado(x):
   return x ** 2


def nota_em_conceito(x):
    if x >= 90:
        return 'A'
    elif (x >= 80 and x <= 90):
         return 'B'
    elif (x >= 70 and x <= 80):
         return 'C'  
    elif (x >= 60 and x <= 70):
         return 'D'
    return 'E'
    


def main():
    # Definindo sequencias para usarmos nesta tarefa
    numeros = (2, 7, 3, 6, 15, 28, 390, 415, 60, 50)
    letras = "bcdEfGHijKlmnOpq"
    notas = (83, 91, 88, 76, 64, 69, 50, 72)

    # TODO: Usando filter para remover itens de uma lista. Filtrando somente pares
    pares = list(filter(filtro_numeros, numeros))
    print(pares)

    # TODO: Usando filter numa sequência de caracteres.  Filtrando somente maiusculas
    maiusculas = list(filter(filtro_caracteres, letras))
    print(maiusculas)

    # TODO: Usando map para criar uma nova sequência de valores. Quadrado da lista numeros
    quadrados = list(map(numero_ao_quadrado, numeros))
    print(quadrados)

    # TODO: Usando sorted e map para alterar as notas de literais para conceito 
    notas = sorted(notas)
    print (notas)
    conceitos = list(map(nota_em_conceito, notas))
    print (conceitos)
    
# Executa a função main() apenas quando o script é executado diretamente
if __name__ == "__main__":
    main()
