from os import mkdir

def read_archive():
    try:
        with open('file/list.txt', 'r') as f:
            for line in f:
                print(f'{line}')
            input('FIN')
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

def add_guest(name):
    try:
        with open('./file/list.txt', 'a', encoding='utf-8') as f:
            f.write(f'{name}\n')
            f.close()
    except FileNotFoundError:
        opt = input('Archivo no existe. Desea crearlo y agregar el nombre?. Y/N')
        if opt.lower() == 'y':
            create_file()
            add_guest(name)
        else:
            return
