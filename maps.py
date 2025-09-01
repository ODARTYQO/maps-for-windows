import osmnx as ox
import matplotlib.pyplot as plt

# הורדת גרף רחובות
graph = ox.graph_from_place("Tel Aviv, Israel", network_type='drive')

# ציור הגרף
fig, ax = ox.plot_graph(graph, show=False, close=False)

# הוספת שמות רחובות
for u, v, key, data in graph.edges(keys=True, data=True):
    if 'name' in data:
        x = (graph.nodes[u]['x'] + graph.nodes[v]['x']) / 2
        y = (graph.nodes[u]['y'] + graph.nodes[v]['y']) / 2
        ax.text(x, y, data['name'], fontsize=6, color='blue')

plt.show()
