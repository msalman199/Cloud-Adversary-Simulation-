#!/usr/bin/env python3
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def create_asset_graph():
    """Create a network graph from asset data"""
    
    # Create a new graph
    G = nx.Graph()
    
    # Read our relationship data
    try:
        relationships = pd.read_csv('relationships.csv')
        
        # Add edges to the graph
        for _, row in relationships.iterrows():
            G.add_edge(row['Source'], row['Target'], 
                      relationship=row['Relationship'])
        
        print(f"Graph created with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges")
        
        # Basic graph analysis
        print("\nGraph Analysis:")
        print(f"- Density: {nx.density(G):.3f}")
        print(f"- Connected Components: {nx.number_connected_components(G)}")
        
        # Find central nodes
        centrality = nx.degree_centrality(G)
        most_central = max(centrality, key=centrality.get)
        print(f"- Most connected asset: {most_central}")
        
        # Visualize the graph
        plt.figure(figsize=(12, 8))
        pos = nx.spring_layout(G, k=1, iterations=50)
        
        nx.draw(G, pos, with_labels=True, node_color='lightblue', 
                node_size=1500, font_size=8, font_weight='bold')
        
        plt.title("Cloud Asset Relationship Graph")
        plt.savefig("asset_graph_python.png", dpi=300, bbox_inches='tight')
        print("\nGraph visualization saved as 'asset_graph_python.png'")
        
        return G
        
    except FileNotFoundError:
        print("Error: relationships.csv file not found")
        return None

def export_for_maltego(graph):
    """Export graph data in a format suitable for Maltego import"""
    
    if graph is None:
        return
    
    # Create nodes list
    nodes_data = []
    for node in graph.nodes():
        # Determine entity type based on node characteristics
        if '@' in node:
            entity_type = "Email"
        elif '.' in node and not node.replace('.', '').isdigit():
            entity_type = "Domain"
        elif node.replace('.', '').isdigit():
            entity_type = "IPv4"
        else:
            entity_type = "Phrase"
        
        nodes_data.append({
            'Entity': node,
            'Type': entity_type
        })
    
    # Save nodes data
    nodes_df = pd.DataFrame(nodes_data)
    nodes_df.to_csv('maltego_entities.csv', index=False)
    
    # Create edges list
    edges_data = []
    for edge in graph.edges(data=True):
        edges_data.append({
            'Source': edge[0],
            'Target': edge[1],
            'Relationship': edge[2].get('relationship', 'connected_to')
        })
    
    # Save edges data
    edges_df = pd.DataFrame(edges_data)
    edges_df.to_csv('maltego_relationships.csv', index=False)
    
    print("Data exported for Maltego import:")
    print("- maltego_entities.csv")
    print("- maltego_relationships.csv")

if __name__ == "__main__":
    print("Cloud Asset Graph Analysis Tool")
    print("=" * 40)
    
    # Create and analyze the graph
    asset_graph = create_asset_graph()
    
    # Export data for Maltego
    export_for_maltego(asset_graph)
    
    print("\nAnalysis complete!")
