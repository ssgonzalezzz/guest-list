from os import mkdir

def read_archive():
    try:
        with open('archive/list.txt', 'r') as f:
            for line in f:
                print(line, '\n')
    except FileNotFoundError as fnfe:
        input('El archivo no existe. Presione cualquier tecla para continuar')
        return    

def create_file():
    ruta = './file/list.txt'
    try:
        with open(ruta, 'w') as f:
            f.close()
            input(f'Archivo creado en la dirección "{ruta}" satisfactoriamente. Presiona cualquier tecla para continuar')
    except FileNotFoundError:
        mkdir('./file')
        create_file()