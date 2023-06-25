# import time
# import tkinter as tk
# import random

# # Define the Romania map as a dictionary of cities and their neighbors
# romania_map = {
#     "Arad": ["Zerind", "Sibiu", "Timisoara"],
#     "Zerind": ["Oradea", "Arad"],
#     "Oradea": ["Zerind", "Sibiu"],
#     "Sibiu": ["Arad", "Oradea", "Fagaras", "Rimnicu Vilcea"],
#     "Timisoara": ["Arad", "Lugoj"],
#     "Lugoj": ["Timisoara", "Mehadia"],
#     "Mehadia": ["Lugoj", "Drobeta"],
#     "Drobeta": ["Mehadia", "Craiova"],
#     "Craiova": ["Drobeta", "Rimnicu Vilcea", "Pitesti"],
#     "Rimnicu Vilcea": ["Sibiu", "Craiova", "Pitesti"],
#     "Fagaras": ["Sibiu", "Bucharest"],
#     "Pitesti": ["Rimnicu Vilcea", "Craiova", "Bucharest"],
#     "Bucharest": ["Fagaras", "Pitesti", "Giurgiu", "Urziceni"],
#     "Giurgiu": ["Bucharest"],
#     "Urziceni": ["Bucharest", "Hirsova", "Vaslui"],
#     "Hirsova": ["Urziceni", "Eforie"],
#     "Eforie": ["Hirsova"],
#     "Vaslui": ["Urziceni", "Iasi"],
#     "Iasi": ["Vaslui", "Neamt"],
#     "Neamt": ["Iasi"]
# }

# # Define the colors for visualization
# COLOR_INITIAL = "white"
# COLOR_VISITED = "dim gray"
# COLOR_FINAL = "blue"

# # Define the GUI application


# class RomaniaMapDFS:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.title("Romania Map DFS Visualizer")
#         self.canvas = tk.Canvas(self.root, width=650, height=700)
#         self.canvas.pack(side=tk.LEFT)
#         # self.stack_display = tk.Text(self.root, width=30, height=30)
#         # self.stack_display.pack(side=tk.RIGHT )
#         # self.stack_display.pack(padx=20)
#         self.text = tk.Label(self.root, text="Enter source and\ndestination cities: ",)
#         self.text.pack()
#         self.source_entry = tk.Entry(self.root,border=  2)
#         self.source_entry.pack(pady=5)
#         self.dest_entry = tk.Entry(self.root)
#         self.dest_entry.pack(pady=5)
#         self.submit_button = tk.Button(
#             self.root, text="Submit", command=self.start_visualization)
#         self.submit_button.pack(pady=2)
#         self.current_state = None

#     def start_visualization(self):
#         source = self.source_entry.get()
#         destination = self.dest_entry.get()
#         if source and destination:
#             self.visualize_dfs(source, destination)

#     def visualize_dfs(self, source, destination):
#         stack = list[random.choice([(source, [source])])]
#         visited = set()
#         while stack:
#             current, path = stack.pop()
#             self.current_state = current
#             self.draw_map()

#             #self.update_stack_display(stack)
#             #self.stack_display.pack(padx=100)

#             self.canvas.update()
#             time.sleep(0.5)  

#             if current == destination:
#                 self.highlight_path(path)
#                 break
            
#             if current not in visited:
#                 visited.add(current)
#                 for neighbor in romania_map[current]:
#                     if neighbor not in visited:
#                         stack.append((neighbor, path + [neighbor]))

#     def draw_map(self):
#         self.canvas.delete("all")
#         max_x = 0
#         max_y = 0
#         for city, neighbors in romania_map.items():
#             x, y = self.get_city_coordinates(city)
#             max_x = max(max_x, x)
#             max_y = max(max_y, y)
#             fill_color = COLOR_INITIAL
#             if city == self.current_state:
#                 fill_color = COLOR_VISITED
#             self.canvas.create_oval(
#                 x - 10, y - 10, x + 10, y + 10, fill=fill_color)
#             self.canvas.create_text(x+15, y+15, text=city)
#             for neighbor in neighbors:
#                 x2, y2 = self.get_city_coordinates(neighbor)
#                 self.canvas.create_line(x, y, x2, y2)

#         self.canvas.config(width=max_x + 60, height=max_y + 30)

#     # def update_stack_display(self, stack):
#     #     self.stack_display.delete("1.0", tk.END)
#     #     self.stack_display.insert(tk.END, "Stack Contents:\n")
#     #     for item in stack[::-1]:
#     #         self.stack_display.insert(tk.END, f"{item[0]}: {item[1]}\n\n")


#     def get_city_coordinates(self, city):         
         
#         x = {
#         "Arad": 100, "Zerind": 300, "Oradea": 450, "Sibiu": 400, "Timisoara": 100,
#         "Lugoj": 300, "Mehadia": 500, "Drobeta": 600, "Craiova": 700, "Rimnicu Vilcea": 600,
#         "Fagaras": 700, "Pitesti": 800, "Bucharest": 900, "Giurgiu": 920, "Urziceni": 900,
#         "Hirsova": 1000, "Eforie": 1100, "Vaslui": 900, "Iasi": 1000, "Neamt": 1100
#          }
#         y = {
#         "Arad": 300, "Zerind": 200, "Oradea": 150, "Sibiu": 320, "Timisoara": 400,
#         "Lugoj": 400, "Mehadia": 500, "Drobeta": 500, "Craiova": 600, "Rimnicu Vilcea": 400,
#         "Fagaras": 300, "Pitesti": 500, "Bucharest": 500, "Giurgiu": 600, "Urziceni": 400,
#         "Hirsova": 600, "Eforie": 700, "Vaslui": 300, "Iasi": 300, "Neamt": 200
#         }
#         return x[city], y[city]

#     def highlight_path(self, path):
#         for i in range(len(path) - 1):
#             city1 = path[i]
#             city2 = path[i + 1]
#             x1, y1 = self.get_city_coordinates(city1)
#             x2, y2 = self.get_city_coordinates(city2)
#             self.canvas.create_line(x1, y1, x2, y2, fill=COLOR_FINAL, width=2)
#             self.canvas.create_oval(
#                 x1 - 10, y1 - 10, x1 + 10, y1 + 10, fill=COLOR_VISITED)
#             self.canvas.create_oval(
#                 x2 - 10, y2 - 10, x2 + 10, y2 + 10, fill=COLOR_FINAL)

#     def run(self):
#         self.draw_map()
#         self.root.mainloop()


# app = RomaniaMapDFS()
# app.run()

import time
import tkinter as tk
import random

# Define the Romania map as a dictionary of cities and their neighbors
romania_map = {
    "Arad": ["Zerind", "Sibiu", "Timisoara"],
    "Zerind": ["Oradea", "Arad"],
    "Oradea": ["Zerind", "Sibiu"],
    "Sibiu": ["Arad", "Oradea", "Fagaras", "Rimnicu Vilcea"],
    "Timisoara": ["Arad", "Lugoj"],
    "Lugoj": ["Timisoara", "Mehadia"],
    "Mehadia": ["Lugoj", "Drobeta"],
    "Drobeta": ["Mehadia", "Craiova"],
    "Craiova": ["Drobeta", "Rimnicu Vilcea", "Pitesti"],
    "Rimnicu Vilcea": ["Sibiu", "Craiova", "Pitesti"],
    "Fagaras": ["Sibiu", "Bucharest"],
    "Pitesti": ["Rimnicu Vilcea", "Craiova", "Bucharest"],
    "Bucharest": ["Fagaras", "Pitesti", "Giurgiu", "Urziceni"],
    "Giurgiu": ["Bucharest"],
    "Urziceni": ["Bucharest", "Hirsova", "Vaslui"],
    "Hirsova": ["Urziceni", "Eforie"],
    "Eforie": ["Hirsova"],
    "Vaslui": ["Urziceni", "Iasi"],
    "Iasi": ["Vaslui", "Neamt"],
    "Neamt": ["Iasi"]
}

# Define the colors for visualization
COLOR_INITIAL = "white"
COLOR_VISITED = "dim gray"
COLOR_FINAL = "blue"

# Define the GUI application


class RomaniaMapDFS:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Romania Map DFS Visualizer")
        self.canvas = tk.Canvas(self.root, width=650, height=700)
        self.canvas.pack(side=tk.LEFT)
        self.source_label = tk.Label(self.root, text="Source City:")
        self.source_label.pack(pady=5)
        self.source_var = tk.StringVar(self.root)
        self.source_dropdown = tk.OptionMenu(self.root, self.source_var, *romania_map.keys())
        self.source_dropdown.pack(pady=5)
        self.dest_label = tk.Label(self.root, text="Destination City:")
        self.dest_label.pack(pady=5)
        self.dest_var = tk.StringVar(self.root)
        self.dest_dropdown = tk.OptionMenu(self.root, self.dest_var, *romania_map.keys())
        self.dest_dropdown.pack(pady=5)
        self.submit_button = tk.Button(self.root, text="Submit", command=self.start_visualization)
        self.submit_button.pack(pady=5)
        self.current_state = None

    def start_visualization(self):
        source = self.source_var.get()
        destination = self.dest_var.get()
        if source and destination:
            self.visualize_dfs(source, destination)

    def visualize_dfs(self, source, destination):
        stack = [(source, [source])]
        visited = set()
        while stack:
            current, path = stack.pop()
            self.current_state = current
            self.draw_map()

            self.canvas.update()
            time.sleep(0.5)

            if current == destination:
                self.highlight_path(path)
                break

            if current not in visited:
                visited.add(current)
                neighbors = romania_map[current]
                random.shuffle(neighbors)  # Shuffle the neighbors randomly
                for neighbor in neighbors:
                    if neighbor not in visited:
                        stack.append((neighbor, path + [neighbor]))

    def draw_map(self):
        self.canvas.delete("all")
        max_x = 0
        max_y = 0
        for city, neighbors in romania_map.items():
            x, y = self.get_city_coordinates(city)
            max_x = max(max_x, x)
            max_y = max(max_y, y)
            fill_color = COLOR_INITIAL
            if city == self.current_state:
                fill_color = COLOR_VISITED
            self.canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill=fill_color)
            self.canvas.create_text(x + 15, y + 15, text=city)
            for neighbor in neighbors:
                x2, y2 = self.get_city_coordinates(neighbor)
                self.canvas.create_line(x, y, x2, y2)

        self.canvas.config(width=max_x + 60, height=max_y + 30)

    def get_city_coordinates(self, city):
        x = {
            "Arad": 100, "Zerind": 300, "Oradea": 450, "Sibiu": 400, "Timisoara": 100,
            "Lugoj": 300, "Mehadia": 500, "Drobeta": 600, "Craiova": 700, "Rimnicu Vilcea": 600,
            "Fagaras": 700, "Pitesti": 800, "Bucharest": 900, "Giurgiu": 920, "Urziceni": 900,
            "Hirsova": 1000, "Eforie": 1100, "Vaslui": 900, "Iasi": 1000, "Neamt": 1100
        }
        y = {
            "Arad": 300, "Zerind": 200, "Oradea": 150, "Sibiu": 320, "Timisoara": 400,
            "Lugoj": 400, "Mehadia": 500, "Drobeta": 500, "Craiova": 600, "Rimnicu Vilcea": 400,
            "Fagaras": 300, "Pitesti": 500, "Bucharest": 500, "Giurgiu": 600, "Urziceni": 400,
            "Hirsova": 600, "Eforie": 700, "Vaslui": 300, "Iasi": 300, "Neamt": 200
        }
        return x[city], y[city]

    def highlight_path(self, path):
        for i in range(len(path) - 1):
            city1 = path[i]
            city2 = path[i + 1]
            x1, y1 = self.get_city_coordinates(city1)
            x2, y2 = self.get_city_coordinates(city2)
            self.canvas.create_line(x1, y1, x2, y2, fill=COLOR_FINAL, width=2)
            self.canvas.create_oval(x1 - 10, y1 - 10, x1 + 10, y1 + 10, fill=COLOR_VISITED)
            self.canvas.create_oval(x2 - 10, y2 - 10, x2 + 10, y2 + 10, fill=COLOR_FINAL)

    def run(self):
        self.draw_map()
        self.root.mainloop()


app = RomaniaMapDFS()
app.run()
