
def verificaLongitud(contraseña):
  longitud=len(contraseña)
  respuesta=True
  if(longitud<=8):
    respuesta=False
  return(respuesta)

def verificaMayusculas(contraseña):
  respuesta=False
  for cont in range(0,len(contraseña)):
    if(contraseña[cont].isupper()):
      respuesta=True
  return(respuesta)

def verificaMinusculas(contraseña):
  respuesta=False
  for cont in range(0,len(contraseña)): 
    if(contraseña[cont].islower()):
      respuesta=True
  return(respuesta)

def verificaNumeros(contraseña):
  respuesta=False
  for cont in range(0,len(contraseña)):
    if(contraseña[cont].isnumeric()):
      respuesta=True
  return(respuesta)

def verificaEspaciosBlancos(contraseña):
  respuesta=False
  for cont in range(0,len(contraseña)):
    if(contraseña[cont]==" "):
      respuesta=True
  return(respuesta)

def verificaCaracteresExtraños(contraseña):
  lista="!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
  respuesta=False
  for cont1 in range(0,len(contraseña)):
    for cont2 in range(0,len(lista)):
      if(contraseña[cont1]==lista[cont2]):
        respuesta=True
  return(respuesta)
  
  





def verificaContraseña():
  
  contraseña=input("Ingrese una contraseña: ")
  validez=0
  
  if(verificaLongitud(contraseña)==True):
    validez=validez+1
    print("Tiene longitud correcta")
  else:
    (print("demasiado corta"))
  
  if(verificaMayusculas(contraseña)==True):
    validez=validez+1
    print("Contiene al menos 1 mayúscula")
  else:
    print("no tiene mayusculas")
  
  if(verificaMinusculas(contraseña)==True):
    validez=validez+1
    print("Contiene al menos una minúscula")
  else:
    print("ni tiene minusculas")
  
  if(verificaNumeros(contraseña)==True):
    validez=validez+1
    print("Contiene al menos un número")
  else:
    print("ni tiene numeros")
  
  if(verificaCaracteresExtraños(contraseña)==True):
    validez=validez+1
    print("Contiene al menos un carácter extraño")
  else:
    print("faltan caracteres extraños")
  
  if(verificaEspaciosBlancos(contraseña)==False):
    validez=validez+1
    print("No contiene espacios en blanco")
  else:
    print("no se permiten espacios blancos")
  
  print("Validez = "+str(validez))
  if(validez==6):
    print("Contraseña VÁlIDA")
  else:
    print("Busca otra contraseña")

verificaContraseña()
    
