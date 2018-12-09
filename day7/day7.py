from anytree import Node, RenderTree, find_by_attr, AsciiStyle, PreOrderIter,PostOrderIter

instructions = [instruction.rstrip('\n') for instruction in open('test.txt')]

i = 0
for instruction in instructions:
    parent = instruction[5]
    child = instruction[36]

    # generate tree
    if i == 0:
        root = Node(parent)
        i += 1
    Node(child, parent=find_by_attr(root, parent))

for pre, _, node in RenderTree(root):
    print("%s%s" % (pre, node.name))

# start with root
# get children, sort alphabetical
res = list()
res.append(root)

tempC = root.children
#print(tempC)
#print(sorted(tempC))
print([node.name for node in PreOrderIter(root)])