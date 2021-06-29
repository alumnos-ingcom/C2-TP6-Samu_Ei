########################################################
# Samuel Sisto - @samusisto
# Eimi Saiz - @EimiSaiz
# TP 6 - Eje. x: Xxx
# UNRN Andina - Introducción a Ingeniería en Computación
########################################################

from codificacion_cesar import decodificador

def manejador_archivo(archivo_entrada, texto_nuevo = None, accion = None):

    if accion == 'w' and texto_nuevo != None:
            
        archivo_entrada = open(archivo_entrada+'.decode', "w")
        archivo_entrada.write(texto_nuevo)
        archivo_entrada.close()

    else:

        try:

            archivo_entrada = open(archivo_entrada, "r")
            texto = archivo_entrada.read()
            archivo_entrada.close()

            return texto

        except FileNotFoundError:

            raise FileNotFoundError('No se encuentra el archivo!')


def principal():
    
    a_entrada = input("Ingrese la dirección de archivo de entrada.")
    cant_rotacion = input("Ingrese la cantidad de rotaciones.")
    
    texto = manejador_archivo(a_entrada)
    print(texto)
    texto_codificado = decodificador(texto, cant_rotacion)

    a_salida = manejador_archivo(a_entrada, texto_codificado, "w")

if __name__ == "__main__":
    principal()