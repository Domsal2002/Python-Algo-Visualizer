import tkinter as tk
from tkinter import ttk, Canvas
import random
import time

class MainWindow(tk.Frame):
    def __init__(self, master, sorting_algorithms):
        print("Initializing main window")
        super().__init__(master, background="white")
        self.master = master
        self.sorting_algorithms = sorting_algorithms
        self.selected_algorithm = tk.StringVar()
        self.delay = tk.IntVar(value=0)
        self.array = []
        self.master.minsize(1000, 700)
        self.create_widgets()

    def create_widgets(self):
        print("Creating widgets")
        self.master.title("Sorting Algorithm Visualizer")
        self.pack(fill=tk.BOTH, expand=True)

        # Dropdown menu for selecting the sorting algorithm
        algorithm_frame = tk.Frame(self)
        algorithm_frame.pack(fill=tk.X, expand=True)

        algorithm_label = tk.Label(algorithm_frame, text="Select Algorithm: ")
        algorithm_label.pack(side=tk.LEFT, padx=5, pady=5)

        algorithm_dropdown = ttk.Combobox(algorithm_frame, textvariable=self.selected_algorithm, values=list(self.sorting_algorithms.keys()))
        algorithm_dropdown.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=5)
        algorithm_dropdown.current(0)

        # Slider for adjusting delay
        delay_frame = tk.Frame(self)
        delay_frame.pack(fill=tk.X, expand=True)

        delay_label = tk.Label(delay_frame, text="Delay (in ms): ")
        delay_label.pack(side=tk.LEFT, padx=5, pady=5)
        
        delay_slider = tk.Scale(delay_frame, from_=0, to=100, resolution=10 , orient=tk.HORIZONTAL, variable=self.delay)
        delay_slider.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=5)

        # Array Size Input
        self.array_size = tk.IntVar(value=5)
        array_size_label = tk.Label(self, text="Array Size:")
        array_size_label.pack(side=tk.LEFT, padx=5, pady=5)
        array_size_scale = tk.Scale(self, from_=1, to=1000, variable=self.array_size, label="Array Size") #creates the sliders
        array_size_scale.pack(side=tk.LEFT, padx=5, pady=5) #slider customization

        # Start Sorting Button
        start_button = tk.Button(self, text="Start Sorting", command=self.start_sorting)
        start_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Canvas for Visualization
        self.canvas = Canvas(self, width=1000, height=800) #drawing canvas
        self.canvas.pack(fill=tk.BOTH, expand=True)

    def start_sorting(self):
        """Sort the array and update the visualization."""
        array_size = self.array_size.get()
        self.array = [random.randint(1, 100) for _ in range(array_size)]
        self.draw_array(self.array)

        #get the selecter sorting algorithm
        sorting_algorithm_name = self.selected_algorithm.get()
        sorting_algorithm = self.sorting_algorithms[sorting_algorithm_name]

        #sort and update the visualization
        for array_state, change_indices in sorting_algorithm(self.array):
            self.draw_array(array_state, change_indices)
            self.master.update_idletasks()
            time.sleep(self.delay.get()/1000)

        # Get the selected sorting algorithm
        sorting_algorithm_name = self.selected_algorithm.get()
        sorting_algorithm = self.sorting_algorithms[sorting_algorithm_name]

        for array_state, change_indices in sorting_algorithm(self.array):
            self.draw_array(array_state, change_indices)
            self.master.update_idletasks()
            time.sleep(self.delay.get()/1000)

        # Sort and update the visualization
        for step in sorting_algorithm(self.array):
            self.draw_array(step)
            self.master.update_idletasks()  # Update the canvas

    def draw_array(self, array, change_indices=None):
        """Draw the array on the canvas."""
        self.canvas.delete("all")
        bar_width = 1000 / len(array)  # Adjusted for canvas width
        for i, value in enumerate(array):
            x0 = i * bar_width
            y0 = 800 - value * 8  # Adjusted for canvas height
            x1 = (i + 1) * bar_width
            y1 = 800
            color = "red" if change_indices and i in change_indices else "blue"
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
