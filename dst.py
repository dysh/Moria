#!/usr/bin/python
import os
import sys
from ete2 import Tree


def process():
    t = Tree("sample.phy_phyml_tree.txt")
    t1 = Tree("samplAA.phy_phyml_tree.txt")
    nms = t.get_leaf_names()
    nms1 = t1.get_leaf_names()
    s1 = []
    s2 = []
    s11 = []
    s12 = []
    for s in nms:
        if s[2] == '_':
            s1.append(s)
        if s[2] == 'e':
            s2.append(s)
    for s in nms1:
        if s[2] == '_':
            s11.append(s)
        if s[2] == 'e':
            s12.append(s)
    n1 = t.get_common_ancestor(s1)
    n2 = t.get_common_ancestor(s2)
    n11 = t1.get_common_ancestor(s11)
    n12 = t1.get_common_ancestor(s12)
    # now checking for admixture!
    q1 = n1.get_leaf_names()
    q2 = n2.get_leaf_names()
    q11 = n11.get_leaf_names()
    q12 = n12.get_leaf_names()
    crit1 = crit2 = crit3 = crit4 = 0
    for s in q1:
        if s[2] == 'e':
            crit1 = 1
            break
    for s in q2:
        if s[2] == '_':
            crit2 = 1
            break
    for s in q11:
        if s[2] == 'e':
            crit3 = 1
            break
    for s in q12:
        if s[2] == '_':
            crit4 = 1
            break
    #
    d1 = t.get_distance(n1, n2)
    d11 = t1.get_distance(n11, n12)
    d2 = t.get_distance(n1, 'OUTGROUP')
    d3 = t.get_distance(n2, 'OUTGROUP')
    d12 = t1.get_distance(n11, 'OUTGROUP')
    d13 = t1.get_distance(n12, 'OUTGROUP')
    out = "%f\t%f\t%f\t%f\t%f\t%f\t%i\t%i\t%i\t%i\n" % (d1, d2, d3, d11, d12, d13, crit1, crit2, crit3, crit4)
    return out


if __name__ == "__main__":
    print("\n\n Starting tree processing!\n\n")
    f = open('ress', 'a')
    outs = process()
    f.write('{0}\t{1}'.format(sys.argv[1], outs))
    fn1="sample.phy_phyml_tree.txt"
    fn2="samplAA.phy_phyml_tree.txt"
    cmd1 = "cp %s tree%s.tre" %(fn1, sys.argv[1])
    cmd2 = "cp %s treeAA%s.tre" %(fn2, sys.argv[1])
    os.system(cmd1)
    os.system(cmd2)

    f.close()
