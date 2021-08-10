import queue

def createMap():
    map = []
    map.append(["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"])       
    map.append(["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"])       #1
    map.append(["#", " ", "O", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"])   	#2
    map.append(["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"])       #3
    map.append(["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"])       #4
    map.append(["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"])       #5
    map.append(["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"])       #6
    map.append(["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"])       #7
    map.append(["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"])       #8
    map.append(["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"])       #9
    map.append(["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"])       #10
    map.append(["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "X", " ", " ", "#"])   	#11
    map.append(["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"])

    return map

def printMap(map, path=""):
    for x, pos in enumerate(map[0]):
        if pos == "O":
            start = x
    
    i = start
    j = 0
    pos = set()
    for move in path:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        pos.add((j, i))
    
    for j, row in enumerate(map):
        for i, col in enumerate(row):
            if (j, i) in pos:
                print("+ ", end="")
            else:
                print(col + " ", end="")
    print()

def valid(map, moves):
    for x, pos in enumerate(map[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        
        if not(0 <= i < len(map[0]) and 0 <= j < len(map)):
            return False
        elif (map[j][i] == "#"):
            return False

    return True

def findEnd(map, moves):
    for x, pos in enumerate(map[0]):
        if pos == "O":
            start = x
    
    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

    if map[j][i] == "X":
        print("Found: " +  moves)
        printMap(map, moves)
        return True

    return False


nums = queue.Queue()
nums.put("")
add = ""
map = createMap()

while not findEnd(map, add):
    add = nums.get()
    print(add)
    for j in ["L", "R", "U", "D"]:
        put = add + j
        if valid(map, put):
            nums.put(put) 
