import random
#criação de uma variável
valor=34
#criação de um vetor (vários números)
numeros = [1,34,56,78,23,44] #vetor
print(numeros[4]) #mostra o número que está na posição 4
numeros[4]=567 #alterar o valor que está na posição 4
print(numeros[4]) #mostra o número que está na posição 4
#executa 5 vezes a instrução de entrada de dados
# for x in range(6):
#   numeros[x]=int(input(f"Digite um número {x+1}: "))
# print("\nOs números digitados são:")
# for i in numeros:
#     print(i)

# for x in range(6):
#   print(x)

# frutas = ['banana','maça', 'pera', 'uva','mamão']
# print(frutas[1])

# for posicao in range(4):
#   print(frutas[posicao])

# for texto in frutas:
#   print(texto)

participantes = ['Miguel','Marcelo','Luiz','Rubens',
                 'Lucas','Bia','Angelica','Inês',
                 'Stephane','Ícaro','Luciene',
                 'Graziela','Wendel','Wenderson','Paulo']
print(participantes[random.randrange(len(participantes))])
caracteristicas = ['alto','baixo','pobre','desempregado',
                   'azarento','rico','feliz','bonito',
                   'herdeiro','querido','fofo','trabalhador']
print(caracteristicas[random.randrange(len(
    caracteristicas))])
pedidos= ['comprar um carro','estudar em harvard',
          'aprender inglês','arroz com ovo','picanha',
          'ser alto','dormir','comer bem','viajar',
          'amor','sorvete','ganhar na mega sena']
print(pedidos[random.randrange(len(pedidos))])