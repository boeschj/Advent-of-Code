def partOne(data: list) -> str:
    #Need to find the word XMAS
    
    #Check the following cases:
    #Horizontal
    #Vertical
    #Diagonal
    #Written backwards
    
    #Create a 2D array for the input text
    grid = [list(row) for row in data]
    rows = len(grid)
    cols = len(grid[0])
    
    word = "XMAS"
    found_words = 0
    
    #Iterate through each character. When we find the character X, grab its surrounding neighbors and see if we have one or more matches for 'M'
    #If so, retrieve the remaining characters in that direction. if combining them spells XMAS, we've got a match!
    for yIdx, row in enumerate(grid):
        for xIdx, char in enumerate(row):
            if (char == "X"):
         
                #initialize neighbors in every direction from the X
                l = r = u = d = ul = ur = dl = dr = None
                neighbors = []
                
                #For each neighbor, ensure we're in-bounds for that direction and then retrieve its value
                #left
                if xIdx > 0:
                    vectorLeft = (0, -1)
                    l = grid[yIdx][xIdx - 1]
                    neighbors.append([l, vectorLeft])

                #right
                if xIdx < cols - 1:
                    vectorRight = (0, 1)
                    r = grid[yIdx][xIdx + 1]
                    neighbors.append(([r, vectorRight]))

                #up
                if yIdx > 0:
                    vectorUp = (-1, 0)
                    u = grid[yIdx - 1][xIdx]
                    neighbors.append(([u, vectorUp]))

                #down
                if yIdx < rows - 1:
                    vectorDown = (1, 0)
                    d = grid[yIdx + 1][xIdx]
                    neighbors.append(([d, vectorDown]))

                #top left
                if yIdx > 0 and xIdx > 0:
                    vectorUL = (-1, -1)
                    ul = grid[yIdx - 1][xIdx - 1]
                    neighbors.append(([ul, vectorUL]))

                #top right
                if yIdx > 0 and xIdx < cols - 1:
                    vectorUR = (-1, 1)
                    ur = grid[yIdx - 1][xIdx + 1]
                    neighbors.append(([ur, vectorUR]))

                #bottom left
                if yIdx < rows - 1 and xIdx > 0:
                    vectorDL = (1, -1)
                    dl = grid[yIdx + 1][xIdx - 1]
                    neighbors.append(([dl, vectorDL]))

                #bottom right
                if yIdx < rows - 1 and xIdx < cols - 1:
                    vectorDR = (1, 1)
                    dr = grid[yIdx + 1][xIdx + 1]
                    neighbors.append(([dr, vectorDR]))
                
                
                for neighbor, vector in neighbors:
                    if neighbor == 'M':
                        dy, dx = vector
                        word_chars = []
                        for i in range(len(word)):
                            new_y = yIdx + (dy * i)
                            new_x = xIdx + (dx * i)
                            
                            if 0 <= new_y < rows and 0 <= new_x < cols:
                                word_chars.append(grid[new_y][new_x])
                            else:
                                break
                        
                        if ''.join(word_chars) == word:
                            found_words += 1

    return found_words

def partTwo(data: list) -> int:
    
    ##Need to find this pattern:
    #Horizontal patterns on the top and bottom   
    # M.S               S.M
    # .A.               .A.
    # M.S               S.M
    #
    # Vertical patterns where its on the side 
    # M.M               S.S
    # .A.               .A.  
    # S.S               M.M
    
    #Create a 2D array for the input text
    grid = [list(row) for row in data]
    rows = len(grid)
    cols = len(grid[0])
    
    found_patterns = 0
    
    #Similar approach to before, but this time match on 'A", only pull the edges and see if the combination matches the above
    #Early return if anything isn't an "M" or "S" to save on computations 
    for yIdx, row in enumerate(grid):
        for xIdx, char in enumerate(row):
            if char == "A":
                ul = ur = dl = dr = None
                
                if yIdx > 0 and xIdx > 0:
                    ul = grid[yIdx - 1][xIdx - 1]
                    if ul != "M" and ul != "S":
                        continue
                    
                if yIdx > 0 and xIdx < cols - 1:
                    ur = grid[yIdx - 1][xIdx + 1]
                    if ur != "M" and ur != "S":
                        continue
                    
                if yIdx < rows - 1 and xIdx > 0:
                    dl = grid[yIdx + 1][xIdx - 1]
                    if dl != "M" and dl != "S":
                        continue
                    
                if yIdx < rows - 1 and xIdx < cols - 1:
                    dr = grid[yIdx + 1][xIdx + 1]
                    if dr != "M" and dr != "S":
                        continue
                    
                horizontal = (ul == "M" and ur == "S" and dl == "M" and dr == "S") or (ul == "S" and ur == "M" and dl == "S" and dr == "M")
                vertical = (ul == "M" and dl == "S" and ur == "M" and dr == "S") or (ul == "S" and dl == "M" and ur == "S" and dr == "M")
                
                if horizontal or vertical:
                    found_patterns += 1

    return found_patterns

if __name__ == "__main__":

    with open("inputs/day04.txt") as f:
        data = f.read().splitlines()
    
    print("XMAS Count:", partOne(data))
    print("X-MAS Count:", partTwo(data))