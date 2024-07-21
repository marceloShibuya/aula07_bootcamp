from etl import ler_csv, filtrar_vendas_maior_1500, soma_dados_filtrados_quantidade

path_arquivo = "vendas.csv"

arquivo_de_saida = ler_csv(path_arquivo)
print(f'Esse é o arquivo de saída {arquivo_de_saida}')
arquivo_filtrado = filtrar_vendas_maior_1500(arquivo_de_saida)
print(f'Esse é o produto de filtrado {arquivo_filtrado}')   
soma_qtd = soma_dados_filtrados_quantidade(arquivo_filtrado)   
print(f'A soma da qtd total é: {soma_qtd}')