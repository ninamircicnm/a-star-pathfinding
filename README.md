# A* Pathfinding Algorithm Visualizer

An interactive graph-based pathfinding application built with Python and Tkinter, implementing the A* search algorithm to find optimal paths between nodes.

---

## About the Project

The goal of this project was to move away from classic terminal-based implementations and instead create an interactive visual experience. Using Python and the Tkinter library, the application allows users to build a graph from scratch, define start and goal states, assign heuristic values, and visually watch the A* algorithm find the optimal path.

---

## Features

- Interactive canvas for adding nodes and edges
- Custom edge cost input
- Heuristic value assignment per node
- Visual distinction between start (purple), goal (green), and regular (light blue) nodes
- Optimal path highlighted in green after algorithm execution
- Reset functionality to clear the board without restarting the app
- Built-in instructions accessible via the Instructions button

---

## Technologies Used

- **Python 3**
- **Tkinter** — built-in Python GUI library
- **heapq** — Python standard library for priority queue (min-heap)

No additional installations required — everything runs on the Python standard library.

---

## How to Run

1. Make sure Python 3 is installed on your system
2. Clone the repository:
   ```bash
   git clone https://github.com/ninamircicnm/a-star-pathfinding.git
   ```
3. Navigate to the project folder:
   ```bash
   cd a-star-pathfinding
   ```
4. Run the program:
   ```bash
   python program.py
   ```

---

## How to Use

1. **Add states** — click anywhere on the board to create a new node
2. **Create edges** — click one node, then another to create an edge and enter the cost
3. **Set start and goal** — use the *Set Start* and *Set Goal* buttons (start = purple, goal = green)
4. **Add heuristics** — click *Add Heuristics* and enter h(n) values for each node; defaults to 1.0 if left empty
5. **Run A\*** — click *Run A\** to find and display the optimal path
6. **View result** — the optimal path is shown in a dialog and highlighted in green on the graph
7. **Reset** — click *Reset Board* to start over without restarting the application

---

## Algorithm

The A* algorithm is implemented as a standalone function `astar(graph, heuristic, start, goal)`.

It uses a **min-heap (priority queue)** and evaluates each node using the formula:

```
f(n) = g(n) + h(n)
```

where:
- `g(n)` — actual cost from the start node to the current node
- `h(n)` — heuristic estimate of the distance from the current node to the goal

The algorithm explores nodes in order of lowest `f` value and terminates when the goal node is reached, returning the optimal path and total cost.

---

## Project Structure

```
a-star-pathfinding/
├── program.py        # Main application — A* algorithm + Tkinter GUI
└── README.md         # Project documentation
```

---

## Author

Nina Mirčić  
Faculty of Organization and Informatics, Varaždin  
University of Zagreb, 2025
