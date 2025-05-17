import osmnx as ox
import networkx as nx
import folium
import webbrowser

# Coordenadas de las 18 paradas (ejemplo en Manta, Ecuador)
paradas = [
    (-0.9714710793618166, -80.63941245698396),  # Parada 1: Colisa
    (-0.9652341272437134, -80.66891029383767),  # Parada 2: Redondel Del Imperio
    (-0.9600209046864329, -80.6724100254931),   # Parada 3: Villamarina
    (-0.9600903909694588, -80.68246086925235),  # Parada 4: Redondel de la Barca
    (-0.9599128536912693, -80.68459883246932),  # Parada 5: Gasolinera Petrovelca
    (-0.9597046213277984, -80.68988228318663),  # Parada 6: Terminal Terrestre
    (-0.9563800068973028, -80.69976275760757),  # Parada 7: Redondel el Paraíso
    (-0.9560739170082108, -80.70439419014049),  # Parada 8: Calle 120
    (-0.9513797084670279, -80.70062745945627),  # Parada 9: Feria de los Esteros
    (-0.9524890075654191, -80.70742258246933),  # Parada 10: Mercado de los Esteros
    (-0.9531989661843628, -80.71157166786125),  # Parada 11: Av. 105
    (-0.9474886237048983, -80.72115408960258),  # Parada 12: Espigón-Megaparque
    (-0.941284798095269, -80.72779876472573),   # Parada 13: Redondel de Portuaria
    (-0.9556143285683611, -80.75224315838418),  # Parada 14: Los Bloques
    (-1.0005241335944663, -80.69459443090749),  # Parada 15: Calle 15
    (-0.9524307426459129, -80.72916866007259),  # Parada 16: Calle 11
    (-0.9492835443149059, -80.72622850363383),  # Parada 17: Mercado Central
    (-0.9557337288020086, -80.72994158363622),  # Parada 18: Colegio Manta
    (-0.9548705117113377, -80.73547841400396),  # Parada 19: Santa Martha
    (-0.9579441044083015, -80.7479631821929),   # Parada 20: Redondel los Bomberos
    (-0.9534112084397054, -80.74572469014038),  # Parada 21: ULEAM
    (-0.9575264245348207, -80.75178939423922),  # Parada 22: Manta 2000
    (-0.960670274270229, -80.6904764175131),    # Parada 23: Terminal de buses
    (-0.9567194982939854, -80.76648952692346),  # Parada 24: Fetum
    (-0.9599591630116278, -80.76675854411411),  # Parada 25: Coliseo Tohallí




   
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
mapa.save("ruta_2_paradas.html")

webbrowser.open("ruta_2_paradas.html")
