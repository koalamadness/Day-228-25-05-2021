from cesar import configurar_cif_cesar, configurar_descif_cesar
from xor import configurar_XOR
continuar = True

def menu():
  
  print("""          Opciones
    1) Cifrado César
    2) Descifrar César
    3) Cifrado XOR
    4) Descifrar XOR
    5) Salir
  """)

while continuar:

  menu()

  opc = int(input("Elige una opción: "))

  if opc == 1:
    print("          Cifrado César")
    lineas, llave_cesar = configurar_cif_cesar()

  elif opc == 2:
    print("          Descifrar César")
    configurar_descif_cesar(lineas, llave_cesar)

  elif opc == 3:
    print("          Cifrado XOR")
    configurar_XOR()

  elif opc == 4:
    print("          Descifrar XOR")
    configurar_XOR()

  elif opc == 5:
    continuar = False
  
  else:
    input("Opción no valida")

  input("Presiona enter para continuar...")

input("Presiona enter para salir...")