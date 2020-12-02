
def get_graph(filename):
    with open(filename, 'r') as fp:
        text_data = fp.readlines()
        data = [line_string.rstrip().split(' ') for line_string in text_data]
        # print(data)
        # print(data[0])# size
        graph_matrix = [] #[[None]*int(data[0][1])]*int(data[0][0])
        # print(graph_matrix)
        for c_idx, line in enumerate(data[1:]):
            row = []
            for r_idx, item in enumerate(line):
                item_data = item.split('-')
                if item_data[0]=='O':
                    item_data.append("*")
                
                arrow = {'type': item_data[0], 'direction': item_data[1]}
                # print(c_idx, r_idx, arrow)
                row.append( arrow)
            graph_matrix.append(row)
        # print(graph_matrix)
        for r in range(0, len(graph_matrix)):
            for c in range(0, len(graph_matrix[0])):
                node = (r, c)
                graph_matrix[r][c]['edges'] = connect_edges(graph_matrix, node)
        # graph = {}
        # {(i, j) : dict({'type': 'type', 'direction': 'dir', 'edges': set( (x,y),... ) })
        return graph_matrix

def connect_edges(graph, node):
    edges = set()
    i, j = node
    direction = graph[i][j]['direction'] 
    curr_type = graph[i][j]['type']
    r, c = node
    new_node = (r, c) 
    while True:
        r, c = get_next(graph, new_node, direction)
        new_node = (r, c) 
        # print(r, c)
        if r == None or c == None or not (0 <= r < len(graph) and 0 <= c < len(graph[0])):
            break
        if curr_type != graph[r][c]['type']:
            edges.add(new_node)
    # print(node, edges)
    return edges

def get_next(graph, node, direction):
    i, j = node
    dir_map = {
        'N': (i-1, j),
        'NE': (i-1, j+1),
        'NW': (i-1, j-1),
        'S': (i+1, j),
        'SE': (i+1, j+1),
        'SW':(i+1, j-1),
        'E' : (i, j+1),
        'W': (i, j-1),
        '*': (None, None),
    }
    return dir_map[direction]

def get_edges(graph, node):
    i, j = node
    return graph[i][j]['edges']

# funtions that reconstructs the minimum path from all explored paths
def trace_path(grid, start, end, paths):
    # if end is not in paths it means it can not be reached from start
    if not end in paths:
        return []
    temp = end
    path = []
    # Retrace path
    while temp != None:
        i, j = temp
        direction = grid[i][j]['direction']
        path.append( (temp, direction) )
        temp = paths[temp]
        
        
    # Reverse path and return it 
    path.reverse()
    return path

def format_path(path):
    node, direction = path[0]
    formated_path = []
    for next_node, next_dir in path[1:]:
        r, c = node
        n_r, n_c = next_node
        num = max(abs(n_r - r), abs(n_c - c))
        item = ''+str(num)+direction
        formated_path.append(item)
        node, direction = next_node, next_dir

    return ' '.join(formated_path)

def write_file(filename, path_str):
    with open(filename, 'w+') as fp:
        fp.write(path_str)
# def test_paths(path_str, filename):
#     solution = {
#         'small.txt':'2S 5SE 7N 2W 1W 1SE 1NE 2E 7S 1NE 5NW 2W 3SE 2NE 2SE 3S',
#         'rect.txt': '8S 9E 1SW 2W 7N 3SE 1SE 2N 2NW 2NW 7E 1E 1SW 5S 2E 3SW 3W 4NW 2NW 14E 1NW 2S 2NE 1N 1SW 7SW 2N 1NW 2W 7W 1SE 7N 1E 2SE 5SE 3N 4E 5E 5S 1E',
#         'small':'2S 5SE 7N 2W 1W 1SE 1NE 2E 7S 1NE 5NW 2W 3SE 2NE 2SE 3S',
#         'rect': '8S 9E 1SW 2W 7N 3SE 1SE 2N 2NW 2NW 7E 1E 1SW 5S 2E 3SW 3W 4NW 2NW 14E 1NW 2S 2NE 1N 1SW 7SW 2N 1NW 2W 7W 1SE 7N 1E 2SE 5SE 3N 4E 5E 5S 1E',
    
#     }
#     res = filename in solution and path_str == solution[filename]
#     if not res:
#         print('exp',solution[filename])
#         print('act', path_str)
#     return res