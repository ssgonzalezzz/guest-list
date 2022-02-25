from os import system, mkdir

def run():
    while True:
        system('clear')
        print(
            """Hola, bienvenido a la creación de la lista de invitados. Eliga una opción:

1. Crear nuevo archivo (borrará la lista anterior).
2. Agregar un nuevo nombre.
3. Mostrar lista de invitados.
4. Salir

            """
        )
        try:
            value = int(input('Elige tu opción: '))
        except ValueError:
            print('La opción debe ser un numero válido')
            input('\nPresiona cualquier tecla para continuar')
            system('clear')
            continue
        
        if value == 4:
            system('clear')
            break
        elif value == 3:
            read_archive()
        elif value == 1:
            create_file()
        

def read_archive():
    try:
        with open('archive/list.txt', 'r') as f:
            for line in f:
                print(line, '\n')
    except FileNotFoundError as fnfe:
        print('El archivo no existe. Presione cualquier tecla para continuar')
        input()
        return    

def create_file():
    with open('archive/list.txt', 'w') as f:
        f.close()

if __name__ == '__main__':
    run()