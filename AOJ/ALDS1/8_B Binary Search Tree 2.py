class Node:
  def __init__(self, key, left=None, right=None):
    self.key = key
    self.left = left
    self.right = right

def insert(key):
  global root
  if root:
    ch = root
    pa = None
    while ch:
      pa, ch = ch, ch.left if key < ch.key else ch.right
    if key < pa.key:
      pa.left = Node(key)
    else:
      pa.right = Node(key)
  else:#rootがないときはここで挿入
    root = Node(key)

def find(key):
  node = root
  while node and node.key != key:
    node = node.left if key < node.key else node.right
  print("yes" if node else "no")

def delete(key):
  global root
  pa, node = None, root
  while node.key != key:
    pa, node = node, node.left if key < node.key else node.right
  if node.left and node.right:
    pa, to_del = node, node.right
    while to_del.left:
      pa, to_del = to_del, to_del.left
    node.key = to_del.key
  else:
    to_del = node
  ch = to_del.left or to_del.right
  if not pa:
    root = ch
  elif pa.left == to_del:
    pa.left = ch
  else:
    pa.right = ch

def walk(node, order):
  walked = ""
  if node:
    if order == "Pre":
      walked += f" {node.key}"
    walked += walk(node.left, order)
    if order == "In":
      walked += f" {node.key}"
    walked += walk(node.right, order)
  return walked

def show():
  for order in ["In", "Pre"]:
    print(walk(root, order))

root = None
cmds = {"print":show, "insert":insert, "find":find, "delete":delete}
for _ in range(int(input())):
  cmd_name, *key = input().split()
  cmds[cmd_name](*map(int, key))