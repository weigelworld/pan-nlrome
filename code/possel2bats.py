#!/usr/bin/env python

import collections
import argparse
import re
import scipy.stats
import numpy as np

from ete3 import Tree

def main():
    # Set description
    desc = 'Tool that maps BaTS association to aBRSEL-detected clades/branches and tests for correlation.'

    # Parse arguments
    parser = argparse.ArgumentParser(description=desc, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(metavar='bmap', type=str, nargs=1, dest='bmap', help='Node-ID mapping for BaTS.')
    parser.add_argument(metavar='bnwk', type=str, nargs=1, dest='bnwk', help='Input tree for BaTS.')
    parser.add_argument(metavar='bout', type=str, nargs=1, dest='bout', help='BaTS output.')
    parser.add_argument(metavar='anwk', type=str, nargs=1, dest='anwk', help='Input tree for aBRSEL.')
    parser.add_argument(metavar='aout', type=str, nargs=1, dest='aout', help='aBRSEL Output.')
    parser.add_argument('--min', type=int, default=2, dest='min', help='Minimal clade size to consider (aBRSEL).')
    parser.add_argument('--sig', type=float, default=1, dest='sig', help='P-value cutoff (aBRSEL).')
    args = parser.parse_args()

    # Parse Node-ID Mapping
    dict_bmap = dict()
    bmap = open(args.bmap[0], "r")
    for line in bmap:
        data = line.split('\t')
        dict_bmap[data[1].strip()] = data[0].strip()
    bmap.close()

    # # Parse Traits from Input tree for BaTS
    dict_trait = dict()
    ord_dict_trait = collections.OrderedDict()
    bnwk = open(args.bnwk[0], "r")
    with bnwk:
        content = bnwk.read()
        rx_traits = re.compile(r"begin states;\n((.+\n)+)End;\n\nbegin trees;", re.MULTILINE)
        for trait_match in rx_traits.finditer(content):
            trait_lines = trait_match.group(1).strip().split('\n')
            for trait_entry in trait_lines:
                trait_pair = trait_entry.split()
                trait_str = trait_pair[1].strip()
                dict_trait[trait_pair[0]] = trait_str
                if trait_str not in ord_dict_trait:
                    ord_dict_trait[trait_pair[1].strip()] = 1
    bnwk.close()

    # Parse BaTS output
    dict_bats = dict()
    bout = open(args.bout[0], "r")
    with bout:
        content = bout.read()
        rx_bout = re.compile(r"observed.+\n((.+\n)+)done", re.MULTILINE)
        for bout_match in rx_bout.finditer(content):
            bout_lines = bout_match.group(1).strip().split('\n')
            if len(ord_dict_trait) != len(bout_lines[8:]):
                raise Exception('BaTS output and trait values inconsistent.')
            for bout_entry in bout_lines[8:]:
                bout_pair = bout_entry.split('\t')
                bats_trait = ord_dict_trait.popitem(last=False)
                dict_bats[bats_trait[0]] = bout_pair[6].strip()
    bout.close()

    # Parse Input tree for aBRSEL
    tree = open(args.anwk[0], "r")
    ete3_tree = []
    for nwk in tree:
        ete3_tree.append(Tree(nwk))
    tree.close()

    # # Parse aBRSEL Output
    results_absrel = dict()
    aout = open(args.aout[0], "r")
    rx_node = re.compile(r"Selected\s+\d+\s+branches\s+for\s+testing:\s+`((.*))`")
    rx_pvalue = re.compile(r"(Node\d+),\s+p-value\s+=\s+(\d+\.\d+)\n")
    with aout:
        content = aout.read()
        for nodes_match in rx_node.finditer(content):
            nodes_absrel = nodes_match.group(1).strip().split(', ')
        for result_match in rx_pvalue.finditer(content):
            results_absrel[result_match.group(1)] = result_match.group(2)
    aout.close()

    # Traverse tree and test
    idx = 0
    tree_leaves = ete3_tree[0].get_leaves()
    for node in ete3_tree[0].traverse("postorder"):
        tree_nodeid = node.name.replace("|", "_").replace("-", "_").replace(".", "_")
        if idx < len(nodes_absrel):
            absrel_nodeid = nodes_absrel[idx]
            idx += 1
            if tree_nodeid:
                if tree_nodeid != absrel_nodeid:
                    raise Exception('BaTS node order and tree order inconsistent.')
            else:
                if absrel_nodeid in results_absrel:
                    node_leaves = node.get_leaves()
                    if len(node_leaves) >= args.min and len(tree_leaves) - len(node_leaves) >= args.min:
                        x_leaves = [x.name for x in node_leaves]
                        y_leaves = list(set([x.name for x in tree_leaves]) - set(x_leaves))
                        x_values = [float(i) for i in [dict_bats[dict_trait[dict_bmap[x]]] for x in x_leaves]]
                        y_values = [float(i) for i in [dict_bats[dict_trait[dict_bmap[x]]] for x in y_leaves]]
                        rs = scipy.stats.ranksums(x_values, y_values)
                        og = re.sub(r'.*/', '', args.anwk[0].replace(".nwk", "", 1))
                        res_br = str(og) + "\t" + ','.join(x_leaves)
                        res_rs = 1
                        if rs[1] <= args.sig and np.sum(x_values) < np.sum(y_values):
                            res_rs = str(rs[1])
                        print(str(res_br) + "\t" + str(args.bout[0].split('_')[1]) + "\t" + str(res_rs))
                                
                        
main()
