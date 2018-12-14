from collections import defaultdict

def appendNoDupl(in_list, val):
    if (in_list.count(val) < 1):
        in_list.append(val)
    return in_list

def preCond (tree, cand, ref):
     # check if all conditions are fulfilled before appending
    cond = list()
    for a, b in tree.items():
        for it in b:
            if it == cand:
                cond.append(a)
    return all(elem in ref for elem in cond)

instructions = [instruction.rstrip('\n') for instruction in open('test.txt')]
tree = defaultdict(list)

for instruction in instructions:
    parent = instruction[36]
    child = instruction[5]

    # generate tree
    tree[parent].append(child)

print(tree.items())
print(sorted(tree.keys()))
#define root
root1 = list()
for trk in tree.keys():
    c_check = trk
    find = 0
    for val in tree.values():
        if val.count(trk) > 0:
            find += 1
    if find == 0:
        root1.append(trk)
root = 'E'
#print(root)

#for root in root1:
par_list = list()
tree_val = list()
res_list = list()
child = list()

res_list.append(root)
par_list.append(root)

p = 0
while p < len(par_list):
    child = tree.get(par_list[p], False)
    par_list.remove(par_list[p])
    if child != False:
        for c in child:
            tree_val = appendNoDupl(tree_val, c)
            par_list = appendNoDupl(par_list, c)
    else:
        break
    tree_val.sort()
    #print(tree_val)
    for tr in tree_val:
        all_there = preCond(tree, tr, res_list)
        if all_there:
            res_list.append(tr)
            #no duplicates
            par_list = appendNoDupl(par_list, tr)
            tree_val.remove(tr)
            for t in tree_val:
                # no duplicates
                par_list = appendNoDupl(par_list, t)
            break

    print(res_list)
