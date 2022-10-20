from matplotlib.pyplot import table
import pandas as pd 
tabela = pd.read_excel('D:\PythonExcel\Produtos.xlsx')

# tabela.loc[tabela['Tipo']=='Serviço','Multiplicador Imposto'] = 1.5
# tabela['Preço Base Reais'] = tabela['Preço Base Original'] * tabela['Multiplicador Imposto']

# tabela.to_excel('ProdutosNovos.xlsx')
produtos = tabela['Produtos']
lista = []
for item in produtos:
    lista.append(item)
print(lista)
