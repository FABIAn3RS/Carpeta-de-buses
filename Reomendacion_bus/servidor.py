from flask import Flask, request, jsonify
from flask_cors import CORS
from procesador import cargar_coordenadas, encontrar_punto_mas_cercano, buscar_grupos_por_claves

app = Flask(__name__)
CORS(app)



@app.route('/coordenadas', methods=['POST'])

def recibir_coordenadas():
    data = request.get_json()
    print("JSON recibido:", data)
    lat = float(data['lat'])
    lon = float(data['lon'])


    puntos = cargar_coordenadas('nombres_final_orden_alfabetico.txt')
    punto_cercano = encontrar_punto_mas_cercano(lat, lon, puntos)
    clave = punto_cercano[0]

    clave_inicial = clave
    clave_extra = "Av. María Auxiliadora"

    grupo = buscar_grupos_por_claves([clave_inicial, clave_extra], 'ruta_cbus.txt')

    print(f"Clave más cercana: {clave}")
    print(f"Coordenadas: ({punto_cercano[1]}, {punto_cercano[2]})")
    if grupo:
        print(f"El bus recomendado para llegar a su destino es la línea/s {grupo}")
    else:
        print("No pertenece a ningún grupo.")

    
    return jsonify({
        'clave': clave,
        'grupo': grupo,  # esto ahora incluirá el número como '1', '2', etc.
        'latitud': punto_cercano[1],
        'longitud': punto_cercano[2]
    })


if __name__ == '__main__':
    app.run(debug=True)
