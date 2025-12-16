import numpy

def CheckWalls(step_x, step_y):
    new_x = position_x + step_x
    new_y = position_y + step_y
    if maze_numpy[new_x][new_y] == "#":
        print(maze_numpy[position_x + step_x][position_y + step_y])
        print("There is a wall there!")
        return False
    return True

def CheckBoundaries(step):
    if step == "N":
        if position_x == 0:
            print("You can't go there!")
        else:
            if CheckWalls(-1, 0):
                return (-1, 0)
    elif step == "S":
        if position_x == 4:
            print("You can't go there!")
        else:
            if CheckWalls(1, 0):
                return (1, 0)
    elif step == "E":
        if position_y == 4:
            print("You can't go there!")
        else:
            if CheckWalls(0, 1):
                return (0, 1)
    elif step == "W":
        if position_y == 0:
            print("You can't go there!")
        else:
            if CheckWalls(0, -1):
                return (0, -1)
    else:
        print("No such direction!")
    return None

maze = [
    ["S", ".", ".", "#", "."],
    ["#", "#", ".", "#", "."],
    [".", ".", ".", ".", "."],
    [".", "#", "#", "#", "#"],
    [".", ".", ".", ".", "E"]
]
maze_numpy = numpy.array(maze)
position = maze_numpy[0][0]
position_x = 0
position_y = 0

while position != "E":
    print(f"Start position: ({position_x}, {position_y})")
    step = input("Move (N/S/E/W): ")
    steps = CheckBoundaries(step)
    if steps: 
        dx, dy = steps
        position_x += dx
        position_y += dy
    position = maze_numpy[position_x][position_y]

if position == "E":
    print("You found the exit! You win!.")