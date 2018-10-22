class vertex:
    
    def __init__(self,key):
        self.key = key
        self.neighbors = {}
    
    def addNeighbor(self, newNeighborName, weight):
        self.neighbors[newNeighborName] = weight
    
    def getConnections(self):
        return self.neighbors.keys()
    
    def getKey(self):
        return self.key

    def getWeight(self,targetNeighbor):
        weight = self.neighbors[targetNeighbor]
        if not weight:
            raise Exception('Provided target neighbor is not a neighbor of this vertex')
        return weight

    def __str__(self):
        return str(self.key) + " is connected to " + str([nbr.key for nbr in self.neighbors])