

#this will be pretty hard
#steps to add
#choose the farthest robot via 1 round of BFS 
#apply SEARCH for the farthest robot
#Apply the directions to ALL OTHER ROBOTS IN THE LIST, fill the robot square with a period
#choose the new farthest robot
#repeat previous steps until robot coord list is empty

#EX.X...XXX......XX.XX..X..XX...X..XR....
#EX.X
#...X
#XX..
#....
#XX.X
#X..X
#..XX
#...X
#..XR
#....

#two robots
#EXRX...XXX......XX.XX..X..XX...X..XR....

#EXRX
#...X
#XX..
#....
#XX.X
#X..X
#..XX
#...X
#..XR
#....

#EX.X
#...X
#XX..
#....
#XX.X
#X..X
#..XR
#..X.
#..XR
#....

#EX.X...XXX......XX.XX..X..XR..X...XR....

#sort into grid

import copy 
import numpy as np

class BFS:
    def __init__(self, maze, height, width):
        self.sources = []
        self.entrance = 0
        self.grid = [] #[x,y, type]
        self.connections = [] #[x,y, type, connection]
        
        self.singleCord = [] #[x,y,location]
        self.singleCordList = [] #[location, type, connection (connections are also locations)]
        
        self.graph = [] #[x,y, type, connection, pred, distance]
        self.stack = []
        self.visit = []
        
        self.finalCord = [] #[final directions]

        self.maze = maze
        self.height = height
        self.width = width      
    
    def Makevisual(self):
        x = 1
        y = 1
        visual = ''
        for node in self.maze:
            visual += node
            if x == self.width:
                x = 1
                y += 1
                visual += '\n' 
            else:
                x += 1       
        print('\n')
        print('VISUAL')
        print(visual)
        print('\n')
            
    def Makevisual_row(self):
        x = 1
        y = 1
        visual = []
        row = []
        for node in self.maze:
            row.append(node)
            if x == self.width:
                x = 1
                y += 1
                rowdone = " ".join(row)
                visual.append(rowdone)
                row = []
            else:
                x += 1       
        #print('\n')
        #print('VISUAL')
        #print(visual)
        #print('\n')
        return visual
        
    def Makegrid(self):
        #[x, y, type (X, ., R, E)]
        details = []
        x = 1
        y = 1
        location = 1
        for node in self.maze:
            details = [x, y, node]
            details2 = [x,y,location]
            if node == 'R':
                self.sources.append(location)
            if node == "E":
                self.entrance = location
                print("ENTRANCE location: ", self.entrance)
            if x == self.width:
                x = 1
                y += 1
            else:
                x += 1
            
            self.grid.append(details)
            self.singleCord.append(details2)
            location += 1
        print("Location of robots (self.sources): ", self.sources)
        #print(self.grid)
        print("SELF.singleCord: ", self.singleCord)
    
    def find_connections(self):
        #check up, then right, then down, then left
        maxHeight = self.height #10
        minHeight = 1
        maxWidth = self.width #4
        minWidth = 1
        
        counter = 0
        for node_list in self.grid:
            x = node_list[0]
            y = node_list[1]
            node_type = node_list[2]
            connection = []
            
            SingleCORDconnection = []
            if x + 1 <= maxWidth: #Right
                connection.append([x+1,y])
                for nlist in self.singleCord:
                    if x+1 == nlist[0] and y == nlist[1]:
                        SingleCORDconnection.append(nlist[2]) #appends single number coordinate
            if x - 1 >= minWidth: #Left
                connection.append([x-1,y])
                for nlist in self.singleCord:
                    if x-1 == nlist[0] and y == nlist[1]:
                        SingleCORDconnection.append(nlist[2]) #appends single number coordinate           
            if y + 1 <= maxHeight: #Down
                connection.append([x,y+1])
                for nlist in self.singleCord:
                    if x == nlist[0] and y+1 == nlist[1]:
                        SingleCORDconnection.append(nlist[2]) #appends single number coordinate               
            if y - 1 >= minHeight: #Up
                connection.append([x,y-1])
                for nlist in self.singleCord:
                    if x == nlist[0] and y-1 == nlist[1]: #[x, y, n]
                        SingleCORDconnection.append(nlist[2]) #appends single number coordinate           
            
            details = [x, y, node_type, connection]
            self.connections.append(details)
            
            details2 = [self.singleCord[counter][2], node_type, SingleCORDconnection, None, None, [x,y]] #pred, distance are the nones
            self.singleCordList.append(details2)
            counter += 1
            #print(details2)
        print(self.singleCordList)
    
    def Compile_robot_order(self):
        #self.sources
        distances = []
        unsolvable = False 
        print('\n')
        for source in self.sources: 
            self.stack = []
            distance_from_robot_list = copy.deepcopy(self.singleCordList)
            print("New COPY: ", distance_from_robot_list)
            distance_from_robot_list[source-1][4] = 0
            #print("SOURCE: ", source)
            print("SOURCE list: ", distance_from_robot_list[source-1])
    
            self.stack.append(source-1)
            #print("SELF.STACK: ", self.stack)
            EntranceFound = False
            while len(self.stack) != 0 and EntranceFound == False:
                #[location, node_type (X, E, ., R), connections, pred, distance]
                current = self.stack[0]
                node_list = distance_from_robot_list[current]
                #print("CURRENT: ", current)
                #print("NODE LIST: ", node_list)
                distance = int(node_list[4]) + 1
                pred = current + 1
                connections = node_list[2]
                node_type = node_list[1]
    
                for node in connections:
                    check_list = distance_from_robot_list[node-1]
                    check_type = check_list[1]
                    location = check_list[0]
                    #[location, node_type (X, E, ., R), connections, pred, distance]
                    if check_list[3] == None and check_type != "X":
                        distance_from_robot_list[node-1][3] = pred
                        distance_from_robot_list[node-1][4] = distance
                        if check_list[1] == "E":
                            #print("found entrance!")
                            EntranceFound = True
                            break
                        self.stack.append(location-1)
                    else:
                        continue
                self.stack.pop(0)
            print("End COPY", distance_from_robot_list)
            print("SINGLE CORD: ", self.singleCordList)
            print("ENTRANCE FOUND: ", EntranceFound)
            if EntranceFound == True:
                steps = distance_from_robot_list[self.entrance-1][4]
                distances.append(steps)
                del(distance_from_robot_list)
                print("STEPS: ", steps)
            if EntranceFound == False:
                unsolvable = True
            print('\n')
        print(distances)
        sorted_distances = sorted((copy.deepcopy(distances)))
        print("SORTED DISTANCES: ", sorted_distances)
        #print(self.singleCordList)   
    
        self.sources = [x for _, x in sorted(zip(sorted_distances, self.sources))] 
        self.sources.reverse()
        #sources is ordered so that the farthest robot is at the start of the list, and the closest robots at the end of the list
        print("SORTED SELF.SOURCES: ", self.sources)
    
        return self.sources, unsolvable
            
    
    def Solve_graph(self):
        self.stack = []
        source = self.sources[0]
        print("Finding this SOURCE: ", source)
        self.stack.append(source-1)
        EntranceFound = False
        singleCordList = copy.deepcopy(self.singleCordList)
        singleCordList[source-1][4] = 0
        while len(self.stack) != 0 and EntranceFound == False:
            #[location, node_type (X, E, ., R), connections, pred, distance]
            current = self.stack[0]
            node_list = singleCordList[current]
            #print("CURRENT: ", current)
            #print("NODE LIST: ", node_list)
            distance = int(node_list[4]) + 1
            pred = current + 1
            connections = node_list[2]
            node_type = node_list[1]
            
            for node in connections:
                check_list = singleCordList[node-1]
                check_type = check_list[1]
                location = check_list[0]
                #[location, node_type (X, E, ., R), connections, pred, distance]
                if check_list[3] == None and check_type != "X":
                    singleCordList[node-1][3] = pred
                    singleCordList[node-1][4] = distance
                    if check_list[1] == "E":
                        print("found entrance!")
                        EntranceFound = True
                        break
                    self.stack.append(location-1)
                else:
                    continue
            self.stack.pop(0)
        
        #print(singleCordList)
        print("STEP_CHECK: ", singleCordList[self.entrance-1][4])
        
        
        return singleCordList
    
    def Find_Directions(self, singleCordList):
        print('\n')
        self.visit = []
        print("SELF.visit: ", self.visit)
        done = False
        self.visit.append(self.entrance-1)
        source = self.sources[0]
        print("DIRECTION source: ", source)
        
        
        while done == False:
            current = self.visit[0]
            node_list = singleCordList[current]
            #[location, node_type (X, E, ., R), connections, pred, distance]
            current_coordinates = self.singleCord[current]
            pred = node_list[3]
            cord = current_coordinates[2]
            if cord == source:
                done = True
                self.singleCordList[current][1] = '.'
                break
            print("SELF.SINGLECORD [pred-1]: ", self.singleCord[pred-1])
            connect_coordinates = self.singleCord[pred-1]
            now_x = current_coordinates[0]
            now_y = current_coordinates[1]
            connect_x = connect_coordinates[0]
            connect_y = connect_coordinates[1]           
            
            if now_x == connect_x + 1 and now_y == connect_y: #right
                self.finalCord.append("R")
            if now_x == connect_x - 1 and now_y == connect_y: #left
                self.finalCord.append("L")            
            if now_x == connect_x and now_y == connect_y + 1: #down
                self.finalCord.append("D")           
            if now_x == connect_x and now_y == connect_y - 1: #up
                self.finalCord.append("U")    
            
            self.visit.pop(0)
            self.visit.append(pred-1)
        self.finalCord.reverse()
        #print(self.finalCord)
        print("UPDATED self.singleCordList: ", self.singleCordList)
        print("".join(self.finalCord))
        result = "".join(self.finalCord)
        self.finalCord = []
        print('\n')
        
        self.sources.pop(0)
        print("NEW UPDATED self.sources: ", self.sources)
        
        return (result), self.sources
    
    def update_graph(self, coordinates):
        #print(self.singleCordList)
        maxHeight = self.height #10
        minHeight = 1
        maxWidth = self.width #4
        minWidth = 1        
        print(self.sources)
        robot_num = 0
        for robot in self.sources: 
            x = self.singleCordList[robot-1][5][0]
            y = self.singleCordList[robot-1][5][1]
            node_type = self.singleCordList[robot-1][1]
            connections = self.singleCordList[robot-1][2]
            current = self.singleCordList[robot-1][0]
            
            for direction in coordinates:
                next_current_found = False
                if direction == 'U' and y - 1 >= minHeight:
                    check = [x, y-1]
                    for connection in connections: 
                        if [self.singleCordList[connection-1][5][0], self.singleCordList[connection-1][5][1]] == check and self.singleCordList[connection-1][1] != 'X':
                            self.singleCordList[connection-1][1] = 'R'
                            self.singleCordList[current-1][1] = '.'
                            next_current = connection
                            next_current_found = True
                            break
                            
                            
                if direction == 'D' and y + 1 <= maxHeight:
                    check = [x, y+1]
                    for connection in connections: 
                        if [self.singleCordList[connection-1][5][0], self.singleCordList[connection-1][5][1]] == check and self.singleCordList[connection-1][1] != 'X':
                            self.singleCordList[connection-1][1] = 'R'
                            self.singleCordList[current-1][1] = '.'    
                            next_current = connection
                            next_current_found = True
                            break                            
                            
                if direction == 'R' and x + 1 <= maxWidth:
                    check = [x+1, y]
                    for connection in connections: 
                        if [self.singleCordList[connection-1][5][0], self.singleCordList[connection-1][5][1]] == check and self.singleCordList[connection-1][1] != 'X':
                            self.singleCordList[connection-1][1] = 'R'
                            self.singleCordList[current-1][1] = '.'    
                            next_current = connection
                            next_current_found = True
                            break                            
                            
                if direction == 'L' and x - 1 >= minWidth:
                    check = [x-1, y]
                    for connection in connections: 
                        if [self.singleCordList[connection-1][5][0], self.singleCordList[connection-1][5][1]] == check and self.singleCordList[connection-1][1] != 'X':
                            self.singleCordList[connection-1][1] = 'R'
                            self.singleCordList[current-1][1] = '.'   
                            next_current = connection
                            next_current_found = True
                            break                            
                            
                #print("NEXT CURRENT: ", next_current)
                #test = self.singleCordList[next_current-1]
                #print(self.singleCordList[next_current-1])
                if next_current_found:
                    x = self.singleCordList[next_current-1][5][0]
                    y = self.singleCordList[next_current-1][5][1]
                    node_type = self.singleCordList[next_current-1][1]
                    connections = self.singleCordList[next_current-1][2]
                    current = self.singleCordList[next_current-1][0]   
            
            new_source = self.singleCordList[next_current-1][0]   
            self.sources[robot_num] = new_source
            robot_num += 1
            if self.singleCordList[self.entrance-1][1] == 'R':
                self.singleCordList[self.entrance-1][1] = 'E'
                self.sources.pop()
                
        print("UPDATED singleCordList (ROBOTS MOVED): ", self.singleCordList)
        if len(self.sources) == 0: 
            print("NO MORE ROBOTS!")
        print(self.sources)
        
        return self.sources
        
    def revert(self):
        string_maze = ''
        for node_list in self.singleCordList:
            string_maze += node_list[1]
        
        upper_bound = self.width
        for node in range(0, self.width * self.height, self.width):
            print(string_maze[node:upper_bound])
            upper_bound += self.width

def Maze_solver(maze, height, width):
    combined_directions = ''
    maze = BFS(maze, height, width)
    maze.Makegrid()
    maze.find_connections()
    robots_left, unsolvable = maze.Compile_robot_order()    
    
    if unsolvable == True: 
        return 'unsolvable' 
    
    while len(robots_left) != 0:
        singlecord = maze.Solve_graph()
        result, robots_left = maze.Find_Directions(singlecord)
        combined_directions += result
        maze.update_graph(result)
        maze.revert()
    
    return combined_directions
    
            
                
                
            
                    
            
            
#EXRX...XXX......XX.XX..X..XX...X..XR....       

#EX.X...XXX......XX.XX..X..XR..X...X..R..        

#______________________________________
#EXRX...XXX......XX.XX..XR.XX...X..XR....