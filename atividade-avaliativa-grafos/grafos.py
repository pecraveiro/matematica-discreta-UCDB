import networkx as nx
import matplotlib.pyplot as plt

def criar_grafo():
    grafo = nx.Graph()
    while True:
        vertice = input("Digite um vértice (ou 'fim' para parar): ")
        if vertice.lower() == 'fim':
            break
        grafo.add_node(vertice)
    
    while True:
        aresta = input("Digite uma aresta no formato 'vértice1-vértice2' (ou 'fim' para parar): ")
        if aresta.lower() == 'fim':
            break
        vertice1, vertice2 = aresta.split('-')
        
        if vertice1 in grafo.nodes() and vertice2 in grafo.nodes():
            grafo.add_edge(vertice1, vertice2)
        else:
            print("Erro: Vértices não encontrados. Certifique-se de que ambos os vértices existem no grafo.")

    return grafo

def visualizar_grafo(grafo):
    pos = nx.spring_layout(grafo)
    nx.draw(grafo, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=10, font_color='black')
    plt.title("Grafo Criado")
    plt.show()

def propriedades_grafo(grafo):
    while True:
        print("\nOpções de Propriedades do Grafo:")
        print("1. Visualizar Grafo")
        print("2. Ordem do Grafo")
        print("3. Tamanho do Grafo")
        print("4. Grau Médio do Grafo")
        print("5. Conectividade do Grafo")
        print("6. Bipartição do Grafo")
        print("7. Árvore do Grafo")
        print("8. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            visualizar_grafo(grafo)
        elif escolha == "2":
            print(f"Ordem do Grafo: {len(grafo.nodes())}")
        elif escolha == "3":
            print(f"Tamanho do Grafo: {len(grafo.edges())}")
        elif escolha == "4":
            grau_medio = sum(dict(grafo.degree()).values()) / len(grafo.nodes())
            print(f"Grau Médio do Grafo: {grau_medio}")
        elif escolha == "5":
            if nx.is_connected(grafo):
                print("O grafo é conexo.")
            else:
                print("O grafo não é conexo.")
        elif escolha == "6":
            if nx.is_bipartite(grafo):
                print("O grafo é bipartido.")
            else:
                print("O grafo não é bipartido.")
        elif escolha == "7":
            if nx.is_tree(grafo):
                print("O grafo é uma árvore.")
            else:
                print("O grafo não é uma árvore.")
        elif escolha == "8":
            break
        else:
            print("Opção inválida. Tente novamente.")

def main():
    print("Criação e Propriedades de um Grafo")
    grafo = criar_grafo()
    
    print("\nGrafo Criado:")
    for vertice, vizinhos in grafo.adjacency():
        print(f"Vértice {vertice}: Arestas para {', '.join(vizinhos)}")

    propriedades_grafo(grafo)

if __name__ == "__main__":
    main()
