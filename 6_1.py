input = [(267, 196),(76, 184),(231, 301),(241, 76),(84, 210),(186, 243),(251, 316),(265, 129),(142, 124),(107, 134),(265, 191),(216, 226),(67, 188),(256, 211),(317, 166),(110, 41),(347, 332),(129, 91),(217, 327),(104, 57),(332, 171),(257, 287),(230, 105),(131, 209),(110, 282),(263, 146),(113, 217),(193, 149),(280, 71),(357, 160),(356, 43),(321, 123),(272, 70),(171, 49),(288, 196),(156, 139),(268, 163),(188, 141),(156, 182),(199, 242),(330, 47),(89, 292),(351, 329),(292, 353),(290, 158),(167, 116),(268, 235),(124, 139),(116, 119),(142, 259)]
#input = [(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)]
width = height = 500

def manhattan_distance(p, q):
  return abs(p[0] - q[0]) + abs(p[1] - q[1])

def build_grid():
  return [[-1 for x in range(width)] for y in range(height)]
  
def process_coordinate(coords):
  grid = build_grid()
  for y in range(height):
    for x in range(width):
      grid[y][x] = manhattan_distance(coords, (x,y))
  return grid

grids = map(lambda x: process_coordinate(x), input)
comp = build_grid()
result = build_grid()

for g, grid in enumerate(grids):
  for y, line in enumerate(grid):
    for x, index in enumerate(line):
       if grid[y][x] == comp[y][x]:
         result[y][x] = -1 
       if grid[y][x] < comp[y][x] or comp[y][x] == -1:
         comp[y][x] = grid[y][x]
         result[y][x] = g

def print_grid(grid):
  for line in grid:
    print(line)
  print('')

def edges(grid):
  return grid[0] + grid[height-1] + list(zip(*grid)[0]) + list(zip(*grid)[height-1])

output = {}
for i in range(0, len(input)):
  if i not in edges(result):
    output[i]= sum(x.count(i) for x in result)

print(output[max(output, key=output.get)])
