'''
  File: Graph.py

  Description: A16 graph traversal

  Student's Name: Rohan Chaudhry

  Student's UT EID: rc43755

  Partner's Name: Daniel Snyder

  Partner's UT EID: djs3928

  Course Name: CS 313E

  Unique Number:  51335

  Date Created: 25 apr

  Date Last Modified: 27 apr
'''


class Stack(object):
    def __init__(self):
        self.stack = []

    # add an item to the top of the stack
    def push(self, item):
        self.stack.append(item)

    # remove an item from the top of the stack
    def pop(self):
        return self.stack.pop()

    # check what item is on top of the stack without removing it
    def peek(self):
        return self.stack[len(self.stack) - 1]

    # check if a stack is empty
    def isEmpty(self):
        return (len(self.stack) == 0)

    # return the number of elements in the stack
    def size(self):
        return (len(self.stack))


class Queue(object):
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return (self.queue.pop(0))

    def isEmpty(self):
        return (len(self.queue) == 0)

    def size(self):
        return len(self.queue)


class Vertex(object):
    def __init__(self, label):
        self.label = label
        self.visited = False

    # determine if a vertex was visited
    def wasVisited(self):
        return self.visited

    # determine the label of the vertex
    def getLabel(self):
        return self.label

    # string representation of the vertex
    def __str__(self):
        return str(self.label)

class Edge(object):
    def __init__(self, fromV, toV, weight):
        self.fromV = fromV
        self.toV = toV
        self.weight = weight




class Graph(object):
    def __init__(self):
        self.Vertices = []
        self.adjMat = []
        self.Edges = []

    # check if a vertex already exists in the graph
    def hasVertex(self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (label == (self.Vertices[i]).label):
                return True
        return False

    # given a label get the index of a vertex
    def getIndex(self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if ((self.Vertices[i]).label == label):
                return i
        return -1

    # add a Vertex with a given label to the graph
    def addVertex(self, label):
        if not self.hasVertex(label):
            self.Vertices.append(Vertex(label))

            # add a new column in the adjacency matrix for the new Vertex
            nVert = len(self.Vertices)
            for i in range(nVert - 1):
                (self.adjMat[i]).append(0)

            # add a new row for the new Vertex in the adjacency matrix
            newRow = []
            for i in range(nVert):
                newRow.append(0)
            self.adjMat.append(newRow)

    # add weighted directed edge to graph
    def addDirectedEdge(self, start, finish, weight=1):
        self.adjMat[start][finish] = weight

    # add weighted undirected edge to graph
    def addUndirectedEdge(self, start, finish, weight=1):
        self.adjMat[start][finish] = weight
        self.adjMat[finish][start] = weight

    # return an unvisited vertex adjacent to vertex v
    def getAdjUnvisitedVertex(self, v):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).wasVisited()):
                return i
        return -1

    # do the depth first search in a graph
    def dfs(self, v):
        # create a Stack
        theStack = Stack()

        # mark vertex v as visited and push on the stack
        (self.Vertices[v]).visited = True
        print(self.Vertices[v])
        theStack.push(v)

        # vist other vertices according to depth
        while (not theStack.isEmpty()):
            # get an adjacent unvisited vertex
            u = self.getAdjUnvisitedVertex(theStack.peek())
            if (u == -1):
                u = theStack.pop()
            else:
                (self.Vertices[u]).visited = True
                print(self.Vertices[u])
                theStack.push(u)
        # the stack is empty let us reset the falgs
        nVert = len(self.Vertices)
        for i in range(nVert):
            (self.Vertices[i]).visited = False

    # do breadth first search in a graph
    def bfs(self, v):
        # create a Queue
        theQueue = Queue()
        (self.Vertices[v]).visited = True   # all vertices are visited

        print(self.Vertices[v])

        theQueue.enqueue(v)   # source node is visited, enqueue

        while (not theQueue.isEmpty()): # while not empty

            v1 = theQueue.dequeue() #
            # print(v, end= ' ')

            v2 = self.getAdjUnvisitedVertex(v1)


            # get all adjacent vertices of dequeued vertex
            # if not visited, mark as visited then enqueue
            while v2 != -1:
                (self.Vertices[v2]).visited = True
                print(self.Vertices[v2])
                theQueue.enqueue(v2)
                v2 = self.getAdjUnvisitedVertex(v1)


    # get edge weight between two vertices
    # return -1 if edge does not exist
    def getEdgeWeight(self, fromVertexLabel, toVertexLabel):

        from_label = self.getIndex(fromVertexLabel)
        to_label = self.getIndex(toVertexLabel)

        if self.adjMat[from_label][to_label] != 0:
            return self.adjMat[from_label][to_label]
        return -1

    # get a list of immediate neighbors that you can go to from a vertex
    # return empty list if there are none
    def getNeighbors(self, vertexLabel):
        neighbors = []
        idx = self.getIndex(vertexLabel)
        # fill list if immediate neighbors are present
        for i in range (len(self.adjMat[idx])):
            if self.adjMat[idx][i] != 0:
                neighbors.append(self.Vertices[i])

        return neighbors # will remain empty if no neighbors

     # get a copy of the list of vertices
    def getVertices(self):
        return self.Vertices[:]



     # delete an edge from the adjacency matrix
    # graph is initialzied with empty edges
    def deleteEdge(self, fromVertexLabel, toVertexLabel):
        for edge in self.Edges:
            if (edge.fromV.label == fromVertexLabel) and (edge.toV.label == toVertexLabel):
                self.Edges.remove(edge)
        # Change value in adjacency matrix to 0
        i = self.getIndex(fromVertexLabel)
        j = self.getIndex(toVertexLabel)
        self.adjMat[i][j] = 0
        self.adjMat[j][i] = 0  # added this


        #return self.Edges



     # delete a vertex from the vertex list and all edges from and
     # to it in the adjacency matrix
    def deleteVertex(self, vertexLabel):
        # Remove row and column of a vertex
        idx = self.getIndex(vertexLabel)
        vertices = len(self.Vertices)
        for i in range(vertices):
            self.adjMat[i].remove(self.adjMat[i][idx])
        self.adjMat.remove(self.adjMat[idx])

        # Deleting all edges associated with the vertex from list of edges
        dup = self.Edges[:]
        self.Edges = []
        for edge in dup:
            if (edge.fromV.label != vertexLabel) and (edge.toV.label != vertexLabel):
                self.Edges.append(edge)

        # Deleting the vertex for list of vertices
        del self.Vertices[idx]


        #return


def main():
    # create a Graph object
    cities = Graph()

    # open file for reading
    inFile = open("./graph.txt", "r")

    # read the Vertices
    numVertices = int((inFile.readline()).strip())
    print(numVertices)

    for i in range(numVertices):
        city = (inFile.readline()).strip()
        print(city)
        cities.addVertex(city)

    # read the edges
    numEdges = int((inFile.readline()).strip())
    print(numEdges)

    for i in range(numEdges):
        edge = (inFile.readline()).strip()
        print(edge)
        edge = edge.split()
        start = int(edge[0])
        finish = int(edge[1])
        weight = int(edge[2])

        # print('\hello pls pay attention')  # I forgot to comment these out lmaoooooooo
        # print(edge)
        # print()

        cities.addDirectedEdge(start, finish, weight)

    # print the adjacency matrix
    print("\nAdjacency Matrix")
    for i in range(numVertices):
        for j in range(numVertices):
            print(cities.adjMat[i][j], end=' ')
        print()
    print()

    # read the starting vertex for dfs and bfs
    startVertex = (inFile.readline()).strip()
    print(startVertex)
    # close file
    inFile.close()



    cities1 = cities



    # get the index of the start Vertex
    startIndex = cities.getIndex(startVertex)
    print(startIndex)

    # do depth first search
    print("\nDepth First Search from " + startVertex)
    cities.dfs(startIndex)
    print()

    # do breadth first search
    print("\nBreadth First Search from " + startVertex)
    cities.bfs(startIndex)
    print()


    # print out adjacency matrix to show the deletion was correct
    # delete both ways
    # delete an edge



    # this did not delete an edge orginally

    all_cities = cities.getVertices()
    begin = str(all_cities[0])
    end = str(all_cities[1])

    print('delete edge from ' + begin + ' to ' + end)


    cities1.deleteEdge(begin, end)
    print("\nAdjacency Matrix")
    for i in range(numVertices):
        for j in range(numVertices):
            print(cities1.adjMat[i][j], end=' ')
        print()
    print()


    # delete a vertex

    print("Remove vertex Miami")
    cities1.deleteVertex('Miami')

    print("\nAdjacency Matrix")
    for i in range(numVertices - 1):
        for j in range(numVertices - 1):
            print(cities1.adjMat[i][j], end=' ')
        print()
    print()






#if __name__ == "__main__":
main()


