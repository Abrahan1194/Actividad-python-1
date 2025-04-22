peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Tu IMC es:", imc, "bajo peso")
elif 18.5 <= imc < 25:
    print("Tu IMC es:", imc, "normal")
elif 25 <= imc < 30:
    print("Tu IMC es:", imc, "sobrepeso")
elif imc >= 30:
    print("Tu IMC es:", imc, "obesidad")