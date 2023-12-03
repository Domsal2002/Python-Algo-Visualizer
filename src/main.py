import tkinter as tk
from gui.main_window import MainWindow
from algorithms.bubble_sort import bubble_sort
from algorithms.quick_sort import quick_sort
from algorithms.merge_sort import merge_sort

def main():
    root = tk.Tk()
    sorting_algorithms = {
        'Bubble Sort': bubble_sort,
        'Quick Sort': quick_sort,
        'Merge Sort': merge_sort
        # add other algorithms to the dictionary
    }
    app = MainWindow(root, sorting_algorithms)
    app.mainloop()

if __name__ == "__main__":
    main()