from openpyxl import Workbook

# Cria uma nova planilha em branco
wb = Workbook()

# Seleciona a planilha ativa
planilha = wb.active

# Define o valor da célula A1
planilha['A1'] = 'Olá, Excel com Python!'

# Salva o arquivo
wb.save('Exemplo.xlsx')