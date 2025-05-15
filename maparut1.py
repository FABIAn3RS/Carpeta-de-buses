import osmnx as ox
import networkx as nx
import folium
import webbrowser

# Coordenadas de las 18 paradas (ejemplo en Manta, Ecuador)
paradas = [
    (-0.9612326339519275, -80.69051288618925),  # Parada 1: Terminal
    (-0.9626996514194313, -80.67382825048325),  # Parada 2 manta rocafuerte
    (-0.9701880841066222, -80.67862260000983),  # Parada 3 costa azul
    (-0.9776618797962864, -80.68951047354798),  # Parada 4 pradera
    (-0.9864088206160938, -80.70116076153248),  # Parada 5 15 abril
    (-0.9921535906148865, -80.7055351759579),  # Parada 6 santa ana
    (-0.9676319152326109, -80.66994565541731),  # Parada 7 via circunvalacion 
    (-0.9599580078921426, -80.73197383443245),  # Parada 8 av de la cultura manta
    (-0.9555468926826187, -80.72677448019635),  # Parada 9 5 de junio
    (-0.9538365818952338, -80.72379791483158),  # Parada 10 nuevo tarqui
    (-0.9492881622122972, -80.70349035412217),  # Parada 11 puerto aeropuerto
    (-0.9527871532716368, -80.69353524850197),  # Parada 12 calle 15
    (-0.9491655433032138, -80.72636797926046),  # Parada 13 mercado central
    (-0.9507199443093797, -80.73037416206965),  # Parada 14 av 24
     (-0.9448165354542963, -80.73473125543687),  # Parada 15 av flavio
    (-0.9535296863510054, -80.74659462390211),  # Parada 16av uni
    (-0.9588671564684202, -80.75892827484031),  # Parada 17 gavilanes
    (-0.9591424074531715, -80.80758572233218),  # Parada 17 san mateo




   
]

# Descargar red de calles para autos alrededor de las paradas
G = ox.graph_from_point(paradas[0], dist=20000, network_type='drive')

# Crear un mapa inicial centrado en la primera parada
mapa = folium.Map(location=paradas[0], zoom_start=14)

# Iterar sobre las paradas y calcular rutas consecutivas
for i in range(len(paradas) - 1):
    # Encontrar los nodos más cercanos a las paradas
    nodo_origen = ox.distance.nearest_nodes(G, paradas[i][1], paradas[i][0])
    nodo_destino = ox.distance.nearest_nodes(G, paradas[i + 1][1], paradas[i + 1][0])
    
    # Calcular la ruta más corta (en distancia)
    ruta = nx.shortest_path(G, nodo_origen, nodo_destino, weight='length')
    
    # Obtener coordenadas de la ruta
    coordenadas_ruta = [(G.nodes[n]['y'], G.nodes[n]['x']) for n in ruta]
    
    # Dibujar la ruta en el mapa
    folium.PolyLine(coordenadas_ruta, color='blue', weight=5).add_to(mapa)
    
    # Marcar las paradas
    folium.Marker(paradas[i], popup=f"Parada {i+1}").add_to(mapa)
    
# Marcar la última parada
folium.Marker(paradas[-1], popup=f"Parada {len(paradas)}").add_to(mapa)

# Guardar el resultado
mapa.save("ruta_18_paradas.html")

webbrowser.open("ruta_18_paradas.html")
