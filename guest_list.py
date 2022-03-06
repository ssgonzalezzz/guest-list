from os import system
from file_manager import *

def run():
    while True:
        system('clear')
        print(
            """Hola, bienvenido a la creación de la lista de invitados. Eliga una opción:

1. Crear nuevo archivo (borrará la lista anterior).
2. Agregar un nuevo nombre.
3. Mostrar lista de invitados.
4. Eliminar un invitado
5. Salir

            """
        )
        try:
            value = int(input('Elige tu opción: '))
        except ValueError:
            print('La opción debe ser un numero válido')
            input('\nPresiona cualquier tecla para continuar')
            system('clear')
            continue
        
        if value == 5:
            system('clear')
            break
        elif value == 3:
            system('clear')
            read_archive()
        elif value == 1:
            system('clear')
            create_file()
        elif value ==2:
            system('clear')
            name = input('Nombre a agregar: ')
            add_guest(name)
        elif value ==4:
            system('clear')
            name = input('Nombre a eliminar: ')
           
        

if __name__ == '__main__':
    run()