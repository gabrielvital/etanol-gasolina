print("Chegou a hora de saber se é mais vantajoso abastecer com etanol ou gasolina!")
print("Observe os preços no posto em que você costuma abastecer e informe: ")
gas = float(input("Qual o preço do litro da gasolina? "))
eta = float(input("Qual o preço do litro do etanol? "))
propo = eta / gas

if propo > 0.7:
    print("Abasteça com gasolina!")
if propo < 0.7:
    print("Abasteça com etanol!")
