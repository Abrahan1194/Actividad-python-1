print("Adivinando el nuemro !")
numero = int(7)
while True:
   numero_usuario = int(input("ingrese numero :"))
   if numero_usuario > numero:
    print ("Numero es mayor")
   elif numero_usuario < numero:
    print ("Numero es menor")
  else numero_usuario == numero:
    print("numero es igual")
  break
