import matplotlib
from matplotlib import pyplot

eixoX_Grafico1 = [10,20,30,40]
eixoY_Grafico1 = [5,10,15,20]
fig, Grafico1 = pyplot.subplots()
Grafico1.plot(eixoX_Grafico1, eixoY_Grafico1)
pyplot.show()

# Dados
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

# Criar uma figura e um eixo
fig, ax = pyplot.subplots()

# Plotar os dados com as personalizações
ax.plot(x, y, color='red', linestyle='--', marker='o', label='dados')

# Adicionar rótulos e título
ax.set_xlabel('Rótulo X')
ax.set_ylabel('Rótulo Y')
ax.set_title('Título')

# Incluir uma legenda
ax.legend()

# Mostrar o gráfico
pyplot.show()

# Dados em uma lista
rótulos = ['Maçãs', 'Laranjas', 'Bananas', 'Uvas', 'Figos']
valores = [5, 3, 6, 4, 7]

# Criar uma figura e eixos
fig, ax = pyplot.subplots()

# Criar o gráfico de barras
ax.bar(rótulos, valores)

# Inserir rótulos de dados e título do gráfico
ax.set_xlabel('Fruta')
ax.set_ylabel('Quantidade')
ax.set_title('Quantidades de Frutas')

# Exibir o gráfico
pyplot.show()

# Dados
rotulos = ['Maçãs', 'Laranjas', 'Bananas', 'Uvas', 'Figos']
tamanhos = [25, 30, 20, 25, 27]
cores = ['red', 'orange', 'yellow', 'blue', 'purple']

# Criar figura e eixos
fig, ax = pyplot.subplots()

# Criar um gráfico de pizza
ax.pie(tamanhos, labels=rotulos, colors=cores, autopct='%1.1f%%')

# Adicionar título
ax.set_title('Distribuição das Frutas')

# Mostrar o gráfico plotado
pyplot.show()

# Dados (cotações diárias das ações)
dias = list(range(1, 13))
vale5 = [82.2, 79.2, 84.0, 86.4, 84.8, 87.2, 88.8, 92.0, 89.6, 92.8, 95.2, 93.6]
unip6 = [75.0, 73.2, 75.6, 77.4, 78.2, 76.8, 78.0, 81.0, 82.2, 83.6, 83.4, 82.2]
bbas3 = [28.3, 27.9, 28.5, 29.2, 29.0, 29.4, 29.7, 30.1, 29.8, 30.2, 30.5, 30.3]

# Criar figura e eixos
fig, ax = pyplot.subplots()

# Plotar os dados
ax.plot(dias, vale5, label='VALE5')
ax.plot(dias, unip6, label='UNIP6')
ax.plot(dias, bbas3, label='BBAS3')

# Mostrar os rótulos dos eixos e a legenda do gráfico
ax.set_xlabel('Dia')
ax.set_ylabel('Preço (R$)')
ax.legend()

# Exibir o gráfico pronto
pyplot.show()