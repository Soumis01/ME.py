from ast import Expression
import os

CARPETA = 'contactos/' #Carpeta de contactos
EXTENSION = '.txt' #extension de archivos

#orden en que se mostrará la información del contacto
class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria

def app():
    #revisa si la carpeta ya existe o no 
    crear_directorio()

    #mostar menú de opciones
    mostar_menu()

    #Preguantar al usuario la accion a realizar

    preguntar = True
    while preguntar:
        opcion = input('Seleccione una opción: \r\n')
        opcion = int(opcion)

        #ejecuar opción
        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contacto()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        else:
            print('Opción no valida intente de nuevo')

def eliminar_contacto():
    nombre = input('Seleccione al contacto que desea eliminar: \r\n')

    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print('\r\nEliminado con exito')
    except Expression as identifier:
        print('No exite ese contacto')
    
    app()

def mostrar_contacto():
    nombre = input('Seleccione al contacto que desea buscar: \r\n')

    try:
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print('\r\n Informacion del contacto \r\n')
            for linea in contacto:
                print(linea.rstrip())
                print('\r\n')
    except IOError:
        print('El archivo no exite')
        print(IOError)
        
    app()


def mostrar_contacto():
    archivos = os.listdir(CARPETA)

    archivos_txt = [i for i in archivos if i.endwith(EXTENSION)]

    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            #imprime los contactos
            for linea in contacto:
                print(linea.rsplit())
            #imprime un separador entre los contactos
            print('\r\n')

def editar_contacto():
    print('Escribe el nombre del contacto a editaar')
    nombre_anterior = input('Nombre del contacto que desea editar: \r\n')

    #validacion del contacto para ver si existe para poder editar 
    existe = existe_contacto(nombre_anterior)

    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:

            #resto de los campos
            nombre_contacto = input('Agrega el nuevo nombre: \r\n')
            telefono_contacto = input('Agrega el nuevo telefono:\r\n')
            categoria_contacto = input('Categoria del nuevo contacto:\r\n')

            #instanciar los datos 
            contacto = Contacto (nombre_contacto, telefono_contacto, categoria_contacto)

            #escribir en el archivo 
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Telefono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoría: ' + contacto.categoria + '\r\n')

            #renombrar en el archivo
            os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)

            #mensaje de exito
            print('Este contacto de a editaco con exito')

    else:
        print('Ese contacto no existe')

    app()



def agregar_contacto():
    print('Escribe los datos para agregar un nuevo contacto: ' )
    nombre_contacto = input('Nombre del contacto: \r\n')

    #validar si el nombre ya existe, antes de crearlo 
    existe = existe_contacto(nombre_anterior)
    
    if not existe:

        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:


            #resto de los campos
            telefono_contacto = input('Agregar el telefono:\r\n')
            categoria_contacto = input('Categoría del contacto:\r\n')

            #instanciar la clase
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            #escribir en el archivo
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Telefono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoría: ' + contacto.categoria + '\r\n')

            #mostar un mendaje de exito de que todo salió bien con el guardado
            print('\r\n Contacto creado correctamente \r\n')

    else:
        print('Ese contacto ya existe\r\n')

    #reinicar la app
    app()

def mostar_menu():
    print('Seleccione lo que desea hacer: ')
    print('1) Agregar contacto')
    print('2) Editar contacto')
    print('3) Ver contactos')
    print('4) Buscar contacto')
    print('5) Eliminar contacto')

def crear_directorio():
    if not os.path.exists(CARPETA):
        os.makedirs(CARPETA)
        #crear carpera pero si ta existe ya no la va a crear

def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)


app()

