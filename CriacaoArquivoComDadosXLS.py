from openpyxl import Workbook

# Cria uma nova planilha em branco
wb = Workbook()

# Seleciona a planilha ativa
planilha = wb.active

for i in range(1,10):
    enderecoA = "A"+str(i)
    print(enderecoA)
    planilha[enderecoA] = 'Olá, número '+str(i)
    enderecoB = "B"+str(i)
    planilha[enderecoB] = (i*2/100)

# Salva o arquivo
wb.save('ExemploDados1.xlsx')