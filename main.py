print("Calculadora de IMC")
Peso = input("Introduce tu peso: ")
Altura = input("Introduce tu altura: ")
imc = int(Peso)/float(Altura)
print("Tu IMC es " + str(round(imc)))

if int(imc) <= 18.5:
    print("Tienes un peso menor a lo normal")
elif int(imc) >= 18.5 and 24.9:
    print("Tienes un peso normal")
elif int(imc) >= 25 and 29:
    print("Tines sobrepeso")
elif int(imc) >= 35.5 and 39.9:
    print("Tienes obesidad grado 1")
elif int(imc) >= 40:
    print("Padeces obesidad mórbida de alto riesgo")
else:
    print("Error")