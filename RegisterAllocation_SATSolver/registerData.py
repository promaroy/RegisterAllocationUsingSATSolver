# input is liveness information of variables

# give allotted number of registers , number of variables

liveness = [[1,4],[2,4],[3,4]]
edges = []
for x in range(len(liveness)):
    for y in range(x+1,len(liveness)):
        if liveness[y][0] <= liveness[x][1]:
            edges.append([x+1,y+1])
            #edges.append([y,x])

colors = 2
vertices = 3
print("p " + str(colors) +" "+ str(vertices) +" "+ str(len(edges))) 
for x in range(len(edges)):
    print("e "+ str(edges[x][0])+ " "+ str(edges[x][1]))
   # print("e "+ str(edges[x][1])+ " "+ str(edges[x][0]))



