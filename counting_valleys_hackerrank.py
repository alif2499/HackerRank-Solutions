path = "UDDDUDUU" #[1,0,0,0,1,0,1,1]
place = 0
valleyCounter = 0

for i in range (len(path)):
    if path[i] == "U":
        place += 1
    else:
        if place == 0:
            valleyCounter += 1
        place -= 1
        
print(valleyCounter)









