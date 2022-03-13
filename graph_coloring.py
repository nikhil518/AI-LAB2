class graph:
       def __init__(self,edges,n):
         self.adj=[[] for _ in range(n)]
         for(src,dest)in edges:
            self.adj[src].append(dest)
            self.adj[dest].append(src)
def color_graph(graph):
   result={}
   for u in range(n):
     assigned=set([result.get(i) for i in graph.adj[u]if i in result])
     color=1
     for c in assigned:
       if color!=c:
         break
       color= color+1
     result[u]=color
   for v in range(n):
    print("COLOR ASSIGNED TO VERTEX",v,"is",colors[result[v]])
   print("\n")
   for v in range(n):
    print("COLOR ASSIGNED TO EDGE",v,"is",colors[result[v]+3])

if __name__=='__main__':
  colors=["","YELLOW","BLACK","GREEN","PURPLE","BROWN","RED","BLUE","WHITE","VIOLET","ORANGE","PINK"]
  edges=[(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,0)]
  n=7
  Graph=graph(edges,n)
  color_graph(Graph)