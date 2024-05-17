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


def check_lists(uno, dos):

    if len(uno) >= 3 and len(dos) >= 3:
        return (uno[2] == dos[2])
    else:
        return False


def list_of_lists(txt):
    fila1 = txt[0][0:2]
    fila2 = txt[1][1:4]
    fila3 = txt[2][-2:]
    return [fila1, fila2, fila3]
