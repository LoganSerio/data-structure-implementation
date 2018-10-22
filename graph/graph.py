from vertex import vertex

class graph:

    def __init__(self):
        self.vertices = {}
        self.vertexCount = 0

    def addVertex(self,key):
        newVert = vertex(key)
        self.vertices[key] =  newVert
        self.vertexCount += 1

    def getVertex(self, vertName):
        if vertName in self.vertices:
            return self.vertices[vertName]
        else:
            return None
    
    def __contains__(self,vert):
        return vert in self.vertices

    def addEdge(self,v1,v2,cost):
        if v1 not in self.vertices:
            self.addVertex(v1)
            vertexCount += 1
        if v2 not in self.vertices:
            self.addVertex(v2)
            vertexCount += 1
        self.vertices[v1].addNeighbor(self.vertices[v2],cost)

    def __iter__(self):
        return iter(self.vertices.values())


    
    

#http://interactivepython.org/courselib/static/pythonds/Graphs/Implementation.html