import sys
from graph_utils import * 
# DFS implementation that solves the Arrow Traversal problem
def dfs_arrows(graph, start, goal):
    paths = {}
    paths[start] = None
    visited = set()
    visited.add(start)
    stack = []
    stack.append(start)
    while len(stack) != 0:
        node = stack.pop()
        if node == goal:
            # print('found')
            break
        for next_node in get_edges(graph, node):
            if not next_node in visited:
                # print(node, next_node, stack)
                visited.add(next_node)
                paths[next_node] = node
                stack.append(next_node)
        # visited.remove(node)
    return paths


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("\nInvalid number of arguments. Please include path of input and output files.\n")

    else:
        input_file, output_file = sys.argv[1], sys.argv[2]
        graph = get_graph(input_file)
        # print(graph)
        n, m = len(graph), len(graph[0])
        start, goal = (0,0), (n-1, m-1)
        
        paths = dfs_arrows(graph, start, goal)
        path = trace_path(graph, start, goal, paths)
        # print(paths)
        formated_path = format_path(path)
        # print(path)
        # print(formated_path)
        # test_paths(formated_path, input_file)
        write_file(output_file, formated_path)