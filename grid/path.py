from grid import grid
import numpy as np

def need_report(G, path_list, danger_nodes, danger_routes):
    for n in danger_routes:
        if np.all(n==G.matrix):
            return True


    for n in danger_nodes:
        if n in path_list:
            return True
    else: 
        return False

time_of_video = 20
T = time_of_video
t = 0
L = 1
H = 1
n = 10
path_list = []
t = 0
people_list = []
new_people = []
grid_list = []
danger_nodes = []

route1 = np.zeros((n,n))
for i in range(6):
    route1[i,i+1] = 1

danger_routes = [route1]
report = []


while t<T:
    coord_list = [(h%n,(h-1)%n) for h in range(T)]
    new_people = [0,1,2]
    for i in new_people:#new people ?:
        if i > len(people_list)-1:
            people_list.append(i)
            path_list.append([])
            grid_list.append(grid(L,H,np.zeros((n,n))))

    for i in people_list:
        coordinate = coord_list[t]                   #get_coordinate #get coordinate for person i at time t
        path_list[i].append(coordinate)


        grid_list[i].visit_node(coordinate)
    t += 1
    new_people = []
        
for i in range(len(people_list)):        
    if need_report(grid_list[i], path_list[i],danger_nodes,danger_routes):
        report.append((i,path_list[i]))
    
print(path_list)
print(report)
