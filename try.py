import time
import graphviz

def sort_merge(edges):
    degrees = {}
    for e in edges:
        for v in e:
            if v not in degrees:
                degrees[v] = 0
            degrees[v] += 1
    sorted_vertices = sorted(degrees, key=degrees.get, reverse=True)
    print(sorted_vertices)

mass_help=[]
elem={}
Factor = True
with open("list.txt", 'r') as file:
    graph_data = graphviz.Graph()
    graph = []
    graph_data_mod = graphviz.Graph()
    graph_mod = []
    const = 0
    while (const == 0):
        tops = file.readline()
        top = tops.split()
        if len(top) == 2:
            graph_data.edge(top[0],top[1])
            graph.append(top)
        elif len(top) == 1:
            graph_data.node(top[0])
            graph.append(top)
        else:
            const = 1
    print(graph)
    file.close()

unique_vertices = set([v for sublist in graph for v in sublist])
while (Factor == True):  
    print("Enter top to delete:")
    top_to_remove = input()
    if (top_to_remove in unique_vertices):
        Factor=False


with open("list.txt", 'r') as file:
    const = 0
    start_time = time.time()
    while (const == 0):
        mass = []
        tops = file.readline()
        top = tops.split()
        if (len(top) == 2 and top[0]!=top_to_remove and top[1]!=top_to_remove):
            graph_data_mod.edge(top[0],top[1])
            graph_mod.append(top)
        elif (len(top) == 2 and top[0] == top_to_remove and top[1] != top_to_remove):
            mass = top[1]
            graph_data_mod.node(mass)
            graph_mod.append(mass)
            mass_help.append(top[1])
        elif (len(top) == 2 and top[0] != top_to_remove and top[1] == top_to_remove):
            mass = top[0]
            graph_data_mod.node(mass)
            graph_mod.append(mass)
        elif (len(top) == 1 and top[0] != top_to_remove):
            graph_data_mod.node(top[0])
            graph_mod.append(top)
        elif (len(top) == 2 and top[0]==top_to_remove and top[1]==top_to_remove):
            continue
        elif (len(top) == 1 and top[0] == top_to_remove):
            continue
        elif (not tops):
            const = 1
    file.close()

sort_merge(graph_mod)
end_time = time.time()
time_taken = end_time - start_time
print(graph_data_mod)
print(time_taken)
