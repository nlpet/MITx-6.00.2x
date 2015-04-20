# 6.00.2x Problem Set 5
# Graph optimization
#
# A set of data structures to represent graphs
#

class Node(object):
    def __init__(self, name):
        self.name = str(name)
    def getName(self):
        return self.name
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    def __eq__(self, other):
        return self.name == other.name
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        # Override the default hash method
        # Think: Why would we want to do this?
        return self.name.__hash__()

class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return '{0}->{1}'.format(self.src, self.dest)


class WeightedEdge(Edge):
    def __init__(self, src, dest, dist, outDist):
        self.src = src
        self.dest = dest
        self.dist = dist
        self.outDist = outDist

    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dest

    def getTotalDistance(self):
        return self.dist

    def getOutdoorDistance(self):
        return self.outDist

    def __str__(self):
        return '{0}->{1} ({2}, {3})'.format(self.src, self.dest, self.dist, self.outDist)


class Digraph(object):
    """
    A directed graph
    """
    def __init__(self):
        # A Python Set is basically a list that doesn't allow duplicates.
        # Entries into a set must be hashable (where have we seen this before?)
        # Because it is backed by a hashtable, lookups are O(1) as opposed to the O(n) of a list (nifty!)
        # See http://docs.python.org/2/library/stdtypes.html#set-types-set-frozenset
        self.nodes = set([])
        self.edges = {}
    def addNode(self, node):
        if node in self.nodes:
            # Even though self.nodes is a Set, we want to do this to make sure we
            # don't add a duplicate entry for the same node in the self.edges list.
            # raise ValueError('Duplicate node')
            pass
        else:
            self.nodes.add(node)
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = '{0}{1}->{2}\n'.format(res, k, d)
        return res[:-1]


class WeightedDigraph(Digraph):
    def __init__(self):
        Digraph.__init__(self)
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        dist = edge.getTotalDistance()
        outDist = edge.getOutdoorDistance()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError("Node not in graph")
        self.edges[src].append([dest,(dist,outDist)])

    def childrenOf(self,node):
        return [k[0] for k in self.edges[node]]
    def __str__(self):
        res = ''
        for k in self.edges:
            for l in self.edges[k]:
                res = '{0}{1}->{2} ({3}, {4})\n'.format(res,k,l[0],float(l[1][0]),float(l[1][1]))
        return res[:-1]




def test():
    g = WeightedDigraph()
    na = Node('a')
    nb = Node('b')
    nc = Node('c')
    nd = Node('d')
    ne = Node('e')
    nf = Node('f')
    g.addNode(na)
    g.addNode(nb)
    g.addNode(nc)
    g.addNode(nd)
    g.addNode(ne)
    g.addNode(nf)
    e1 = WeightedEdge(na,nb,15,10)
    e2 = WeightedEdge(na,nc,14,6)
    e3 = WeightedEdge(nb,nc,10,9)
    e4 = WeightedEdge(nc,nd,15,13)
    e5 = WeightedEdge(nb,ne,15,14)
    e6 = WeightedEdge(ne,nf,13,2)
    e7 = WeightedEdge(nd,nf,16,3)
    e8 = WeightedEdge(nc,nb,10,9)
    e9 = WeightedEdge(nd,nc,15,13)
    g.addEdge(e1)
    g.addEdge(e2)
    g.addEdge(e3)
    g.addEdge(e4)
    g.addEdge(e5)
    g.addEdge(e6)
    g.addEdge(e7)
    g.addEdge(e8)
    g.addEdge(e9)
    print g


def test2():
    g = Digraph()
    na = Node('a')
    nb = Node('b')
    nc = Node('c')
    nd = Node('d')
    ne = Node('e')
    nf = Node('f')
    g.addNode(na)
    g.addNode(nb)
    g.addNode(nc)
    g.addNode(nd)
    g.addNode(ne)
    g.addNode(nf)
    e1 = Edge(na,nb)
    e2 = Edge(na,nc)
    e3 = Edge(nb,nc)
    e4 = Edge(nc,nd)
    e5 = Edge(nb,ne)
    e6 = Edge(ne,nf)
    e7 = Edge(nd,nf)
    e8 = Edge(nc,nb)
    e9 = Edge(nd,nc)
    g.addEdge(e1)
    g.addEdge(e2)
    g.addEdge(e3)
    g.addEdge(e4)
    g.addEdge(e5)
    g.addEdge(e6)
    g.addEdge(e7)
    g.addEdge(e8)
    g.addEdge(e9)
    print g

'''
print 'Testing WeightedDigraph'
test()
print 'Testing Digraph'
test2()
print 'Finished testing'
'''
