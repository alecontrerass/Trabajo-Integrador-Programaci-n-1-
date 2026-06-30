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


# Filtros y orden
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


# Estadisticas
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
