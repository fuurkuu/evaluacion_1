def suma():
  suma=0
  numero=input("dime un numero: ")
  for cont in range(0,len(numero)):
    suma=suma+int(numero[cont])
  print(str(suma))
suma()
