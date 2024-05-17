def remove_elements(lista):

    if len(lista) == 0:
        return lista
    else:
        del lista[0]

        if len(lista) >= 5:
            del lista[3:5]
            return lista
        elif len(lista) == 4:
            del lista[3]
            return lista
        else:
            return lista
            

def add_elements(agregar):

    agregar.insert(0, 'Pink')
    agregar.append("Yellow")
    return agregar


def is_empty(lista):
    return len(lista) == 0


def list_of_lists(texto):
    fila1 = texto[0][0:2]
    fila2 = texto[1][1:4]
    fila3 = texto[2][-2:]
    return [fila1, fila2, fila3]
