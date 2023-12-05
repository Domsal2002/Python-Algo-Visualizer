import tkinter as tk
from tkinter import ttk
import random
import time
from algorithms.bubble_sort import bubble_sort
from algorithms.merge_sort import merge_sort
from algorithms.quick_sort import quick_sort

class MainWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master, background="#303030")
        self.master = master
        self.selected_algorithm = tk.StringVar()
        self.delay = tk.IntVar(value=0)
        self.array_size = tk.IntVar(value=5)
        self.master.minsize(1000, 700)
        self.create_widgets()

    def create_widgets(self):
        self.master.title("Sorting Algorithm Visualizer")
        self.pack(fill=tk.BOTH, expand=True)

        # Styles
        style = ttk.Style()
        style.configure('TButton', font=('Helvetica', 12))
        style.configure('TLabel', font=('Helvetica', 12), background="#303030", foreground="white")
        style.configure('TScale', font=('Helvetica', 12))

        # Algorithm selection frame
        algorithm_frame = tk.Frame(self, bg="#303030")
        algorithm_frame.pack(fill=tk.X, padx=10, pady=5)

        algorithm_label = ttk.Label(algorithm_frame, text="Select Algorithm: ")
        algorithm_label.pack(side=tk.LEFT, padx=5)

        algorithm_dropdown = ttk.Combobox(algorithm_frame, textvariable=self.selected_algorithm, values=['Bubble Sort', 'Merge Sort', 'Quick Sort'], state="readonly")
        algorithm_dropdown.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        algorithm_dropdown.current(0)

        # Delay adjustment frame with dynamic label
        delay_frame = tk.Frame(self, bg="#303030")
        delay_frame.pack(fill=tk.X, padx=10, pady=5)

        self.delay_label_var = tk.StringVar()
        self.delay_label_var.set(f"Delay: {self.delay.get()} ms")
        delay_label = ttk.Label(delay_frame, textvariable=self.delay_label_var)
        delay_label.pack(side=tk.LEFT, padx=5)

        delay_slider = ttk.Scale(delay_frame, from_=0, to=100, orient=tk.HORIZONTAL, variable=self.delay)
        delay_slider.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        delay_slider.bind("<Motion>", self.update_delay_label)

        # Array size adjustment with dynamic label
        array_size_frame = tk.Frame(self, bg="#303030")
        array_size_frame.pack(fill=tk.X, padx=10, pady=5)

        self.array_size_label_var = tk.StringVar()
        self.array_size_label_var.set(f"Array Size: {self.array_size.get()}")
        array_size_label = ttk.Label(array_size_frame, textvariable=self.array_size_label_var)
        array_size_label.pack(side=tk.LEFT, padx=5)

        array_size_scale = ttk.Scale(array_size_frame, from_=1, to=1000, variable=self.array_size)
        array_size_scale.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        array_size_scale.bind("<Motion>", self.update_array_size_label)

        # Start button
        start_button = ttk.Button(self, text="Start Sorting", command=self.start_sorting)
        start_button.pack(pady=10)

        # Canvas for visualization
        self.canvas = tk.Canvas(self, width=1000, height=500, bg='#303030')
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

    def update_delay_label(self, event=None):
        self.delay_label_var.set(f"Delay: {self.delay.get()} ms")

    def update_array_size_label(self, event=None):
        self.array_size_label_var.set(f"Array Size: {self.array_size.get()}")

    def start_sorting(self):
        sorting_algorithms = {'Bubble Sort': bubble_sort, 'Merge Sort': merge_sort, 'Quick Sort': quick_sort}
        array_size = self.array_size.get()
        self.array = [random.randint(1, 100) for _ in range(array_size)]
        self.draw_array(self.array)

        sorting_algorithm = sorting_algorithms[self.selected_algorithm.get()]
        for array_state, change_indices in sorting_algorithm(self.array):
            self.draw_array(array_state, change_indices)
            self.master.update_idletasks()
            time.sleep(self.delay.get() / 1000)

    def draw_array(self, array, change_indices=None):
        self.canvas.delete("all")
        bar_width = 1000 / len(array)
        canvas_height = 500
        max_value = max(array)

        for i, value in enumerate(array):
            x0 = i * bar_width
            y0 = canvas_height - (value / max_value) * canvas_height
            x1 = (i + 1) * bar_width
            y1 = canvas_height
            color = "red" if change_indices and i in change_indices else "blue"
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="")

root = tk.Tk()
app = MainWindow(root)
app.mainloop()