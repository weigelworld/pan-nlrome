NLRs.interpro_cc_majvote.tsv

The File contains each domain in each NLR of each of the 68 accessions/species (all RenSeq accessions, ATH (Araport11), ALYR (Arabidopsis lyrata), and CRUB (Capsella rubella)). The file follows the TSV output from interproscan (https://github.com/ebi-pf-team/interproscan/wiki/OutputFormats).

NLRs.architectures.tsv

The file contains each NLR gene of each of the 68 accessions/species (column 1). It reports the sorted domain list (column 2), the collapsed and unsorted domain list (column 3), and the subclass the NLR belongs to (column 4). Column 5 is a summarized version of column4 (e.g. for T(N,L)X in col5, col4 contains TLX, TNLX, TNX, and TX). 

arc_freq_total.tsv

The file contains each architecture (collapsed and unsorted) that is found in one of the 68 accessions/species. For each architecture it reports the class, subclass, the number of accessions that have this architecture (eco_count), the mean occurrence (mean_occ), and the total occurrence summed up for all accessions (total_count). 

arc_freq_per_accession.tsv

The file contains for each accession/species (column 2) the count for each collapsed and unsorted domain list (column 3) together with the respective counts (column 1).

OG_architecture_freqs.tsv

The file contains all architectures for each orthogroup together with the frequency this architecture occurrs. Orthogroup number (column 1) is followed by orthogroup size (column 2), and subsequenctly all architectures and their frequencies separated by "\t" (column 3 to column X).

OG_maj_arch.tsv

The file contains the representative architectures for each orthogroup. Orthogroup number (column 1) is followed by orthogroup size (column 2), and the representative architecture class (column 3).
