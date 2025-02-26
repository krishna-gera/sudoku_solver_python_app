import tkinter as tk

class SudokuSolver:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.cells = [[None for _ in range(9)] for _ in range(9)]
        self.create_grid()
        self.create_buttons()

    def create_grid(self):
        for row_block in range(3):
            for col_block in range(3):
                frame = tk.Frame(self.root, bd=2, relief="solid")
                frame.grid(row=row_block, column=col_block, padx=5, pady=5)
                for row in range(3):
                    for col in range(3):
                        entry = tk.Entry(frame, width=3, font=('Arial', 18), justify='center')
                        entry.grid(row=row, column=col, padx=1, pady=1)
                        self.cells[row_block * 3 + row][col_block * 3 + col] = entry

    def create_buttons(self):
        solve_button = tk.Button(self.root, text="Solve", command=self.solve)
        solve_button.grid(row=3, column=1, columnspan=1, pady=10)

    def solve(self):
        board = self.get_board()
        if self.solve_sudoku(board):
            self.update_board(board)
        else:
            tk.messagebox.showerror("Error", "No solution exists")

    def get_board(self):
        board = []
        for row in range(9):
            board_row = []
            for col in range(9):
                value = self.cells[row][col].get()
                board_row.append(int(value) if value else 0)
            board.append(board_row)
        return board

    def update_board(self, board):
        for row in range(9):
            for col in range(9):
                self.cells[row][col].delete(0, tk.END)
                self.cells[row][col].insert(0, str(board[row][col]))

    def solve_sudoku(self, board):
        empty = self.find_empty(board)
        if not empty:
            return True
        row, col = empty

        for num in range(1, 10):
            if self.is_valid(board, num, row, col):
                board[row][col] = num
                if self.solve_sudoku(board):
                    return True
                board[row][col] = 0
        return False

    def find_empty(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    return (row, col)
        return None

    def is_valid(self, board, num, row, col):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        box_row, box_col = row // 3 * 3, col // 3 * 3
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if board[i][j] == num:
                    return False
        return True

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolver(root)
    root.mainloop()