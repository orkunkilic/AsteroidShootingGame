
x = int(input())
y = int(input())
g = int(input())

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

# Initial draw
row = ['*'] * y
grid = []
for satir in range(x):
    grid.append(row.copy())
row = [' '] * y
for satir in range(g):
    grid.append(row.copy())

if y % 2 == 0:
    ship_loc = (y//2) - 1
else:
    ship_loc = (y // 2)

row = [' '] * y
row[ship_loc] = '@'
for satir in range(1):
    grid.append(row.copy())

ex = 0
if (x == 0):
    # print('-'*72)
    print('YOU WON!')
    ex = 1

for row in grid:
    for dot in row:
        print(dot, end='')
    print()
time = 0
score = 0
total_row = x+g

while (True and ex != 1):

    if (x != 0):
        print('-'*72)

    inp = input('Choose your action!\n')
    inp = inp.lower()
    if (inp == 'exit'):
        for row in grid:
            for dot in row:
                print(dot, end='')
            print()
        break
    elif (inp == 'fire'):
        total_move = 0
        for row in reversed(grid):
            if(row[ship_loc]==' '):
                total_move += 1
            if(row[ship_loc] == '*'):
                break

        for fire_dot in range(-2, -total_move - 3, -1):

            if fire_dot != -2:
                grid[fire_dot + 1][ship_loc] = ' '
            else:
                pass

            if fire_dot == -total_move - 2:
                break
            else:
                grid[fire_dot][ship_loc] = '|'

            for row in grid:
                for dot in row:
                    print(dot, end='')
                print()
            print('-'*72)

        if(fire_dot in range(-len(grid), len(grid))):
            if(grid[fire_dot][ship_loc]=='*'):
                score+=1
            grid[fire_dot][ship_loc] = ' '




    elif (inp == 'right'):
        if (ship_loc == y-1):
            pass
        else:
            grid[-1][ship_loc] = ' '
            grid[-1][ship_loc + 1] = '@'
            ship_loc += 1

    elif (inp == 'left'):
        if (ship_loc == 0):
            pass
        else:
            grid[-1][ship_loc] = ' '
            grid[-1][ship_loc - 1] = '@'
            ship_loc -= 1

    """
    if (not '*' in grid[:][-1]):
        g-=1
        x -= 1
    """
    time += 1
    if (time % 5 == 0 and time != 0):
        g -= 1
        added = 0
        for row in reversed(grid):
            if(row == [' '] * y):
                added += 1
            if('*' in row):
                break
        if ( added <= 0):
            print('GAME OVER')
            for row in grid:
                for dot in row:
                    print(dot, end='')
                print()
            break
        grid.pop(-2)
        #added += 1
        grid.insert(0, [' ']*y)

    ctd = 0
    for row in grid[:-1]:
        if('*' in row):
            pass
        else:
            ctd += 1

    if(ctd == total_row):
        # print('-' * 72)
        print('YOU WON!')
        for row in grid:
            for dot in row:
                print(dot, end='')
            print()
        break

    for row in grid:
        for dot in row:
            print(dot, end='')
        print()


print('-'*72)
print('YOUR SCORE:', score)


# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
