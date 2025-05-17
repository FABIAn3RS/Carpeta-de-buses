import math

def cargar_coordenadas(nombre_archivo):
    puntos = []
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            linea = linea.strip()
            if not linea:
                continue

            clave, coords = linea.split(':', 1)
            clave = clave.strip()
            lat_str, lon_str = coords.split(',', 1)

            lat = float(lat_str.strip())
            lon = float(lon_str.strip())

            puntos.append((clave, lat, lon))
    return puntos

def distancia(lat1, lon1, lat2, lon2):
    return math.sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2)

def encontrar_punto_mas_cercano(lat, lon, puntos):
    return min(puntos, key=lambda p: distancia(lat, lon, p[1], p[2]))

def buscar_grupos_por_claves(claves, archivo_lugares):
    if isinstance(claves, str):
        claves = [claves]

    grupos = []

    with open(archivo_lugares, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            if ':' not in linea:
                continue

            numero_str, valores_str = linea.split(':', 1)
            numero = numero_str.strip()
            valores = [v.strip() for v in valores_str.split(',') if v.strip()]

            if all(clave in valores for clave in claves):
                grupos.append(numero)

    return (", ".join(grupos))