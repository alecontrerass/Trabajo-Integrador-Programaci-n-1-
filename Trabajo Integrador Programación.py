import csv
import os

nombre_archivo = "paises.csv"
columnas = ["nombre", "poblacion", "superficie", "continente"]


def cargar_paises(ruta=nombre_archivo):
    paises = []

    if not os.path.exists(ruta):
        print(f"Aviso: No se encontro el archivo '{ruta}'. Se iniciara con una lista vacia.")
        return paises
    try:
        with open(ruta, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            if lector.fieldnames != columnas:
                print("Error: el archivo CSV no tiene el formato esperado (columnas incorrectas).")
                return paises

            for fila_numero, fila in enumerate(lector, start=2):
                pais = _convertir_fila_a_pais(fila, fila_numero)
                if pais is not None:
                    paises.append(pais)

    except Exception as error:
        print(f"Error al leer el archivo CSV: {error}")

    return paises


def _convertir_fila_a_pais(fila, numero_fila):
    try:
        nombre = fila["nombre"].strip()
        poblacion = int(fila["poblacion"])
        superficie = int(fila["superficie"])
        continente = fila["continente"].strip()

        if nombre == "" or continente == "":
            print(f"Aviso: fila {numero_fila} descartada por tener campos vacios.")
            return None

        return {
            "nombre": nombre,
            "poblacion": poblacion,
            "superficie": superficie,
            "continente": continente,
        }

    except (ValueError, KeyError):
        print(f"Aviso: fila {numero_fila} descartada por formato invalido.")
        return None


def guardar_paises(paises, ruta=nombre_archivo):
    try:
        with open(ruta, mode="w", encoding="utf-8", newline="") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=columnas)
            escritor.writeheader()
            for pais in paises:
                escritor.writerow(pais)
        return True

    except Exception as error:
        print(f"Error al guardar el archivo CSV: {error}")
        return False


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


def existe_pais(paises, nombre):
    nombre_normalizado = nombre.lower()
    for pais in paises:
        if pais["nombre"].lower() == nombre_normalizado:
            return True
    return False


def agregar_pais(paises, nombre, poblacion, superficie, continente):
    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente,
    }
    paises.append(nuevo_pais)
    return paises


def actualizar_pais(paises, nombre, nueva_poblacion, nueva_superficie):
    nombre_normalizado = nombre.lower()
    for pais in paises:
        if pais["nombre"].lower() == nombre_normalizado:
            pais["poblacion"] = nueva_poblacion
            pais["superficie"] = nueva_superficie
            return True
    return False


def buscar_por_nombre(paises, texto_busqueda):
    texto_normalizado = texto_busqueda.lower()
    resultado = []
    for pais in paises:
        if texto_normalizado in pais["nombre"].lower():
            resultado.append(pais)
    return resultado


def filtrar_por_continente(paises, continente):
    continente_normalizado = continente.lower()
    resultado = []
    for pais in paises:
        if pais["continente"].lower() == continente_normalizado:
            resultado.append(pais)
    return resultado


def filtrar_por_rango_poblacion(paises, minimo, maximo):
    resultado = []
    for pais in paises:
        if minimo is not None and pais["poblacion"] < minimo:
            continue
        if maximo is not None and pais["poblacion"] > maximo:
            continue
        resultado.append(pais)
    return resultado


def filtrar_por_rango_superficie(paises, minimo, maximo):
    resultado = []
    for pais in paises:
        if minimo is not None and pais["superficie"] < minimo:
            continue
        if maximo is not None and pais["superficie"] > maximo:
            continue
        resultado.append(pais)
    return resultado


def ordenar_paises(paises, clave, descendente=False):
    return sorted(paises, key=lambda pais: pais[clave], reverse=descendente)


def pais_mayor_poblacion(paises):
    return max(paises, key=lambda pais: pais["poblacion"])


def pais_menor_poblacion(paises):
    return min(paises, key=lambda pais: pais["poblacion"])


def promedio_poblacion(paises):
    total = sum(pais["poblacion"] for pais in paises)
    return total / len(paises)


def promedio_superficie(paises):
    total = sum(pais["superficie"] for pais in paises)
    return total / len(paises)


def cantidad_por_continente(paises):
    conteo = {}
    for pais in paises:
        continente = pais["continente"]
        conteo[continente] = conteo.get(continente, 0) + 1
    return conteo


def mostrar_menu():
    print(" Sistema de Gestion de Paises")
    print("1. Agregar pais")
    print("2. Actualizar poblacion y superficie")
    print("3. Buscar pais por nombre")
    print("4. Filtrar paises")
    print("5. Ordenar paises")
    print("6. Mostrar estadisticas")
    print("7. Listar todos los paises")
    print("0. Salir")



def mostrar_pais(pais):
    print(f"- {pais['nombre']:<15} | Poblacion: {pais['poblacion']:>12,} | "
          f"Superficie: {pais['superficie']:>10,} km2 | Continente: {pais['continente']}")


def mostrar_lista_paises(lista_paises):
    if len(lista_paises) == 0:
        print("No se encontraron paises con esos criterios.")
        return
    for pais in lista_paises:
        mostrar_pais(pais)


def opcion_agregar_pais(paises):
    print("\n--- Agregar nuevo pais ---")
    nombre = pedir_texto_no_vacio("Nombre del pais: ")

    if existe_pais(paises, nombre):
        print(f"Error: ya existe un pais llamado '{nombre}'.")
        return

    poblacion = pedir_entero_positivo("Poblacion: ")
    superficie = pedir_entero_positivo("Superficie (km2): ")
    continente = pedir_texto_no_vacio("Continente: ")

    agregar_pais(paises, nombre, poblacion, superficie, continente)
    print(f"Pais '{nombre}' agregado correctamente.")


def opcion_actualizar_pais(paises):
    print("\n--- Actualizar pais ---")
    nombre = pedir_texto_no_vacio("Nombre del pais a actualizar: ")

    if not existe_pais(paises, nombre):
        print(f"Error: no existe ningun pais llamado '{nombre}'.")
        return

    nueva_poblacion = pedir_entero_positivo("Nueva poblacion: ")
    nueva_superficie = pedir_entero_positivo("Nueva superficie (km2): ")

    actualizar_pais(paises, nombre, nueva_poblacion, nueva_superficie)
    print(f"Pais '{nombre}' actualizado correctamente.")


def opcion_buscar_pais(paises):
    print("\n--- Buscar pais por nombre ---")
    texto = pedir_texto_no_vacio("Ingrese nombre o parte del nombre: ")
    resultado = buscar_por_nombre(paises, texto)
    mostrar_lista_paises(resultado)


def opcion_filtrar_paises(paises):
    print("\n--- Filtrar paises ---")
    print("1. Por continente")
    print("2. Por rango de poblacion")
    print("3. Por rango de superficie")
    sub_opcion = input("Elija una opcion: ").strip()

    if sub_opcion == "1":
        continente = pedir_texto_no_vacio("Continente: ")
        resultado = filtrar_por_continente(paises, continente)
        mostrar_lista_paises(resultado)

    elif sub_opcion == "2":
        print("Deje vacio y presione Enter si no quiere limitar ese valor.")
        minimo = pedir_entero_opcional("Poblacion minima: ")
        maximo = pedir_entero_opcional("Poblacion maxima: ")
        resultado = filtrar_por_rango_poblacion(paises, minimo, maximo)
        mostrar_lista_paises(resultado)

    elif sub_opcion == "3":
        print("Deje vacio y presione Enter si no quiere limitar ese valor.")
        minimo = pedir_entero_opcional("Superficie minima: ")
        maximo = pedir_entero_opcional("Superficie maxima: ")
        resultado = filtrar_por_rango_superficie(paises, minimo, maximo)
        mostrar_lista_paises(resultado)

    else:
        print("Error: opcion invalida.")


def opcion_ordenar_paises(paises):
    print("\n--- Ordenar paises ---")
    print("1. Por nombre")
    print("2. Por poblacion")
    print("3. Por superficie")
    sub_opcion = input("Elija una opcion: ").strip()

    claves = {"1": "nombre", "2": "poblacion", "3": "superficie"}
    if sub_opcion not in claves:
        print("Error: opcion invalida.")
        return

    orden = input("Orden (A = ascendente, D = descendente): ").strip().lower()
    descendente = (orden == "d")

    resultado = ordenar_paises(paises, claves[sub_opcion], descendente)
    mostrar_lista_paises(resultado)


def opcion_mostrar_estadisticas(paises):
    print("\n Estadisticas generales ")
    if len(paises) == 0:
        print("No hay paises cargados para calcular estadisticas.")
        return

    mayor = pais_mayor_poblacion(paises)
    menor = pais_menor_poblacion(paises)
    promedio_pob = promedio_poblacion(paises)
    promedio_sup = promedio_superficie(paises)
    conteo = cantidad_por_continente(paises)

    print(f"Pais con mayor poblacion: {mayor['nombre']} ({mayor['poblacion']:,} habitantes)")
    print(f"Pais con menor poblacion: {menor['nombre']} ({menor['poblacion']:,} habitantes)")
    print(f"Promedio de poblacion: {promedio_pob:,.2f} habitantes")
    print(f"Promedio de superficie: {promedio_sup:,.2f} km2")
    print("Cantidad de paises por continente:")
    for continente, cantidad in conteo.items():
        print(f"  - {continente}: {cantidad}")


def main():
    print("Cargando dataset de paises desde paises.csv ...")
    paises = cargar_paises()
    print(f"Se cargaron {len(paises)} paises correctamente.")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            opcion_agregar_pais(paises)
        elif opcion == "2":
            opcion_actualizar_pais(paises)
        elif opcion == "3":
            opcion_buscar_pais(paises)
        elif opcion == "4":
            opcion_filtrar_paises(paises)
        elif opcion == "5":
            opcion_ordenar_paises(paises)
        elif opcion == "6":
            opcion_mostrar_estadisticas(paises)
        elif opcion == "7":
            print("\n--- Listado completo de paises ---")
            mostrar_lista_paises(paises)
        elif opcion == "0":
            if guardar_paises(paises):
                print("Cambios guardados en paises.csv.")
            else:
                print("Hubo un problema al guardar los cambios.")
            break
        else:
            print("Error: opcion invalida. Intente nuevamente.")


if __name__ == "__main__":
    main()


