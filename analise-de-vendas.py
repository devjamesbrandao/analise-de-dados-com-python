import pandas as pd
import matplotlib.pyplot as plt

# Dados de exemplo abrangendo vários meses
dados_vendas = {
    'Data da venda': [
        '2024-01-15', '2024-02-20', '2024-02-25', '2024-03-10', '2024-03-15',
        '2024-04-01', '2024-04-05', '2024-05-10', '2024-05-20', '2024-06-15'
    ],
    'Nome do cliente': [
        'Ana Maria', 'Júlia', 'Aparecida', 'Maria Augusta', 'Antônia',
        'Dona Lica', 'Antônia do Alcides', 'Lenilda', 'Maria Lara', 'Jamilly'
    ],
    'Produto': [
        'Perfume', 'Creme', 'Shampoo', 'Condicionador', 'Sabonete',
        'Loção', 'Desodorante', 'Creme', 'Shampoo', 'Perfume'
    ],
    'Quantidade': [1, 2, 1, 3, 2, 1, 5, 2, 3, 2],
    'Preço unitário': [100.0, 50.0, 30.0, 20.0, 10.0, 15.0, 25.0, 50.0, 30.0, 100.0],
    'Total da venda': [100.0, 100.0, 90.0, 80.0, 50.0, 90.0, 175.0, 400.0, 270.0, 1000.0],
    'Forma de Pagamento': [
        'Dinheiro', 'Cartão', 'Dinheiro', 'Cartão', 'Pix',
        'Dinheiro', 'Cartão', 'Pix', 'Dinheiro', 'Cartão'
    ]
}

# Criação do DataFrame
df = pd.DataFrame(dados_vendas)

# Conversão da coluna 'Data da venda' para datetime
df['Data da venda'] = pd.to_datetime(df['Data da venda'])

# Análises
# Total de vendas
total_vendas = df['Total da venda'].sum()

# Vendas por produto
vendas_por_produto = df.groupby('Produto')['Total da venda'].sum().sort_values(ascending=False)

# Vendas por mês
df['Mês'] = df['Data da venda'].dt.to_period('M')
vendas_por_mes = df.groupby('Mês')['Total da venda'].sum()

# Vendas por forma de pagamento
vendas_por_pagamento = df.groupby('Forma de Pagamento')['Total da venda'].sum()

# Exibir resultados
print(f'Total de vendas: R${total_vendas:.2f}')
print('\nVendas por produto:')
print(vendas_por_produto)
print('\nVendas por mês:')
print(vendas_por_mes)
print('\nVendas por forma de pagamento:')
print(vendas_por_pagamento)

# Visualização dos dados
# Gráfico de barras das vendas por produto
plt.figure(figsize=(10, 5))
vendas_por_produto.plot(kind='bar')
plt.title('Vendas por Produto')
plt.xlabel('Produto')
plt.ylabel('Total de Vendas (R$)')
plt.show()

# Gráfico de linha das vendas por mês
plt.figure(figsize=(10, 5))
vendas_por_mes.plot(kind='line', marker='o')
plt.title('Vendas por Mês')
plt.xlabel('Mês')
plt.ylabel('Total de Vendas (R$)')
plt.show()

# Gráfico de pizza das vendas por forma de pagamento
plt.figure(figsize=(10, 5))
vendas_por_pagamento.plot(kind='pie', autopct='%1.1f%%')
plt.title('Vendas por Forma de Pagamento')
plt.ylabel('')
plt.show()
