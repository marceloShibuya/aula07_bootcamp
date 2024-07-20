import csv

path_arquivo = "vendas.csv"

def ler_csv(nome_do_arquivo_csv: str) -> list[dict]:
    """
    Funcao que le um arquivo csv e retorna uma lista de dicionarios
    """
    lista = []
    with open(nome_do_arquivo_csv, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for i in leitor:
            lista.append(i)
    return lista


def filtrar_produtos_entregues(lista: list[dict]) -> list[dict]:
    """
    Funcao que filtra produtos onde entrega = True
    """
    lista_filtrada = []
    for i in lista:
        if i.get("entregue") == "True":
            lista_filtrada.append(i)
    return lista_filtrada

lista_de_produtos = ler_csv(path_arquivo)
produtos_entregues = filtrar_produtos_entregues(lista_de_produtos)
# print(f'Dados filtrados para True: {produtos_entregues}')
print(produtos_entregues)


