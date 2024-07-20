
# def soma(valor_1: float, valor_2: float) -> float:
#     """
#     uma funcao simples de soma do tipo float que retorna um float
#     """
#     resultado_soma = valor_1 + valor_2
#     return resultado_soma


# valor_soma = soma(valor_1 = 4,valor_2 = 6)

# print(f'Resultado do primeiro exemplo de função ficou em: {valor_soma}')

# valor_soma2 = soma(2.15,2.15)
# print(f'Resultado do segundo exemplo de função ficou em: {valor_soma2}')



def somar_10(valor_1: float, valor_2: float = 10) -> float:
    somar_10 = valor_1 + valor_2
    return somar_10

resultado_soma = somar_10(10)
print(resultado_soma)
