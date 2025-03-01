import tkinter as tk
from tkinter import *

class MainGui:
    def __init__(self):
    def __init__(self, master, **kwargs):
        self.pack(fill=BOTH, expand=YES)
        self.digitsvar = tk.StringVar(value=0)
        self.xnum = tk.DoubleVar()
        self.ynum = tk.DoubleVar()
        self.operator = tk.StringVar(value="+")


if __name__ == "__main__":
    gui = MainGui()

    
