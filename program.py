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

        tk.Button(frame, text="Instructions", command=self.show_instructions).pack(side=tk.LEFT, padx=5)
        tk.Button(frame, text="Set Start", command=self.set_start_node).pack(side=tk.LEFT, padx=5)
        tk.Button(frame, text="Set Goal", command=self.set_goal_node).pack(side=tk.LEFT, padx=5)
        tk.Button(frame, text="Add Heuristics", command=self.add_heuristics).pack(side=tk.LEFT, padx=5)

        self.canvas.bind("<Button-1>", self.on_canvas_click)
    
    def on_canvas_click(self, event):
        clicked = self.find_node(event.x, event.y)

        if clicked:
            if self.selected_node is None:
                self.selected_node = clicked
                self.highlight_node(clicked, "yellow")
            else:
                if clicked != self.selected_node:
                    cost = simpledialog.askfloat("Edge Cost", f"Cost {self.selected_node} → {clicked}:", minvalue=0)
                    if cost is not None:
                        updated = False
                        for i, (node, old_cost) in enumerate(self.graph.get(self.selected_node, [])):
                            if node == clicked:
                                self.graph[self.selected_node][i] = (clicked, cost)
                                updated = True
                                break
                        if not updated:
                            self.graph.setdefault(self.selected_node, []).append((clicked, cost))

                        x1, y1 = self.nodes[self.selected_node]
                        x2, y2 = self.nodes[clicked]
                        mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2

                        items = self.canvas.find_overlapping(mid_x - 10, mid_y - 10, mid_x + 10, mid_y + 10)
                        for item in items:
                            if self.canvas.type(item) == "text":
                                self.canvas.delete(item)

                        self.canvas.create_line(x1, y1, x2, y2, fill="gray", width=2.5)
                        self.canvas.create_text(mid_x, mid_y, text=str(cost), fill="black")

                if self.selected_node == self.start_node:
                    self.highlight_node(self.selected_node, "purple")
                elif self.selected_node == self.goal_node:
                    self.highlight_node(self.selected_node, "green")
                else:
                    self.highlight_node(self.selected_node, "lightblue")

                self.selected_node = None
        else:
            name = f"N{self.node_counter}"
            self.node_counter += 1
            self.nodes[name] = (event.x, event.y)
            self.graph.setdefault(name, [])
            self.canvas.create_oval(event.x - 15, event.y - 15, event.x + 15, event.y + 15, fill="lightblue", outline="black")
            self.canvas.create_text(event.x, event.y, text=name)
    
     # Helper functions for drawing on canvas

    def find_node(self, x, y):
        for name, (nx, ny) in self.nodes.items():
            if (x - nx)**2 + (y - ny)**2 <= 20**2:
                return name
        return None

    def highlight_node(self, name, color):
        x, y = self.nodes[name]
        self.canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill=color, outline="black")
        self.canvas.create_text(x, y, text=name)
    
    def set_start_node(self):
        name = simpledialog.askstring("Start State", "Enter start state name (e.g. N0):")
        if name in self.nodes:
            self.start_node = name
            self.highlight_node(name, "purple")
        else:
            messagebox.showerror("Error", "State does not exist!")

    def set_goal_node(self):
        name = simpledialog.askstring("Goal State", "Enter goal state name (e.g. N7):")
        if name in self.nodes:
            self.goal_node = name
            self.highlight_node(name, "green")
        else:
            messagebox.showerror("Error", "State does not exist!")
    
    def add_heuristics(self):
        if not self.nodes:
            messagebox.showwarning("Warning", "Add states to the board first!")
            return

        win = tk.Toplevel(self.root)
        win.title("Heuristics")

        tk.Label(win, text="Enter heuristic value for each node:").grid(row=0, column=0, columnspan=2, pady=5)

        entries = {}

        for i, name in enumerate(self.nodes.keys(), start=1):
            tk.Label(win, text=name).grid(row=i, column=0, padx=5, pady=2, sticky="e")
            e = tk.Entry(win, width=8)
            e.grid(row=i, column=1, padx=5, pady=2)
            if name in self.heuristic:
                e.insert(0, str(self.heuristic[name]))
            entries[name] = e

        def save_heuristics():
            for n, e in entries.items():
                try:
                    self.heuristic[n] = float(e.get())
                except ValueError:
                    self.heuristic[n] = 1.0
                x, y = self.nodes[n]
                text = f"h={self.heuristic[n]}"

                if n in self.heuristic_texts:
                    self.canvas.delete(self.heuristic_texts[n])

                self.heuristic_texts[n] = self.canvas.create_text(x + 25, y - 10, text=text, fill="darkblue", font=("Arial", 9, "italic"))

            win.destroy()

        tk.Button(win, text="Save", command=save_heuristics).grid(row=len(self.nodes) + 1, column=0, columnspan=2, pady=8)