class Graph :
    def __init__(self):
        self.graph = {}     # dictionary to store vertices and edges
        self.BSFsearch = []     # list to store BSF vertex list
        self.DSFsearch = []     # list to store DSF vertex list

    def add_vertex(self, vertex):
        if vertex not in self.graph :
            self.graph[vertex] = []     # vertex : key,  array of corresponding vertices : value
        else:
            print("Vertex " + vertex + " already present in graph.")

    def add_edge(self, vertex1, vertex2):
        if vertex1 and vertex2 in self.graph :
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)
        else:
            print("These pair of vertex not present in graph.")

    def BSF(self, vertex):
        if vertex not in self.BSFsearch :
            self.BSFsearch.append(vertex)           # append vertex to list

        adjacentVertexList = self.graph[vertex]
        newAdjacentVertexList = []
        for j in adjacentVertexList:
            if j not in self.BSFsearch:
                newAdjacentVertexList.append(j)     # to avoid edge's vertex repeat ambiguity

        for i in adjacentVertexList :
            if i not in self.BSFsearch :
                self.BSFsearch.append(i)

        for i in newAdjacentVertexList :
            if i in self.BSFsearch :
                self.BSF(i)             # exlopre a vertex then move to next vertex

    def displayBSF(self):
        print("BSF order - ")
        for i in self.BSFsearch:
            print(i, end=", ")

        print()
        print("Vertices and adges - ", end=" ")
        print(self.graph)

    def DSF(self, vertex):
        if vertex not in self.DSFsearch :
            self.DSFsearch.append(vertex)           # append vertex to list

        adjacentVertexList = self.graph[vertex]
        newAdjacentVertexList = []

        for j in adjacentVertexList:
            if j not in self.DSFsearch:
                newAdjacentVertexList.append(j)     # to avoid edge's vertex repeat ambiguity

        for i in newAdjacentVertexList :
            self.DSF(i)             # exlopre a vertex till it ends then return to earlier vertex

    def displayDSF(self):
        print("DSF order - ")
        for i in self.DSFsearch:
            print(i, end=", ")

        print()
        print("Vertices and adges - ", end=" ")
        print(self.graph)

g=Graph();
while (True) :
    print("Menu")
    print("1. Add vertices\n2. Add edges\n3. Perform BSF\n4. Perform DSF")
    choice = int(input("Enter choice - "))
    if(choice==1):
        n = int(input("Enter total number of vertices - "))
        for i in range(0,n):
            a = int(input("Vertex - "))
            g.add_vertex(a)
    elif (choice==2) :
        v1 = int(input("Enter vertex 1 of edge - "))
        v2 = int(input("Enter vertex 2 of edge - "))
        g.add_edge(v1,v2)
    elif (choice==3) :
        g.BSF(1)
        g.displayBSF()
    elif (choice==4) :
        g.DSF(1)
        g.displayDSF()
    else :
        break