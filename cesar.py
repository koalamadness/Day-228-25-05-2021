def cifrado_cesar(texto, llave):
  texto_encriptado = ""
  
  for c in texto:

    # revisa si está en mayúscula
    if c.isupper():

      #calculamos la posición en el rango 0-25
      c_indice = ord(c) - ord('A')

      # realizamos el desplazamiento sumando la llave y usando el módulo
      c_desplazado = (c_indice + llave) % 26 + ord('A')

      #convertimos de ASCII a caracter
      c_nuevo = chr(c_desplazado)

      #concatenamos el caracter desplazada a nuestra cadena encriptada
      texto_encriptado += c_nuevo
    
    #revisa si es minúscula
    elif c.islower():

      #calculamos la posición en el rango 0-25
      c_indice = ord(c) - ord('a')

      # realizamos el desplazamiento sumando la llave y usando el módulo
      c_desplazado = (c_indice + llave) % 26 + ord('a')

      #convertimos de ASCII a caracter
      c_nuevo = chr(c_desplazado)

      #concatenamos el caracter desplazada a nuestra cadena encriptada
      texto_encriptado += c_nuevo      
    
    else:

      #cualquier otro caracter que no sea una letra lo concatenamos 
      texto_encriptado += c

  return texto_encriptado

def desencriptar_cesar(texto, llave):
  texto_normal = ""
  
  for c in texto:

    # revisa si está en mayúscula
    if c.isupper():

      #calculamos la posición en el rango 0-25
      c_indice = ord(c) - ord('A')

      # realizamos el desplazamiento restando la llave y usando el módulo
      c_desplazado = (c_indice - llave) % 26 + ord('A')

      #convertimos de ASCII a caracter
      c_nuevo = chr(c_desplazado)

      #concatenamos el caracter desplazada a nuestra cadena encriptada
      texto_normal += c_nuevo
    
    #revisa si es minúscula
    elif c.islower():

      #calculamos la posición en el rango 0-25
      c_indice = ord(c) - ord('a')

      # realizamos el desplazamiento restando la llave y usando el módulo
      c_desplazado = (c_indice - llave) % 26 + ord('a')

      #convertimos de ASCII a caracter
      c_nuevo = chr(c_desplazado)

      #concatenamos el caracter desplazada a nuestra cadena encriptada
      texto_normal += c_nuevo      
    
    else:

      #cualquier otro caracter que no sea una letra lo concatenamos 
      texto_normal += c

  return texto_normal


def configurar_cif_cesar():

  file = open(input("Escribe el nombre del archivo: \n") + ".txt", "r")

  llave_cesar = int(input("La llave del cifrado César: "))

  file_lineas = file.readlines()

  lineas = []

  for linea in file_lineas:
    linea_cifrada = cifrado_cesar(linea, llave_cesar) 
    lineas.append(linea_cifrada)

  file.close()  

  encripted_file = open("archivo_encriptado.txt", "w")

  for linea in lineas:
    encripted_file.write(linea)

  encripted_file.close()

  return lineas, llave_cesar


def configurar_descif_cesar(lineas, llave_cesar):

  normal_file = open("archivo_desencriptado.txt","w")

  for linea in lineas:
    desencriptada = desencriptar_cesar(linea, llave_cesar)
    normal_file.write(desencriptada)

  normal_file.close()  

