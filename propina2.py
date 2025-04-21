cuenta = int(input("ingrese Total cuenta:50    "))
Porcentaje_propina  = int(input("Que porcentaje de propina desea agregar 10%,15%, 20% :"))
if Porcentaje_propina == 10:
    total_cuenta = (cuenta*0.10)
    print (total_cuenta)
elif Porcentaje_propina == 20:
    total_cuenta = (cuenta*0.20)
    print (total_cuenta)
elif  Porcentaje_propina == 15:
    total_cuenta = (cuenta*0.15 )
    print (total_cuenta)
else :
   print("valor ingresado incorrecto")