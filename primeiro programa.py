print("Jogo de advinhação")
numero_secreto = 17
chute_string = input("Digite o nro:")
print("voce digitou o  nro:", chute_string)

chute = int(chute_string)
if(numero_secreto == chute):
    print("você acertou!")
else:
    print("voce errou!")
