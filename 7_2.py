input = ("G", "M"),("T", "E"),("P", "M"),("V", "L"),("Y", "B"),("K", "Z"),("H", "I"),("D", "U"),("C", "L"),("R", "Z"),("U", "B"),("J", "M"),("M", "E"),("I", "X"),("N", "O"),("S", "F"),("X", "A"),("F", "Q"),("B", "Z"),("Q", "W"),("L", "W"),("O", "Z"),("A", "Z"),("E", "W"),("W", "Z"),("G", "R"),("H", "A"),("A", "W"),("Y", "D"),("O", "A"),("V", "U"),("H", "W"),("K", "F"),("J", "X"),("V", "R"),("Q", "A"),("F", "B"),("G", "P"),("L", "A"),("B", "Q"),("H", "J"),("J", "L"),("F", "E"),("U", "A"),("G", "Q"),("G", "S"),("K", "J"),("N", "B"),("F", "O"),("C", "Z"),("B", "E"),("M", "S"),("A", "E"),("E", "Z"),("K", "I"),("P", "A"),("Y", "L"),("Y", "J"),("G", "N"),("Q", "L"),("D", "X"),("C", "I"),("K", "B"),("N", "F"),("D", "M"),("B", "A"),("U", "J"),("Q", "Z"),("X", "F"),("K", "X"),("U", "E"),("X", "W"),("K", "Q"),("I", "E"),("D", "J"),("P", "I"),("K", "D"),("S", "X"),("C", "R"),("P", "W"),("I", "O"),("S", "O"),("K", "C"),("N", "Q"),("L", "E"),("L", "Z"),("K", "W"),("Y", "A"),("L", "O"),("N", "W"),("R", "W"),("C", "O"),("H", "X"),("V", "Y"),("S", "W"),("V", "E"),("Q", "E"),("P", "H"),("V", "H"),("N", "Z"),("C", "A")
#input = [("C", "A"),("C", "F"),("A", "B"),("A", "D"),("B", "E"),("D", "E"),("F", "E")]

#The tree to hold the nodes
tree = []

#A Node class to store parent/child relationships
class Node():
  _value = ''
  _work_done = 0
  _process_time = 0
  _children = []
  _parents = []
 
  def work(self):
    self._work_done += 1

  def get_process_time(self):
    return self._process_time
  
  def get_work_done(self):
    return self._work_done

  def get_progress(self):
    return self._work_done / self._process_time

  def get_value(self):
    return self._value

  def has_children(self):
    return len(self._children)

  def get_children(self):
    return self._children

  def get_child(self, value):
    for child in self._children:
      if child == value:
        return child

  def add_child(self, node):
    if node not in self._children:
      self._children.append(node)

  def get_parents(self):
    return self._parents

  def add_parent(self, node):
    if node not in self._parents:
      self._parents.append(node)

  def __init__(self, value):
    self._value = value
    self._children = []
    self._parents = []
    self._work_done = 0
    self._process_time = 60 + (ord(value.lower()) - 96)

  def __eq__(self, other):
    return self._value == other.get_value()

  def __repr__(self):
    return self._value

  def __str__(self):
    return self._value


print("populating...")
for item in input:
  parent = Node(item[0])
  child = Node(item[1])
  parent = next((node for node in tree if parent == node), parent)
  child = next((node for node in tree if child == node), child)
  parent.add_child(child)
  child.add_parent(parent)
  if parent not in tree:
    tree.append(parent)
  if child not in tree:
    tree.append(child)

global completed
available = []
completed = []
workers = []
time = 0
def is_available(node):
  for parent in node.get_parents():
    if parent not in completed:
      return False
  return True

def initialize_workers():
  global available
  global completed
  global workers
  for node in tree:
    if len(node.get_parents()) == 0:
      available.append(node)
  available.sort(key=lambda x: str(x))
  fill_workers()

def fill_workers():
  global available
  global completed
  global workers
  for node in available:
    if len(workers) < 5:
      workers.append(node)
    else:
      break
  for node in workers:
    if node in available:
      available.remove(node)
  available.sort(key=lambda x: str(x))


def process_workers():
  global available
  global completed
  global workers
  global time
  to_process = []
  for node in workers:
    to_process.append(node)
  for node in to_process:
    process_node(node)
  time += 1

def process_node(node):
  global available
  global completed
  global workers
  node.work()
  print("Processing: "+str(node)+' '+str(node.get_work_done())+"/"+str(node.get_process_time()))
  if node.get_progress():
    completed.append(node)
    workers.remove(node)
  for child in node.get_children():
    if is_available(child) and child not in completed and child not in available:
      available.append(child)
  available.sort(key=lambda x: str(x))
  fill_workers()


initialize_workers()
x,y = zip(*input)
while len(completed) < len(set(x+y)):
  debug = str(time)
  for worker in workers:
    debug += ' '+str(worker)
  print(debug)
  print("Available:")
  print(available)
  print("Complete:")
  print(completed)
  print("Workers:")
  print(workers)
  process_workers()
  print('')


print(str(time))
print(''.join(str(x) for x in completed))

