"""Script to verify the output solution file.
To run:
    python verifyGraph.py <input_graph_file> <output_soln_file>
Ex: python verifyGraph.py small.txt small-soln.txt
"""
import sys
import re

GRAPH_FILE_NAME = sys.argv[1]
OUTPUT_FILE_NAME = sys.argv[2]
NSIndex, EWIndex = 0, 0  # Movement indices for tracking current node
BullsEye = 'O'

# Get matrix/graph
with open(GRAPH_FILE_NAME) as file:
    next(file)
    graph = [line.split() for line in file]

# Get solution
soln_path_list = open(OUTPUT_FILE_NAME).read().split()

prev_color = None
for i in range(len(soln_path_list)):
    # Boundary check for movement indices
    if (NSIndex >= len(graph) or EWIndex >= len(graph[0])) or (
            EWIndex < 0 or NSIndex < 0):
        raise Exception("Movement Indices out of graph's boundary.")

    node = re.split('(\d+)', soln_path_list[i])
    # Get distance to move
    distance = int(node[1])
    # Get direction to move
    directions = node[2].upper()

    # Check for current path's direction
    current_node = (graph[NSIndex][EWIndex]).upper()
    curr_color, curr_direction = current_node.split("-")

    if (curr_direction != directions):
        # print(curr_direction, directions)
        raise Exception((
            "Invalid intermediate state. "
            "Next node does not lie on path indicated by arrow on current node."
        ))

    if prev_color and prev_color == curr_color:
        raise Exception((
            "Invalid intermediate state. "
            "Subsequent nodes of same colour found in the path."
        ))
    else:
        prev_color = curr_color

    # Move across the graph.
    for direction in list(directions):  # Ex: list(NE) -> [N,E]
        if direction == 'N':
            NSIndex -= distance
        elif direction == 'S':
            NSIndex += distance
        elif direction == 'E':
            EWIndex += distance
        elif direction == 'W':
            EWIndex -= distance
        else:
            raise Exception("Unknown direction found.")


# Final movement indices from above will be bullseye if path is correct
final_node = graph[NSIndex][EWIndex].upper()
if final_node == BullsEye:
    print("Congrats! You hit the BullsEye.")
else:
    print("Oh! You MISSED the target.")
