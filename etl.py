import csv


def ler_csv(nome_do_arquivo_csv: str) -> list[dict]:
    """
    Funcao que le um arquivo csv e retorna uma lista de dicionarios
    """
    lista = []
    with open(nome_do_arquivo_csv, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for i in leitor:
            lista.append(i)
    return list(lista)


vendas_lista = ler_csv('vendas.csv')
print(vendas_lista)