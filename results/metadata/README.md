# Explanation of metadata columns

## File 'transcript_based_metadata.tsv':
Transcript_ID
Gene_ID
Architecture: sorted domain list
Collapsed_Arch: collapsed and unsorted domain list
Subclass: subclass an NLR belongs to
Combined_Subclasses: summarized version of column4 (e.g. for T(N,L)X in col5, col4 contains TLX, TNLX, TNX, and TX)
Arch_Type: canonical or with integrated domains (noncanonical)
OG_ID: from initial orthogroup calculations
OG_Size: from initial orthogroup calculations
OG_Refined: ID from orthogroup refinement
OG_Refined_Size: from orthogroup refinement
Fusion_Flag: from webapollo, points to gene fusion correction
Merged_Flag: from webapollo, points to gene splitting
Pair_Fla
PutPair_Flag
Truncated_Flag: from webapollo, gene putatively truncated
Pseudogene_Flag: from webapollo, gene with similarity to pseudogene in Araport11
NoEvidence_Flag: from webapollo, reannotation done without direct evidence from any webapollo track
CorBound_Flag: from webapollo, geneboundaries were corrected without direct evidence from Araport11 proteins or transcripts
CorTrans_Flag: from webapollo, intron/exonboundaries were corrected without direct evidence from Araport11 proteins or transcripts
Misassembly_Flag: from webapollo, gene on putatively misassembled contig
Delete_Flag: from webapollo, suggests untrustworthy gene annotations
Mod_Flag: from webapollo, used if gene model was extensively changed (mostly without evidence from gene predictors or Araport11 transcript/protein mappings) in order to rescue the doma$
Note_Flag: from webapollo, note present in webapollo
Accession_Name
Origin: geographic origin country
Seed_Collection
Sequencing_Facility
Population
Albugo_Phenotype: GS=Green Susceptible, GR=Green Resistant, WCS=Weak Chlorotic Susceptible
Assembly_Quality
Expression
Relict_Flag
TE_In_Exons: one or more TE(s) predicted in exon(s)
TE_In_Introns: one or more TE(s) predicted in intron(s)
TEs_2kb_Downstream: one or more TE(s) predicted in 2kb region downstream of gene
TEs_2kb_Upstream: one or more TE(s) predicted in 2kb region upstream of gene

## File 'orthogroup_based_metadata.tsv':
idnew: Reinspected orthogroup ID
idold: Original orthogroup ID
status: orthogroup or singleton
use: binary
NLRs: number of NLRs contained
majorclass: major NLR class
majorsubclass: major NLR subclass
pairs: number of genes that are in pairs
putpairs: number of genes that are in putative pairs
IDs: number of genes with integrated domains
