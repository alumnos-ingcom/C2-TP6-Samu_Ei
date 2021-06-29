########################################################
# Samuel Sisto - @samusisto
# Eimi Saiz - @EimiSaiz
# TP 6 - Eje. 6: Etiquetas HTML parte 2 (opcional)
# UNRN Andina - Introducción a Ingeniería en Computación
########################################################

def hace_etiqueta(contenido, etiqueta):

    nueva_etiqueta = f'<{etiqueta}>{contenido}</{etiqueta}>' 

    return nueva_etiqueta

def hace_comenta(contenido):

    nuevo_comentario = f'<!-- {contenido} -->' 

    return nuevo_comentario


def creador_pagina():

    e_h1 = hace_etiqueta('Hola HTML.','h1')
    e_parrafo = hace_etiqueta('Esto es un párrafo.','p')
    e_boton = hace_etiqueta('Esto es un botón.','button')
    e_comentario = hace_comenta('Este es un comentario.')
    e_body = hace_etiqueta(e_h1 + e_parrafo + e_comentario + e_boton,'body')
    e_html = hace_etiqueta(e_body,'html')

    texto_pagina = e_html

    return texto_pagina

def manejador_archivo(texto, nombre_archivo):

    nuevo_archivo = open(nombre_archivo + '.html', "w")

    nuevo_archivo.write(texto)

    nuevo_archivo.close()


def prueba():
    
    nombre_archivo = input("Ingrese un nombre para el archivo a guardar.\n")

    texto = creador_pagina()

    manejador_archivo(texto, nombre_archivo)

if __name__ == "__main__":
    prueba()