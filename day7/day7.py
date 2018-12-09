from anytree import Node, RenderTree, find_by_attr, AsciiStyle, PreOrderIter, PostOrderIter, LevelOrderGroupIter

instructions = [instruction.rstrip('\n') for instruction in open('input.txt')]

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

temp = root.children


k = [[node.name for node in children] for children in LevelOrderGroupIter(root)]
print(k)
fin = list()
temp = list()
fin.append(k[0][0])

i = 1
while i < len(k):
    for e in k[i]:
        temp.append(e)
    temp.sort()
    fin.append(temp[0])
    temp.remove(temp[0])
    #print(temp)
    i += 1
