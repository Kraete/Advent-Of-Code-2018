input = [(267, 196),(76, 184),(231, 301),(241, 76),(84, 210),(186, 243),(251, 316),(265, 129),(142, 124),(107, 134),(265, 191),(216, 226),(67, 188),(256, 211),(317, 166),(110, 41),(347, 332),(129, 91),(217, 327),(104, 57),(332, 171),(257, 287),(230, 105),(131, 209),(110, 282),(263, 146),(113, 217),(193, 149),(280, 71),(357, 160),(356, 43),(321, 123),(272, 70),(171, 49),(288, 196),(156, 139),(268, 163),(188, 141),(156, 182),(199, 242),(330, 47),(89, 292),(351, 329),(292, 353),(290, 158),(167, 116),(268, 235),(124, 139),(116, 119),(142, 259)]
#input = [(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)]
width, height = map(lambda x: max(x), zip(*input))
width = height = 500

def manhattan_distance(p, q):
  return abs(p[0] - q[0]) + abs(p[1] - q[1])

def build_grid():
  return [[0 for x in range(width)] for y in range(height)]
  
def process_coordinate(coords):
  grid = build_grid()
  for y in range(height):
    for x in range(width):
      grid[y][x] = manhattan_distance(coords, (x,y))
  return grid

grids = map(lambda x: process_coordinate(x), input)
result = build_grid()

for g, grid in enumerate(grids):
  for y, line in enumerate(grid):
    for x, index in enumerate(line):
         result[y][x] += grid[x][y]

def print_grid(grid):
  for line in grid:
    print(line)
  print('')

count = 0
for y, line in enumerate(result):
  for x, index in enumerate(line):
    count = count + 1 if result[y][x] < 10000 else count

print(count)
