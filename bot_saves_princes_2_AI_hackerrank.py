

def nextMove(n,r,c,grid):
    bot_position = []
    queen_position = []
    bot_position = []
    length = len(grid)
    for i in range(length):
        for j in range(length):
            if grid[i][j] == "p":
                queen_position.append(i)
                queen_position.append(j)
    for i in range(length):
        for j in range(length):
            if grid[i][j] == "m":
                bot_position.append(i)
                bot_position.append(j)
    #return bot_position, queen_position
    if bot_position[0]>queen_position[0] and bot_position[1]>queen_position[1]:
        return "UP"
    
    if bot_position[0]>queen_position[0] and bot_position[1]<queen_position[1]:
        return "UP"
    
    if bot_position[0]<queen_position[0] and bot_position[1]>queen_position[1]:
        return "DOWN"
            
    if bot_position[0]<queen_position[0] and bot_position[1]<queen_position[1]:
        return "DOWN"

    if bot_position[0]==queen_position[0] and bot_position[1]<queen_position[1]:
        return "RIGHT"
    
    if bot_position[0]==queen_position[0] and bot_position[1]>queen_position[1]:
        return "LEFT"
    
    if bot_position[0]<queen_position[0] and bot_position[1]==queen_position[1]:
        return "DOWN"
    
    if bot_position[0]==queen_position[0] and bot_position[1]<queen_position[1]:
        return "UP"