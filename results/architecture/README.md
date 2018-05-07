The architectures for each transcript can be found in the file transcript_based_metadata.tsv elsewhere in this repository. 

## arc_freq_total.tsv

- architecture: each architecture (collapsed and unsorted) that is found in one of the 68 accessions/species.
- subclass: the subclass an NLR belongs to 
- class: NLR class
- eco_count: the number of accessions that have this architecture
- mean_occ: the mean occurrence of this architecture
- total_count: the total occurrence summed up for all accessions 

## arc_freq_per_accession.tsv

- counts: counts for each collapsed_arch
- ID: accession or species
- collapsed_arch: collapsed and unsorted domain list

## OG_architecture_freqs.tsv

The file is based on the original unrefined orthogroups. It contains all architectures for each orthogroup together with the frequency this architecture occurrs. Orthogroup number (column 1) is followed by orthogroup size (column 2), and subsequenctly all architectures and their frequencies separated by "\t" (column 3 to column X).

## OG_maj_arch.tsv

The file is based on the original unrefined orthogroups. It contains the representative architectures for each orthogroup. Orthogroup number (column 1) is followed by orthogroup size (column 2), and the representative architecture class (column 3).
