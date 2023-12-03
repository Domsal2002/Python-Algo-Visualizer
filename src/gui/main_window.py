import tkinter as tk
from tkinter import ttk, Canvas
import random
import threading

class MainWindow(tk.Frame):
    def __init__(self, master, sorting_algorithms):
        print("Initializing main window")
        super().__init__(master, background="white")
        self.master = master
        self.sorting_algorithms = sorting_algorithms
        self.selected_algorithm = tk.StringVar()
        self.delay = tk.IntVar(value=100)
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

        delay_slider = tk.Scale(delay_frame, from_=0, to=100000, resolution=10, orient=tk.HORIZONTAL, variable=self.delay)
        delay_slider.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=5)

        # Array Size Input
        self.array_size = tk.IntVar(value=10)
        array_size_label = tk.Label(self, text="Array Size:")
        array_size_label.pack(side=tk.LEFT, padx=5, pady=5)
        array_size_entry = tk.Entry(self, textvariable=self.array_size)
        array_size_entry.pack(side=tk.LEFT, padx=5, pady=5)

        # Start Sorting Button
        start_button = tk.Button(self, text="Start Sorting", command=self.start_sorting_thread)
        start_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Canvas for Visualization
        self.canvas = Canvas(self, width=600, height=400)
        self.canvas.pack(fill=tk.BOTH, expand=True)

    def start_sorting_thread(self):
        """Start the sorting process in a separate thread."""
        sorting_thread = threading.Thread(target=self.start_sorting)
        sorting_thread.start()

    def start_sorting(self):
        """Sort the array and update the visualization."""
        array_size = self.array_size.get()
        self.array = [random.randint(1, 100) for _ in range(array_size)]
        self.draw_array()

        #get the selecter sorting algorithm
        sorting_algorithm_name = self.selected_algorithm.get()
        sorting_algorithm = self.sorting_algorithms[sorting_algorithm_name]

        #sort and update the visualization
        for step in sorting_algorithm(self.array):
            self.draw_array(step)
            self.master.update_idletasks()

        # Get the selected sorting algorithm
        sorting_algorithm_name = self.selected_algorithm.get()
        sorting_algorithm = self.sorting_algorithms[sorting_algorithm_name]

        # Sort and update the visualization
        for step in sorting_algorithm(self.array):
            self.draw_array(step)
            self.master.update_idletasks()  # Update the canvas

    def draw_array(self, array=None):
        """Draw the array on the canvas."""
        if array is None:
            array = self.array
        self.canvas.delete("all")  # Clear the canvas
        bar_width = 600 / len(array)
        for i, value in enumerate(array):
            x0 = i * bar_width
            y0 = 400 - value * 4  # Scale the value for better visualization
            x1 = (i + 1) * bar_width
            y1 = 400
            self.canvas.create_rectangle(x0, y0, x1, y1, fill="blue")
