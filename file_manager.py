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


def delete_guest(guest_to_delete):
    """
    Elimina un guest del archivo. Utiliza list comprehensions para lograrlo. BORRA TODAS LAS CONCIDENCIAS

    param guest_to_delete string: nombre a eliminar
    """
    try:
        with open('file/list.txt', 'r') as f:
            all_guest = f.readlines()
            f.close()
            if all_guest == []:
                raise Exception('El archivo se encuentra vacio, no es posible realizar la operacion')

        new_list = [name for name in all_guest if name.lower() != (guest_to_delete+'\n').lower()]

        with open('file/list.txt', 'w') as f:
            for name in new_list:
                f.write(name)

        # for name in all_guest:
        #     if name.lower() != (guest_to_delete+'\n').lower():
        #         new_list.append(name)
        

        
        # if new_list != []:
        #     with open('file/list.txt') as f:
        #         for name in new_list:
        #             f.write(name)
        
        # with open('file/list.txt', 'w') as f:
        #     for name in all_guest:                                    Esto borra el archivo. Lo mejor seria crear una lista y que de escriba todo de una vez
        #         if name.lower() != (guest_to_delete+'\n').lower():
        #             print('igual') 
            # print(all_guest)



        input()
    except Exception as ve:
        print(ve)
        input()