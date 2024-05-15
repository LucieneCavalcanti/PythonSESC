# Solicita ao usuário que insira a primeira nota
nota1 = float(input("Digite a primeira nota: "))

# Solicita ao usuário que insira a segunda nota
nota2 = float(input("Digite a segunda nota: "))

# Calcula a média das duas notas
media = (nota1 + nota2) / 2

# Exibe a média calculada
print("Sua média é", media)

# Verifica se o aluno foi aprovado ou não com base na média
if media >= 6:
    print("Aprovadoooo")
else:
    print("Já era amiguinhooo")
