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
    lista_filtrada = []
    for i in lista:
        if int(i.get("Quantidade")) == int("20"):
            lista_filtrada.append(i)
    return lista_filtrada

path_arquivo = "vendas.csv"
arquivo_de_saida = ler_csv(path_arquivo)
print(f'Esse é o arquivo de saída {arquivo_de_saida}')
arquivo_filtrado = filtrar_vendas_maior_1500(arquivo_de_saida)
print(f'Esse é o produto de filtrado {arquivo_filtrado}')      
    
