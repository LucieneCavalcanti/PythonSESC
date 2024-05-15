from openpyxl import Workbook
import math

# Cria uma nova planilha em branco
wb = Workbook()

# Seleciona a planilha ativa
planilha = wb.active


#fórmulas para calcular os juros
def simples(investimento,taxa,tempo):
   tjuro=taxa/100
   valorFuturo= investimento*(1+tjuro*tempo)
   jurototal = investimento*tjuro*tempo
   juroano =investimento*tjuro
   print('\n\n\t\t O valor futuro é de {:.2f}'.format(valorFuturo))
   print('\n\t\t Os juros totais é de {:.2f}'.format(jurototal))
   print('\n\t\t Os juros ao ano é de {:.2f}'.format(juroano))



def composto(investimento,taxa,tempo):
   tjuro=taxa/100
   valorFuturo= investimento*pow(1+tjuro,3)
   jurototal = investimento*(pow(1+tjuro,3)-1)
   print('\n\n\t\t O valor futuro é de {:.2f}'.format(valorFuturo))
   print('\n\t\t Os juros totais é de {:.2f}'.format(jurototal))


#entrada de dados
# def menu():
#     while True:
#         try:
#             menu5 =' |[1] Juros Simples   |'
#             menu1 =' |[2] Juros Compostos |'
#             menu2 =' |[3] Sair            |'
#             menu3 ='---------------------'
#             print ('\n\n')
#             print (menu3.center(80, ' '))
#             print (menu5.center(80, ' '))
#             print (menu1.center(80, ' '))
#             print (menu2.center(80, ' '))
#             print (menu3.center(80, ' '))
#             option = int(input(' Escolha a opção: '))
#             if option == 1:
#              simples()
#              menu()
#             elif option == 2:
#              composto()
#              menu()
#             elif option == 3:
#              print('Fim do Programa')
#              exit()
#             else:
#              print('Escolha Inválida. Escolha entre 1 a 3')
#         except ValueError:
#           print('Escolha Inválida. Escolha entre 1 a 3')
# menu()
valorDoEmprestimo = float(input("Digite o valor a ser emprestado:"))
taxaJuros = float(input("Digite a taxa de juros (sem o %):"))
quantidadeDeParcelas=float(input("Qual é a quantidade de parcelas (meses)?"))

#geracao do arquivo
for i in range(1,int(quantidadeDeParcelas)):
    enderecoA = "A"+str(i)
    print(enderecoA)
    planilha[enderecoA] = str(i)
    enderecoB = "B"+str(i)
    planilha[enderecoB] = (valorDoEmprestimo/quantidadeDeParcelas)*(i+tjuro*tempo)

# Salva o arquivo
wb.save('ExemploDados1.xlsx')