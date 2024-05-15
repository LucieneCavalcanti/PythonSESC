try:
 x = int(input("Digite um numero: "))
 if not type(x) is int:
  raise TypeError("Digite apenas números inteiros.") 
except:
 print("Erro do string e conversão para int")

try:
 y = input("Digite um numero: ")
 if not type(y) is int:
  raise TypeError("Digite apenas numeros inteiros.") 
except:
 print("Erro na conversão de float para int")