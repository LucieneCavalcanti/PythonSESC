import math
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
valorDoEmprestimo = float(input("Digite o valor a ser emprestado:"))
taxaJuros = float(input("Digite a taxa de juros (sem o %):"))
quantidadeDeParcelas=float(input("Qual é a quantidade de parcelas (meses)?"))
simples(valorDoEmprestimo,taxaJuros,quantidadeDeParcelas)
