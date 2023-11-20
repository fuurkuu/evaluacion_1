def cuenta_vocales():
  palabra=input("Dime una palabra: ")
  numeroVocales=0
  for cont in range(0,len(palabra)):
    if((palabra[cont]== "A" or palabra[cont]=="a")
      or(palabra[cont]== "E" or palabra[cont]=="e")
      or(palabra[cont]== "I" or palabra[cont]=="i")
      or(palabra[cont]== "O" or palabra[cont]=="o")
      or(palabra[cont]== "U" or palabra[cont]=="u")):
      numeroVocales=numeroVocales+1
  #Mostramos el número de aes contadas
  print("La palabra "+palabra+" tiene "+str(numeroVocales)+ " vocales")

cuenta_vocales()
