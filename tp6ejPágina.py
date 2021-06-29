########################################################
# Samuel Sisto - @samusisto
# Eimi Saiz - @EimiSaiz
# TP 6 - Eje. : Página
# UNRN Andina - Introducción a Ingeniería en Computación
########################################################

def hace_etiqueta(contenido, etiqueta, atributos = None):

    nueva_etiqueta = f'<{etiqueta}'

    if atributos != None:
        for atributo in atributos:

            nuevo_atributo = ' ' + atributo + ' = "' + atributos.get(atributo) + '" '
            nueva_etiqueta += nuevo_atributo 

    nueva_etiqueta += f'>{contenido}</{etiqueta}>'

    return nueva_etiqueta

def hace_comenta(contenido):

    nuevo_comentario = f'<!-- {contenido} -->' 

    return nuevo_comentario


def creador_pagina():

    e_h1 = hace_etiqueta('Hola HTML','h1', {'style':'color: blue;', 'id':'titulo_principal'})
    e_parrafo = hace_etiqueta('Esto es un párrafo','p')
    e_boton = hace_etiqueta('Link de usuario GitHub de la cátedra','button', {'style':'color: blue'})
    e_comentario = hace_comenta('Este es un comentario.')

    e_link = hace_etiqueta(e_boton, 'a', {'href':'https://github.com/INGCOM-UNRN'})
    e_body = hace_etiqueta(e_h1 + e_parrafo + e_comentario + e_link,'body')
    e_html = hace_etiqueta(e_body,'html')

    pagina = e_html

    return pagina

def manejador_archivo(texto, nombre_archivo):

    nuevo_archivo = open(nombre_archivo + '.html', "w")

    nuevo_archivo.write(texto)

    nuevo_archivo.close()


def prueba():
    
    texto = creador_pagina()

    manejador_archivo(texto, 'Página')

if __name__ == "__main__":
    prueba()