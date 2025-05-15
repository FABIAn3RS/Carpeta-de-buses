import folium
import networkx as nx
import osmnx as ox
import webbrowser

# Coordenadas de origen y destino (CDMX por ejemplo)
parada1 = (-0.9612326339519275, -80.69051288618925)  # terminal
parada2 = (-0.9713656366906177, -80.64530814832925)  # Bellas Artes

# Descargar red de calles para autos
G = ox.graph_from_point(parada1, dist=19999, network_type='drive')

# Encontrar los nodos más cercanos
nodo_parada1 = ox.distance.nearest_nodes(G, parada1[1], parada1[0])
nodo_parada2 = ox.distance.nearest_nodes(G, parada2[1], parada2[0])

# Calcular ruta más corta (en distancia)
ruta = nx.shortest_path(G, nodo_parada1, nodo_parada2, weight='length')

# Obtener coordenadas de la ruta
coordenadas_ruta = [(G.nodes[n]['y'], G.nodes[n]['x']) for n in ruta]

# Crear el mapa
mapa = folium.Map(location=parada1, zoom_start=15)

# Dibujar la ruta
folium.PolyLine(coordenadas_ruta, color='blue', weight=5).add_to(mapa)

# Marcar inicio y fin
folium.Marker(parada1, popup="Inicio").add_to(mapa)
folium.Marker(parada2, popup="Destino").add_to(mapa)

# Guardar el resultado
mapa.save("ruta_linea1.html")

webbrowser.open("ruta_linea1.html")