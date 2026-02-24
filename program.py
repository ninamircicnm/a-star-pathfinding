import heapq
import tkinter as tk
from tkinter import simpledialog, messagebox

# A* algorithm implementation
def astar(graph, heuristic, start, goal):

    open_set=[]
    heapq.heappush(open_set, (0 + heuristic.get(start,0), 0, start, [start]))
    closed = set()

    while open_set:
        f, g, current, path = heapq.heappop(open_set)
        if current == goal:
            return path, g
        
        if current in closed:
            continue
        closed.add(current)

        for neighbor, cost in graph.get(current, []):
            if neighbor not in closed:
                new_g = g + cost
                new_f = new_g + heuristic.get(neighbor,0)
                heapq.heappush(open_set, (new_f, new_g, neighbor, path + [neighbor]))
    return None, float('inf')

# GUI - Tkinter

class GraphPlannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("A* Algorithm")
        self.canvas = tk.Canvas(root, width=700, height=500, bg="white")
        self.canvas.pack()

        self.nodes = {}
        self.graph = {}
        self.heuristic = {}
        self.heuristic_texts = {}

        self.node_counter = 0
        self.selected_node = None
        self.start_node = None
        self.goal_node = None

        frame = tk.Frame(root)
        frame.pack(pady=5)

        self.canvas.bind("<Button-1>", self.on_canvas_click)