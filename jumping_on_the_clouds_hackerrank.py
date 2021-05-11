path = [0,0,0,1,0,0]      #Some example [0, 0, 1, 0, 0, 1, 0]    [0,0,0,1,0,0]   
jump = 0
i = 0

while i < (len(path) - 1):
    if len(path) - i == 2:
        jump += 1
        break
    else:
        if path[i + 1] == 0:
            if path[i + 2] == 0:
                jump += 1
                i += 2
            else:
                jump += 1
                i += 1
        elif path[i + 1] != 0 and path[i + 2] == 0:
            jump += 1
            i += 2
print(jump)