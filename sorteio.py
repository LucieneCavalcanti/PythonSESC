#V1) imprime na tela 6 números entre 1 e 60
#V2) imprimir 10 números diferentes
import random
cont=1
while(cont<=10):
    print(random.randrange(1,60)) #V1
    cont+=1 #cont=cont+1

#armazenando os 10 números sorteados
numero1=random.randrange(1,60)
numero2=random.randrange(1,60)
numero3=random.randrange(1,60)
numero4=random.randrange(1,60)
numero5=random.randrange(1,60)
numero6=random.randrange(1,60)
numero7=random.randrange(1,60)
numero8=random.randrange(1,60)
numero9=random.randrange(1,60)
numero10=random.randrange(1,60)
#verifica se o número 1 está repetido (até o 10)
while(numero1==numero2 or numero1==numero3 or
      numero1==numero4 or numero1==numero5 or
      numero1==numero6 or numero1==numero7 or
      numero1==numero8 or numero1==numero9 or
      numero1==numero10):
    numero1=random.randrange(1,60)
while(numero2==numero1 or numero2==numero3 or
      numero2==numero4 or numero2==numero5 or
      numero2==numero6 or numero2==numero7 or
      numero2==numero8 or numero2==numero9 or
      numero2==numero10):
    numero2=random.randrange(1,60)
while(numero3==numero1 or numero3==numero2 or
      numero3==numero4 or numero3==numero5 or
      numero3==numero6 or numero3==numero7 or
      numero3==numero8 or numero3==numero9 or
      numero3==numero10):
    numero3=random.randrange(1,60)
while(numero4==numero1 or numero4==numero2 or
      numero4==numero3 or numero4==numero5 or
      numero4==numero6 or numero4==numero7 or
      numero4==numero8 or numero4==numero9 or
      numero4==numero10):
    numero4=random.randrange(1,60)
while(numero5==numero1 or numero5==numero2 or
      numero5==numero3 or numero5==numero4 or
      numero5==numero6 or numero5==numero7 or
      numero5==numero8 or numero5==numero9 or
      numero5==numero10):
    numero5=random.randrange(1,60)
while(numero6==numero1 or numero6==numero2 or
      numero6==numero3 or numero6==numero4 or
      numero6==numero5 or numero6==numero7 or
      numero6==numero8 or numero6==numero9 or
      numero6==numero10):
    numero2=random.randrange(1,60)
while(numero7==numero1 or numero7==numero2 or
      numero7==numero3 or numero7==numero4 or
      numero7==numero5 or numero7==numero6 or
      numero7==numero8 or numero7==numero9 or
      numero7==numero10):
    numero7=random.randrange(1,60)
while(numero8==numero1 or numero8==numero2 or
      numero8==numero3 or numero8==numero4 or
      numero8==numero5 or numero8==numero6 or
      numero8==numero7 or numero8==numero9 or
      numero8==numero10):
    numero8=random.randrange(1,60)
while(numero9==numero1 or numero9==numero2 or
      numero9==numero3 or numero9==numero4 or
      numero9==numero5 or numero9==numero6 or
      numero9==numero7 or numero9==numero8 or
      numero9==numero10):
    numero9=random.randrange(1,60)
while(numero10==numero1 or numero10==numero2 or
      numero10==numero3 or numero10==numero4 or
      numero10==numero5 or numero10==numero6 or
      numero10==numero7 or numero10==numero8 or
      numero10==numero9):
    numero10=random.randrange(1,60)
#pedir para o usuário digitar 5 números
digitado1=0
digitado2=0
digitado3=0
digitado4=0
digitado5=0
while(digitado1<=0 or digitado1>60):
 digitado1=int(input("Digite o primeiro número:"))
while(digitado2<=0 or digitado2>60):
 digitado2=int(input("Digite o segundo número:"))
while(digitado3<=0 or digitado3>60):
 digitado3=int(input("Digite o terceiro número:"))
while(digitado4<=0 or digitado4>60):
 digitado4=int(input("Digite o quarto número:"))
while(digitado5<=0 or digitado5>60): 
 digitado5=int(input("Digite o quinto número:"))

while(digitado1==digitado2 or digitado1==digitado3 or 
      digitado1==digitado4 or digitado1==digitado5):
     digitado1=input("Digite novamente o número 1")
     while(digitado1<=0 or digitado1>60):
      digitado1=input("Digite um número entre 1 e 60: ")
while(digitado2==digitado1 or digitado2==digitado3 or
      digitado2==digitado4 or digitado2==digitado5):
    digitado2=input("Digite novamente o número 2")
    while(digitado2<=0 or digitado2>60):
      digitado2=input("Digite um número entre 1 e 60: ")
while(digitado3==digitado1 or digitado3==digitado2 or
      digitado3==digitado4 or digitado3==digitado5):
    digitado3=input("Digite novamente o número 3")
    while(digitado3<=0 or digitado3>60):
      digitado3=input("Digite um número entre 1 e 60: ")
while(digitado4==digitado1 or digitado4==digitado2 or
      digitado4==digitado3 or digitado4==digitado5):
    digitado4=input("Digite novamente o número 2")
    while(digitado4<=0 or digitado4>60):
      digitado4=input("Digite um número entre 1 e 60: ")
while(digitado5==digitado1 or digitado5==digitado2 or
      digitado5==digitado3 or digitado5==digitado4):
    digitado5=input("Digite novamente o número 5")
    while(digitado5<=0 or digitado5>60):
      digitado5=input("Digite um número entre 1 e 60: ")
#mostrar quais acertou e quais errou    
#mostra os 10 números sorteados
print("---- 10 números sorteados ----")
print(numero1)
print(numero2)
print(numero3)
print(numero4)
print(numero5)
print(numero6)
print(numero7)
print(numero8)
print(numero9)
print(numero10)
