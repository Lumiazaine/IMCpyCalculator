
print("Calculadora de IMC")
Peso = float(input("Introduce tu peso: "))
Altura = float(input("Introduce tu altura: "))
imc = Peso/Altura
print("Tu IMC es " + str(round(imc)))

if imc <= 18.5:
    print("Tienes un peso menor a lo normal")
elif imc >= 18.5 and 24.9:
    print("Tienes un peso normal")
elif imc >= 25 and 29:
    print("Tines sobrepeso")
elif imc >= 35.5 and 39.9:
    print("Tienes obesidad grado 1")
elif imc >= 40:
    print("Padeces obesidad mórbida de alto riesgo")
else:
    print("Error")
