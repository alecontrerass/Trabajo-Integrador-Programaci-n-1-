def pedir_texto_no_vacio(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor != "":
            return valor
        print("Error: el campo no puede estar vacio. Intente nuevamente.")


def pedir_entero_positivo(mensaje):
    while True:
        entrada = input(mensaje).strip()
        try:
            numero = int(entrada)
            if numero <= 0:
                print("Error: el valor debe ser un numero entero positivo.")
                continue
            return numero
        except ValueError:
            print("Error: debe ingresar un numero entero valido.")


def pedir_entero_opcional(mensaje):
    entrada = input(mensaje).strip()
    if entrada == "":
        return None
    try:
        return int(entrada)
    except ValueError:
        print("Valor invalido, se ignorara este limite.")
        return None
