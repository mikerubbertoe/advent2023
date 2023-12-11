import heapq as heap

class Node():
    #0 = closed | 1 = open
    def __init__(self, north=0, south=0, east=0, west=0, row=0, col=0):
        self.north = north
        self.south = south
        self.east  = east
        self.west  = west
        self.row   = row
        self.col   = col

    def __str__(self):
        return f"north={self.north}, south={self.south}, east={self.east}, west={self.west}"

    def __repr__(self):
        return f"Node(north={self.north}, south={self.south}, east={self.east}, west={self.west})"

def part1():
    tunnel, start = createTunnel()
    pq = []
    not_visited = set()
    distance = [float('inf')] * (len(tunnel) * len(tunnel[0]))
    startingNode = (len(tunnel) * start[0]) + start[1]
    distance[startingNode] = 0
    for i in range(len(tunnel) * len(tunnel[0])):
        not_visited.add(i)

    heap.heappush(pq, (0, startingNode))

    while pq:
        currNode = heap.heappop(pq)
        # print(currNode)
        not_visited.remove(currNode[1])
        for n in get_neighbors(currNode[1], tunnel):
            row = int(n / len(tunnel[0]))
            col = int(n % len(tunnel[0]))
            thisNode = tunnel[int(currNode[1] / len(tunnel[0]))][int(currNode[1] % len(tunnel[0]))]

            if n in not_visited:
                cost = distance[(thisNode.row * len(tunnel)) + thisNode.col] if distance[(thisNode.row * len(tunnel)) + thisNode.col] != float('inf') else 0
                old_cost = distance[n]
                new_cost = cost + 1

                if new_cost < old_cost:
                    distance[len(tunnel[0]) * row + col] = new_cost
                    heap.heappush(pq, (new_cost, n))

    print(sorted(distance))

def get_neighbors(node, tunnel):
    a, b = len(tunnel), len(tunnel[0])
    neighbors = []
    currRow = int(node / b)
    currCol = int(node % b)

    # check north
    row, col = [-1, 0]
    newRow = row + currRow
    newCol = col + currCol
    if 0 <= newRow < len(tunnel) and 0 <= newCol < len(tunnel[0]):
        currNode = tunnel[currRow][currCol]
        nextNode = tunnel[newRow][newCol]
        if currNode.north == 1 and nextNode.south == 1:
            neighbors.append(int((newRow * b) + newCol))

    # check south
    row, col = [1, 0]
    newRow = row + currRow
    newCol = col + currCol
    if 0 <= newRow < len(tunnel) and 0 <= newCol < len(tunnel[0]):
        currNode = tunnel[currRow][currCol]
        nextNode = tunnel[newRow][newCol]
        if currNode.south == 1 and nextNode.north == 1:
            neighbors.append(int((newRow * b) + newCol))

    # check east
    row, col = [0, 1]
    newRow = row + currRow
    newCol = col + currCol
    if 0 <= newRow < len(tunnel) and 0 <= newCol < len(tunnel[0]):
        currNode = tunnel[currRow][currCol]
        nextNode = tunnel[newRow][newCol]
        if currNode.east == 1 and nextNode.west == 1:
            neighbors.append(int((newRow * b) + newCol))

    # check west
    row, col = [0, -1]
    newRow = row + currRow
    newCol = col + currCol
    if 0 <= newRow < len(tunnel) and 0 <= newCol < len(tunnel[0]):
        currNode = tunnel[currRow][currCol]
        nextNode = tunnel[newRow][newCol]
        if currNode.west == 1 and nextNode.east == 1:
            neighbors.append(int((newRow * b) + newCol))

    return neighbors

def createTunnel():
    tunnel = []
    r, c = 0, 0
    start = None
    with open("day10_input.txt") as f:
        for line in f:
            row = []
            c = 0
            for char in line:
                if char == '.':
                    row.append(Node())
                elif char == '|':
                    row.append(Node(north=1, south=1, row=r, col=c))
                elif char == '-':
                    row.append(Node(east=1, west=1, row=r, col=c))
                elif char == 'L':
                    row.append(Node(north=1, east=1, row=r, col=c))
                elif char == 'J':
                    row.append(Node(north=1, west=1, row=r, col=c))
                elif char == '7':
                    row.append(Node(south=1, west=1, row=r, col=c))
                elif char == 'F':
                    row.append(Node(south=1, east=1, row=r, col=c))
                elif char == 'S':
                    row.append(Node())
                    start = (r, c)
                c += 1
            tunnel.append(row)
            r += 1

    #check north
    row, col = [-1, 0]
    newRow = row + start[0]
    newCol = col + start[1]
    if 0 <= newRow < len(tunnel) and 0 <= newCol < len(tunnel[0]):
        nextNode = tunnel[newRow][newCol]
        if nextNode.south == 1:
            tunnel[start[0]][start[1]].north = 1

    #check south
    row, col = [1, 0]
    newRow = row + start[0]
    newCol = col + start[1]
    if 0 <= newRow < len(tunnel) and 0 <= newCol < len(tunnel[0]):
        nextNode = tunnel[newRow][newCol]
        if nextNode.north == 1:
            tunnel[start[0]][start[1]].south = 1

    #check east
    row, col = [0, 1]
    newRow = row + start[0]
    newCol = col + start[1]
    if 0 <= newRow < len(tunnel) and 0 <= newCol < len(tunnel[0]):
        nextNode = tunnel[newRow][newCol]
        if nextNode.west == 1:
            tunnel[start[0]][start[1]].east = 1

    #check west
    row, col = [0, -1]
    newRow = row + start[0]
    newCol = col + start[1]
    if 0 <= newRow < len(tunnel) and 0 <= newCol < len(tunnel[0]):
        nextNode = tunnel[newRow][newCol]
        if nextNode.east == 1:
            tunnel[start[0]][start[1]].west = 1

    return tunnel, start

part1()