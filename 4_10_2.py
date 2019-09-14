grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
"""
len(grid) = 9
len(grind[0]) = 6
print(grid[0][0])
print(grind[1][0])
print(grind[2][0])
……
print(grind[0][1])
print(grind[1][1])
……
print(grind[8][6])
"""
for i in range(len(grid[0])):
    for j in range(len(grid)):
        print(grid[j][i], end = '')
        #print('grid[' + str(j) + '][' + str(i) + '] = ' + grid[j][i], end = '')
    print('')
        
