# Romania Map DFS Visualizer

This is a Python program that visualizes the Depth-First Search (DFS) algorithm on the map of Romania. It uses the Tkinter library for creating a graphical user interface (GUI) and provides an interactive visualization of the DFS algorithm as it searches for a path between two cities.

## Prerequisites

- Python 3.x
- Tkinter library (usually included with Python)

## How to Run

1. Make sure you have Python installed on your system.
2. Clone the repository or download the `romania_map_dfs.py` file.
3. Open a terminal or command prompt and navigate to the directory containing the `romania_map_dfs.py` file.
4. Run the following command:


5. The GUI window titled "Romania Map DFS Visualizer" will open.
6. Select a source city and a destination city from the dropdown menus.
7. Click the "Submit" button to start the visualization.
8. The program will animate the DFS algorithm's progress on the map of Romania, highlighting the visited cities and the final path when found.

## How it Works

The program represents the map of Romania as a dictionary where each city is a key, and its neighboring cities are the corresponding values. The DFS algorithm is then applied to this graph-like structure to find a path from the source city to the destination city.

The visualization uses Tkinter to create a graphical interface. The map is drawn using circles representing cities, lines representing connections between cities, and text labels for city names. The algorithm's progress is displayed by highlighting the visited cities in gray color.

When the algorithm finds the destination city, the final path is highlighted in blue color.

## Customization

If you want to modify the map or add more cities, you can update the `romania_map` dictionary at the beginning of the code. Each city is a key, and its neighbors are specified as a list of values.

You can also customize the colors used for visualization by modifying the following constants defined in the code:

- `COLOR_INITIAL`: Color of the initial city circles (default: "white").
- `COLOR_VISITED`: Color used to highlight visited cities during the algorithm's progress (default: "dim gray").
- `COLOR_FINAL`: Color used to highlight the final path (default: "blue").

Additionally, you can adjust the coordinates of the cities on the map by modifying the `get_city_coordinates` function. The coordinates are defined as dictionaries with city names as keys and X and Y coordinates as values.

## Contributions

Contributions to this project are welcome. If you find any issues or want to enhance the functionality, feel free to open an issue or submit a pull request.

## License

This code is released under the MIT License. You can find the details in the [LICENSE](LICENSE) file.
