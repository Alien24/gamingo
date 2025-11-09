from django.shortcuts import render
import random, copy

def generate_sudoku(difficulty="medium"):
    base = 3
    side = base * base

    def pattern(r, c): return (base * (r % base) + r // base + c) % side
    def shuffle(s): return random.sample(s, len(s))
    rBase = range(base)
    rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
    cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
    nums = shuffle(range(1, side + 1))
    board = [[nums[pattern(r, c)] for c in cols] for r in rows]

    if difficulty == "easy":
        empties = random.randint(36, 45)
    elif difficulty == "medium":
        empties = random.randint(46, 55)
    else:
        empties = random.randint(56, 65)

    for p in random.sample(range(side*side), empties):
        board[p // side][p % side] = 0
    return board

def solve_sudoku(board):
    side = 9
    b = copy.deepcopy(board)

    def find_empty():
        for i in range(side):
            for j in range(side):
                if b[i][j] == 0:
                    return i, j
        return None

    def valid(num, pos):
        row, col = pos
        if num in b[row]: return False
        if num in [b[i][col] for i in range(side)]: return False
        box_x, box_y = col // 3, row // 3
        for i in range(box_y*3, box_y*3+3):
            for j in range(box_x*3, box_x*3+3):
                if b[i][j] == num:
                    return False
        return True

    def solve():
        find = find_empty()
        if not find: return True
        row, col = find
        for i in range(1, 10):
            if valid(i, (row, col)):
                b[row][col] = i
                if solve():
                    return True
                b[row][col] = 0
        return False

    solve()
    return b

def sudoku(request):
    # poziom trudności z GET
    difficulty = request.GET.get("level", "medium")
    # jeśli kliknięto "Nowa gra" lub brak parametrów
    if request.GET.get("new") == "1" or True:
        board = generate_sudoku(difficulty)
        solution = solve_sudoku(board)
    return render(request, "main/sudoku.html", {
        "board": board,
        "solution": solution,
        "difficulty": difficulty
    })
