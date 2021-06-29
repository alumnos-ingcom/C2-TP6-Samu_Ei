########################################################
# Samuel Sisto - @samusisto
# Eimi Saiz - @EimiSaiz
# TP 6 - Eje. 3: Copiadora
# UNRN Andina - Introducción a Ingeniería en Computación
########################################################

def copiadora(archivo_entrada, archivo_salida):

    archivo_entrada = open(archivo_entrada, encoding="utf8")
    texto = archivo_entrada.read()
    archivo_entrada.close()

    archivo_salida = open(archivo_salida, "w")
    archivo_salida.write(texto)
    archivo_salida.close()


def prueba():
    
    a_entrada = input("Ingrese la dirección de archivo de entrada.\n")
    a_salida = input("Ingrese dirección de archivo de salida.\n")

    copiadora(a_entrada, a_salida)

if __name__ == "__main__":
    prueba()