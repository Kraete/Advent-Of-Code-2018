input = ("G", "M"),("T", "E"),("P", "M"),("V", "L"),("Y", "B"),("K", "Z"),("H", "I"),("D", "U"),("C", "L"),("R", "Z"),("U", "B"),("J", "M"),("M", "E"),("I", "X"),("N", "O"),("S", "F"),("X", "A"),("F", "Q"),("B", "Z"),("Q", "W"),("L", "W"),("O", "Z"),("A", "Z"),("E", "W"),("W", "Z"),("G", "R"),("H", "A"),("A", "W"),("Y", "D"),("O", "A"),("V", "U"),("H", "W"),("K", "F"),("J", "X"),("V", "R"),("Q", "A"),("F", "B"),("G", "P"),("L", "A"),("B", "Q"),("H", "J"),("J", "L"),("F", "E"),("U", "A"),("G", "Q"),("G", "S"),("K", "J"),("N", "B"),("F", "O"),("C", "Z"),("B", "E"),("M", "S"),("A", "E"),("E", "Z"),("K", "I"),("P", "A"),("Y", "L"),("Y", "J"),("G", "N"),("Q", "L"),("D", "X"),("C", "I"),("K", "B"),("N", "F"),("D", "M"),("B", "A"),("U", "J"),("Q", "Z"),("X", "F"),("K", "X"),("U", "E"),("X", "W"),("K", "Q"),("I", "E"),("D", "J"),("P", "I"),("K", "D"),("S", "X"),("C", "R"),("P", "W"),("I", "O"),("S", "O"),("K", "C"),("N", "Q"),("L", "E"),("L", "Z"),("K", "W"),("Y", "A"),("L", "O"),("N", "W"),("R", "W"),("C", "O"),("H", "X"),("V", "Y"),("S", "W"),("V", "E"),("Q", "E"),("P", "H"),("V", "H"),("N", "Z"),("C", "A")
input = [("C", "A"),("C", "F"),("A", "B"),("A", "D"),("B", "E"),("D", "E"),("F", "E")]

#The tree to hold the nodes
tree = []

#A Node class to store parent/child relationships
class Node():
  _value = ''
  _children = []
  _parents = []
  
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

  def __eq__(self, other):
    return self._value == other.get_value()

  def __repr__(self):
    return self._value

  def __str__(self):
    return self._value

#Search the tree recursively to find if a node exists
#Returns the found node else None
def find_node(new_node, tree_node):
  if new_node == tree_node:
    #print('found node ' + str(tree_node))
    new_node = tree_node
    return new_node
  else:
    if tree_node.has_children():
      n = []
      #print('Checking parent ' + str(tree_node) + " for child " + str(new_node))

      for child in tree_node.get_children():
        node = find_node(new_node, child)
        if node:
          return node
          #print('die?')
      return
    else:
      #print('Child not found')
      return

#Populate the tree with correctly linked nodes
def populate_single_root():
  for item in input:
    parent = Node(item[0])
    child = Node(item[1])
    #print('Input ' + str(parent) + "->" + str(child))
    if len(tree) == 0 or parent.get_value() == "V" and parent not in tree:
      #print('Building new tree with ' + str(parent) + "->" + str(child))
      parent.add_child(child)
      child.add_parent(parent)
      tree.append(parent)
    else:
      #print('Checking for parent...')
      for node in tree:
        node = find_node(parent, node)
        if node:
          #print('Setting parent to '+ str(node))
          parent = node
        #print('Checking for child...')
        node = find_node(child, node)
        if node:
          #print('Setting child to '+ str(node))
          child = node
        #print('Adding new link ' + str(parent) + '->' + str(child))
        parent.add_child(child)
        child.add_parent(parent)
    #print('')

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


available = []
completed = []
def get_available_steps(node):
  return node.get_children()

def is_available(step):
  #print(step.get_parents())
  for parent in step.get_parents():
    #print('checking parent: ' + str(parent))
    if parent not in completed:
      return False
  return True

def traverse_tree(tree):
  global available
  for node in tree:
    if len(node.get_parents()) == 0:
      available.append(node)
  available.sort(key=lambda x: str(x))
  traverse_node(available[0])



global count
count = 0

set_len = float(len(tree))
iterator = int(1)
def traverse_node(node):
  global count
  global available
  global iterator
  print("progress: %.2f" % (iterator/set_len))
  iterator += 1

  count += 1

  #print('traversing ' +str(node))
  if node not in completed:
    completed.append(node)

  for step in node.get_children():
    #print('adding available step: '+str(step))
    if step not in available:
      available.append(step)
  available.sort(key=lambda x: str(x))
  
  print('Steps available: ')
  print(available)
  print('Steps completed: ')
  print(completed)

  if len(available):
    #print('checking availability for: ' + str(available[0]))
    while not is_available(available[0]):
      print('not available')
      print(available)
      available = available[1:] + available[:1]
    #print('available')
    traverse_node(available.pop(0))
  else:
    print(''.join(str(x) for x in completed))

print("Traversing")
#traverse_node(tree[0])
traverse_tree(tree)
