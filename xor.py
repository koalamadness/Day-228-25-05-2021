def encriptarXOR(texto, xorLlave): 
    # Definir una llave, cualquier carácter puede servir    

    # Calcular el tamaño de la cadena
    longitud = len(texto)
  
    # Realizamos la operación XOR con la llave 
    # con cada carácter en la cadena
    for i in range(longitud):
        texto = (texto[:i] + chr(ord(texto[i]) ^ ord(xorLlave)) 
        + texto[i + 1:])

    return texto


def configurar_XOR():
  
  file = open(input("Escribe el nombre del archivo: \n") + ".txt", "r")

  llave_XOR = input("La llave del cifrado XOR: ")

  file_lineas = file.readlines()

  lineas = []

  for linea in file_lineas:
    linea_cifrada = encriptarXOR(linea, llave_XOR) 
    lineas.append(linea_cifrada)

  file.close()

  encripted_file = open("archivo_XOR.txt", "w")

  for linea in lineas:
    encripted_file.write(linea)

  encripted_file.close()    


