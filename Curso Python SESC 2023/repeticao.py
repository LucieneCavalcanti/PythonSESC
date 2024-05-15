import math
valor1=10
valor2=20
contador=2
somaTodos=0
contImpares=0
contPares=0
while (contador>=2):
   try:
    valor3=int(input("Digite um valor inteiro: "))
    contador=contador+1
    somaTodos=somaTodos+valor3
    if (contador>3): break
    if(valor3%2==0): contPares=contPares+1
    else : contImpares=contImpares+1
   except:
     print("erro ao digitar o número")
soma=valor1+valor2+somaTodos
print(soma)
print("Foram digitados ",contPares," números pares.")
print("Foram digitados ",contImpares," números ímpares")
print(math.pi)
print(math.pow(2,2))
print(math.sqrt(25))
print(math.log(15))
print(math.ceil(25.89644885))
nome1="teste"
print(nome1.isnumeric())
nome2="12356"
print(nome2.isnumeric())
nome3=123654
print(type(nome3) is int)
print(type(nome1) is str)