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
        with open(ruta, mode="r", encoding="utf-8", newline="") as archivo:
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
