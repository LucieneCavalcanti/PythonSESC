import random
numerosDigitados=[0,0,0,0,0,0]
for d in range(6):#pedir 6 números
    while(numerosDigitados[d]<=0 or numerosDigitados[d]>60):
        numerosDigitados[d]=int(input(f"Digite o número {d+1}:"))
        for m in range(6):
            if(numerosDigitados[d]==numerosDigitados[m] and d!=m): 
                numerosDigitados[d]=int(input(f"Digite o número {d+1}:"))

numerosSorteados=[random.randrange(1,60),
                  random.randrange(1,60),
                  random.randrange(1,60),
                  random.randrange(1,60),
                  random.randrange(1,60),
                  random.randrange(1,60)]
print("Os números digitados foram:")
for s in numerosDigitados:
    print(s)
print("Os números sorteados foram:")
for s in numerosSorteados:
    print(s)
for d in numerosDigitados:
    print(f"--verificando o número digitado {d} ---")
    for s in numerosSorteados:
        print(f"-->com o número sorteado{s} ---")
        if(d==s):
            print(f"Você acertou o número {d}")