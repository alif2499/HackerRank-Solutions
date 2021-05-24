#This is the desired function required for the problem


def displayPathtoPrincess(n,grid):
    #print all the moves here
    bot = n//2
    bot_position = []
    queen_position = []
    bot_position.append(bot)
    bot_position.append(bot)
    moves = []
    length = len(grid)
    for i in range(length):
        for j in range(length):
            if grid[i][j] == "p":
                queen_position.append(i)
                queen_position.append(j)
    if bot_position[0]>queen_position[0] and bot_position[1]>queen_position[1]:
        while bot_position[0]!=queen_position[0]:
            moves.append("UP")
            bot_position[0] -= 1
        while bot_position[1]!=queen_position[1]:
            moves.append("LEFT")
            bot_position[1] -= 1
    
    if bot_position[0]>queen_position[0] and bot_position[1]<queen_position[1]:
        while bot_position[0]!=queen_position[0]:
            moves.append("UP")
            bot_position[0] -= 1
        while bot_position[1]!=queen_position[1]:
            moves.append("RIGHT")
            bot_position[1] += 1
    
    if bot_position[0]<queen_position[0] and bot_position[1]>queen_position[1]:
        while bot_position[0]!=queen_position[0]:
            moves.append("DOWN")
            bot_position[0] += 1
        while bot_position[1]!=queen_position[1]:
            moves.append("LEFT")
            bot_position[1] -= 1
            
    if bot_position[0]<queen_position[0] and bot_position[1]<queen_position[1]:
        while bot_position[0]!=queen_position[0]:
            moves.append("DOWN")
            bot_position[0] += 1
        while bot_position[1]!=queen_position[1]:
            moves.append("RIGHT")
            bot_position[1] += 1
            
    #print("Bot Position: {}".format(bot_position))
    #print("Queen Position: {}".format(queen_position))
    for i in moves:
        print(i)




