#IMC = Peso / (Altura * Altura)

print("academaia mc valinhos")
print(".........................")
print("seja bem-vindo(a)!")

nome = input("me diga, por favor me diga seu nome: ")
idade = int(input("agora preciso que voce me informe a sua idade: "))
altura = float(input("informe a sua altura: "))
nascimento = 2024 - idade
peso = float(input("informe o seu peso: "))
IMC = peso / (altura * altura)

print("ola senhor (a)", nome)
print("sua idade e: ", idade, "anos.")
print("voce nasceu em: ", nascimento)
print("sua altura e de: ", altura, "metros.")
print("seu peso e: ", peso)
print("seu imc e: {:.2f} kg/m²".format(IMC))
