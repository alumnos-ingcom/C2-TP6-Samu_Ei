########################################################
# Samuel Sisto - @samusisto
# Eimi Saiz - @EimiSaiz
# TP 6 - Eje. x: Xxx
# UNRN Andina - Introducción a Ingeniería en Computación
########################################################

def copiadora(archivo_entrada, archivo_salida):

    archivo_entrada = open(archivo_entrada, encoding="utf8")
    texto = archivo_entrada.read()
    archivo_entrada.close()

    archivo_salida = open(archivo_salida, "w")
    archivo_salida.write(texto)
    archivo_salida.close()

def principal():
    
    a_entrada = input("Ingrese la dirección de archivo de entrada.")
    a_salida = input("Ingrese dirección de archivo de salida.")

    copiadora(a_entrada, a_salida)

if __name__ == "__main__":
    principal()