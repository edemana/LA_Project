import tkinter as tk
from tkinter import ttk
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

class LinearAlgebraSolver:
    def __init__(self, master):
        self.master = master
        master.title("Linear Algebra Solver")
        master.configure(bg='#000000')
        
        # Apply a theme
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure styles
        style.configure('TFrame', background='#f0f0f0')
        style.configure('TButton', background='#4CAF50', foreground='white', font=('Arial', 10, 'bold'))
        style.configure('TLabel', background='#f0f0f0', font=('Arial', 11))
        
        # Create main frame
        self.main_frame = ttk.Frame(master, padding="20")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weight to make it responsive
        self.main_frame.grid_columnconfigure(0, weight=2)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure(4, weight=1)
        
        # Create and place widgets
        self.create_widgets()
        
    def create_widgets(self):
        # Input area
        ttk.Label(self.main_frame, text="Enter augmented matrix [A | b]:").grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
        self.matrix_input = tk.Text(self.main_frame, height=5, width=40, font=('Courier', 10), bg='#ffffff', relief=tk.SUNKEN)
        self.matrix_input.grid(row=1, column=0, columnspan=2, pady=5, sticky=(tk.W, tk.E))
        
        # Solve buttons
        ttk.Button(self.main_frame, text="Solve Ax = 0", command=self.solve_homogeneous).grid(row=2, column=0, pady=10, padx=(0, 5), sticky=tk.W)
        ttk.Button(self.main_frame, text="Solve Ax = b", command=self.solve_nonhomogeneous).grid(row=2, column=1, pady=10, padx=(5, 0), sticky=tk.E)
        
        # Results display
        ttk.Label(self.main_frame, text="Solution:").grid(row=3, column=0, sticky=tk.W, pady=(10, 5))
        self.solution_display = tk.Text(self.main_frame, height=5, width=40, font=('Courier', 10), bg='#ffffff', relief=tk.SUNKEN, state='disabled')
        self.solution_display.grid(row=4, column=0, columnspan=2, pady=5, sticky=(tk.W, tk.E))
        
        # 3D plot
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.main_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=2, rowspan=5, padx=(20, 0), sticky=(tk.W, tk.E, tk.N, tk.S))

    def solve_homogeneous(self):
        # Implement solution for Ax = 0
        pass

    def solve_nonhomogeneous(self):
        # Implement solution for Ax = b
        pass

    def plot_solution(self, solution):
        # Implement 3D plotting of solution
        pass

root = tk.Tk()
root.geometry("800x500")  # Set initial window size
app = LinearAlgebraSolver(root)
root.mainloop()
