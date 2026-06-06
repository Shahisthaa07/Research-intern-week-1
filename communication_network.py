import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_edges_from([
    ("Sensor_1", "Gateway"),
    ("Gateway", "Router"),
    ("Router", "Server"),
    ("Gateway", "Monitor"),
    ("Monitor", "Server")
])

plt.figure(figsize=(6,4))

nx.draw(
    G,
    with_labels=True,
    node_size=2200,
    font_size=10
)

plt.title("Communication Network Topology")
plt.savefig("communication_network.png")
plt.show()

print("Total Nodes:", G.number_of_nodes())
print("Total Connections:", G.number_of_edges())
