"""
Modul zur Simulation
------------------------
Ausbreitung eines Virus in einer Population als Zufallsprozess 
auf einem Graphen - Programmierprojekt zur COMAII, Teil 1
geschrieben von Quentin Wach, 18. Juni 2020
"""
import random

class Node:
    def __init__(self, key, coordinates, infection_date, 
        neighbors, active=True):
        self.key = key
        self.coordinates = coordinates
        self.infection_date = infection_date
        self.neighbors = sorted(neighbors)
        self.active = active

class Virus:
    def __init__(self, time, incubation_period, contageous_period, mobility,
        transmissibility, graph, side_length):
        self.time = time                            # non-negative int
        self.incubation_period = incubation_period  # non-negative int
        self.contageous_period = contageous_period  # non-negative int
        self.side_length = side_length              # non-negative int
        self.mobility = mobility                    # float [0,1]
        self.transmissibility = transmissibility    # float [0,1]
        self.graph = self.sorted_graph(graph)       # sorted list of Node-objects
        self.grid = self.initGrid()                 # array of Nodes from coordinates

    def sorted_graph(self, graph):
        """
        Returns the graph sorted by the keys of the Nodes.
        """
        new_graph_list = []
        key_list = []
        for Nd in graph:
            key_list.append(Nd.key)
        key_list = sorted(key_list)
        for k in key_list:
            for node in graph:
                if node.key == k:
                    new_graph_list.append(node)

        return new_graph_list

    def initGrid(self):
        """
        Return an array of the Nodes from the graph placed by their coordinates.
        """
        # create a list of all nodes in the graph sorted by the coordinates
        line = sorted(self.graph, key=lambda Node: Node.coordinates)
        # convert the list into a array for the given side-length
        grid = []
        for y in range(self.side_length):
            l = []
            for x in range(self.side_length):
                l.append([line[x]])
            grid.append(l)
        return grid

    def time_step(self):
        # step forward in time
        self.time += 1
        # verbreite den Virus
        self.transmitt()
        # bewege Nodes zufällig
        self.moveRandom()

    def transmitt(self):
        # für jeden Knoten
        for Nd in self.graph:
            # falls Knoten ein Infizierter
            if Nd.active and Nd.infection_date != -1:
                # gesund oder gestorben
                if self.time > (Nd.infection_date + self.incubation_period + self.contageous_period):
                    Nd.active = False
                # krank und ansteckend
                elif self.time > (Nd.infection_date + self.incubation_period):
                    # interagiert mit jedem Nachbarn
                    for k in Nd.neighbors:
                        # find the node with the key k in the graph
                        for N in self.graph:
                            if k == N.key:
                                Nd_k = N
                                break
                        if Nd_k.infection_date == -1:
                            # zufällige Ansteckung des Nachbarn
                            if random.random() < self.transmissibility:
                                Nd_k.infection_date = self.time

    def moveRandom(self):
        """
        Move a fraction of all nodes in the graph while updating the grid and neighbors.
        """
        for Node in self.graph:
            if random.random() <= self.mobility:
                # 0) save previous neighbor keys
                prev_neigh_keys = Node.neighbors 
                # 1) change the position to a neighboring grid cell
                x, y = Node.coordinates[0], Node.coordinates[1]
                new_x = x; new_y = y
                # X
                if x != 0 and x != self.side_length - 1:
                    new_x = x + round(random.random() * 2 - 1) 
                if x == 0:
                    new_x = x + random.choice([0,1])
                if x == self.side_length - 1:
                    new_x = x - random.choice([0,1])
                # Y
                if y != 0 and y != self.side_length - 1:
                    new_y = y + round(random.random() * 2 - 1) 
                if y == 0:
                    new_y = y + random.choice([0,1])
                if y == self.side_length - 1:
                    new_y = y - random.choice([0,1])
                Node.coordinates = (new_x, new_y)
                # 2) update the grid at those two positions
                for N in self.grid[y][x]:
                    if N == Node:
                        del N
                        break
                self.grid[new_y][new_x].append(Node)
                # 3) get the eight new neighbor coordinates
                new_neighbor_coords = []
                base = (new_x, new_y)
                for a in [-1,0,1]:
                    for b in [-1,0,1]:
                        new_neighbor_coords.append((base[0] + a, base[1] + b))
                        if a == b and a == 0:
                            new_neighbor_coords.pop()
                # 3) update the neighbors of the node based on the keys retrieved from the grid
                # del Node.key from all neighbors
                for N in self.graph:
                    if N.key in prev_neigh_keys:
                        new_N_neighs = []
                        for n_key in N.neighbors:
                            if n_key != Node.key:
                                new_N_neighs.append(n_key)
                        N.neighbors = sorted(new_N_neighs)
                # add Node.key to area grid cells
                surr_keys = []
                for N in self.graph:
                    if N.coordinates in new_neighbor_coords:
                        if Node.key not in N.neighbors:
                            N.neighbors.append(Node.key)
                            N.neighbors = sorted(N.neighbors)
                        # add area keys as its own neighbors
                        surr_keys.append(N.key)
                Node.neighbors = sorted(surr_keys)

    def time_steps(self, n):
        for i in range(n):
            self.time_step()




