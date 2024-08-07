import csv

def ler_csv(arquivo_csv: str) -> list[dict]:
    """
    Essa funcao vai ler o arquivo csv e salvar em uma lista com dicionario
    """
    lista_produtos = []
    with open(arquivo_csv, mode="r", encoding="utf-8",newline="") as arquivo:
        leitor = csv.DictReader(arquivo)
        for i in leitor:
            lista_produtos.append(i)
    return lista_produtos

def filtrar_vendas_maior_1500(lista: list[dict]) -> list[dict]:
    """
    Funcao para realizar o filtro do campo Quantidade
    """
    lista_filtrada = []
    for i in lista:
        if int(i.get("Quantidade")) >= int("10"):
            lista_filtrada.append(i)
    return lista_filtrada

def soma_dados_filtrados_quantidade(lista_qtd_filtrada: list[dict]) -> int:
    """
    Funcao para somar todos os valores do campo Quantidade
    """
    valor_qtd_total = 0
    for i in lista_qtd_filtrada:
        valor_qtd_total += int(i.get('Quantidade'))
    return valor_qtd_total


