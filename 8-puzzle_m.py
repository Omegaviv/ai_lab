initial = [[2, 8, 3],
           [1, 6, 4],
           [7, 0, 5]]
goal = [[1, 2, 3],
        [8, 0, 4],
        [7, 6, 5]]


def get_f(current, g):
    h = 0
    for i in range(3):
        for j in range(3):
            if current[i][j] != goal[i][j]:
                h += 1
    return g + h

def manhattan(self):
        h = 0
        for i in range(3):
            for j in range(3):
                x, y = divmod(self.board[i][j], 3)
                h += abs(x-i) + abs(y-j)
        return h
        
def is_goal(current):
    for i in range(3):
        for j in range(3):
            if current[i][j] != goal[i][j]:
                return False
    return True


def print_puzzle(current):
    for i in range(3):
        print("|", end="")
        for j in range(3):
            print(" " + str(current[i][j]) + " ", end="")
        print("|")


def reset_current(current):
    tmp = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0]]
    for i in range(3):
        for j in range(3):
            tmp[i][j] = current[i][j]
    return tmp


def get_next(current, h, prev=None):
    if prev is None:
        prev = [-1, - 1]
    empty = [0, 0]
    move_empty = [0, 0]
    for i in range(3):
        for j in range(3):
            if current[i][j] == 0:
                empty = [i, j]
    # try left
    min_f = 1000
    t_current = reset_current(current)
    # try left
    if 0 <= empty[1] - 1 != prev[1]:
        t_current[empty[0]][empty[1]] = t_current[empty[0]][empty[1] - 1]
        t_current[empty[0]][empty[1] - 1] = 0
        if get_f(t_current, h) <= min_f:
            min_f = get_f(t_current, h)
            move_empty = [empty[0], empty[1] - 1]
    t_current = reset_current(current)
    # try right
    if empty[1] + 1 <= 2 and empty[1] + 1 != prev[1]:
        t_current[empty[0]][empty[1]] = t_current[empty[0]][empty[1] + 1]
        t_current[empty[0]][empty[1] + 1] = 0
        if get_f(t_current, h) <= min_f:
            min_f = get_f(t_current, h)
            move_empty = [empty[0], empty[1] + 1]
    t_current = reset_current(current)
    # try up
    if empty[0] - 1 >= 0 and empty[0] - 1 != prev[0]:
        t_current[empty[0]][empty[1]] = t_current[empty[0] - 1][empty[1]]
        t_current[empty[0] - 1][empty[1]] = 0
        if get_f(t_current, h) <= min_f:
            min_f = get_f(t_current, h)
            move_empty = [empty[0] - 1, empty[1]]
    t_current = reset_current(current)
    # try down
    if empty[0] + 1 <= 2 and empty[0] + 1 != prev[0]:
        t_current[empty[0]][empty[1]] = t_current[empty[0] + 1][empty[1]]
        t_current[empty[0] + 1][empty[1]] = 0
        if get_f(t_current, h) <= min_f:
            move_empty = [empty[0] + 1, empty[1]]

    # swap empty and move empty pos data
    t = current[move_empty[0]][move_empty[1]]
    current[move_empty[0]][move_empty[1]] = current[empty[0]][empty[1]]
    current[empty[0]][empty[1]] = t
    print("Depth "+str(h+1))
    print_puzzle(current)
    # do recursion
    if is_goal(current):
        print("goal achieved")
    else:
        get_next(current, h + 1, empty)


def start_game():
    print_puzzle(initial)
    get_next(initial, 0)


start_game()

