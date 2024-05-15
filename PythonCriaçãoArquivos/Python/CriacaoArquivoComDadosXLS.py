from openpyxl import Workbook
# Cria uma nova planilha em branco
minhaPlanilha = Workbook()
# Seleciona a planilha ativa
planilha = minhaPlanilha.active
for i in range(1,10):
    enderecoA = "A"+str(i)
    planilha[enderecoA] = 'Teste com o '+str(i)
    enderecoB = "B"+str(i)
    planilha[enderecoB] = (i*2/100)

# Salva o arquivo
minhaPlanilha.save('ExemploDados3.xlsx')