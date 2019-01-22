#!/usr/bin/env python

import argparse

from Bio import AlignIO
from Bio.Align import AlignInfo


def seq2pos(seq):
    pos = []
    if len(seq) % 3 == 0:
        codons = [seq[i:i+3] for i in range(0, len(seq), 3)]
        for idx, codon in enumerate(codons):
            if codon.isalpha():
                print(str(idx+1) + "\t" + str(1))
    else:
        print("Error")

def main():
    # Set description
    desc = 'Tool to detect invariant codons in a CDS multiple sequence alignment.'

    # Parse arguments
    parser = argparse.ArgumentParser(description=desc, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(metavar='msa', type=str, nargs=1, dest='msa', help='CDS multiple sequence alignment.')
    args = parser.parse_args()


    aln = AlignIO.read(open(args.msa[0]), "fasta")
    sum = AlignInfo.SummaryInfo(aln)
    con = sum.dumb_consensus(threshold=1, ambiguous='-', require_multiple=1)
    seq2pos(str(con))


main()
