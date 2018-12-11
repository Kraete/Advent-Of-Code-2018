tree = []
node_map = []

class Node():
  _name = ''
  _children = []
  _parents = []
  _metadata = []
  _header = []
  _index = 0

  def get_name(self):
    return self._name

  def get_children(self):
    return self._children

  def add_child(self, node):
    if node not in self._children:
      self._children.append(node)

  def get_parents(self):
    return self._parents

  def add_parent(self, node):
    if node not in self._parents:
      self._parents.append(node)

  def get_header(self):
    return self._header

  def set_header(self, header):
    self._header = header

  def get_child_nodes(self):
    return self._header[0]

  def get_metadata_entries(self):
    return self._header[1]

  def get_metadata(self):
    return self._metadata

  def set_metadata(self, metadata):
    self._metadata = metadata

  def length(self):
    length = 2
    length += len(self._metadata)
    for child in self._children:
      length += child.length()
    return length

  def __init__(self, name):
    self._name = str(name)
    self._children = []
    self._parents = []
    self._metadata = []
    self._header = []

  def __eq__(self, other):
    return self._name == other.get_name()

  def __repr__(self):
    return self._name

  def __str__(self):
    return self._name

  def __int__(self):
    return int(self._name)


def build_node_map():
  digit = ''
  node_map = []
  with open('8_1_s.dat') as input:
    for line in input:
      for char in line:
        if char != ' ':
          digit += char
        else:
          node_map.append(int(digit))
          digit = ''
  return node_map

def build_root():
  global tree
  global node_map
  node_map = build_node_map()
  root = Node(0)
  root.set_header((node_map[0], node_map[1]))
  tree.append(root)
  print('Added root')
  print_node(root)

def build_child(parent):
  global tree
  global node_map
  map_index = int(parent) + 2
  for child in parent.get_children():
    map_index += child.length()
  child = Node(map_index)
  child.set_header((node_map[map_index], node_map[map_index+1]))
  child.add_parent(parent)
  parent.add_child(child)
  for x in range(child.get_child_nodes()):
    build_child(child)
  build_metadata(child)
  print('Added child')
  print_node(child)

def build_children(parent):
  global tree
  global node_map
  for x in range(parent.get_child_nodes()):
    build_child(parent)
  

def build_metadata(node):
  global node_map
  metadata = []
  metadata.append(node.length()-1)
  node.set_metadata(metadata)

def print_node(node):
  output = ''
  output += "ID: " + str(node) + "\n"
  output += "Header: " + str(node.get_header()) + "\n"
  output += "Parents: " + ",".join(str(x) for x in node.get_parents()) + "\n"
  output += "Child Nodes: " + str(node.get_child_nodes()) + "\n"
  output += "Children: " + ",".join(str(x) for x in node.get_children()) + "\n"
  output += "Metadata Entries: " + str(node.get_metadata_entries()) + "\n"
  output += "Metadata: " + ",".join(str(x) for x in node.get_metadata()) + "\n"
  output += ""
  print(output)

build_root()
build_children(tree[0])
build_child(tree[0])
build_metadata(tree[0])
