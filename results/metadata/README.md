# Explanation of metadata columns

## File 'transcript_based_metadata.tsv':
- Transcript_ID
- Gene_ID
- Architecture: sorted domain list
- Collapsed_Arch: collapsed and unsorted domain list
- Subclass: subclass an NLR belongs to
- Combined_Subclasses: summarized version of column4 (e.g. for T(N,L)X in col5, col4 contains TLX, TNLX, TNX, and TX)
- Arch_Type: canonical or with integrated domains (noncanonical)
- OG_ID: from initial orthogroup calculations
- OG_Size: from initial orthogroup calculations
- OG_Refined: ID from orthogroup refinement
- OG_Refined_Size: from orthogroup refinement
- Fusion_Flag: from webapollo, points to gene fusion correction
- Merged_Flag: from webapollo, points to gene splitting
- Pair_Fla
- PutPair_Flag
- Truncated_Flag: from webapollo, gene putatively truncated
- Pseudogene_Flag: from webapollo, gene with similarity to pseudogene in Araport11
- NoEvidence_Flag: from webapollo, reannotation done without direct evidence from any webapollo track
- CorBound_Flag: from webapollo, geneboundaries were corrected without direct evidence from Araport11 proteins or transcripts
- CorTrans_Flag: from webapollo, intron/exonboundaries were corrected without direct evidence from Araport11 proteins or transcripts
- Misassembly_Flag: from webapollo, gene on putatively misassembled contig
- Delete_Flag: from webapollo, suggests untrustworthy gene annotations
- Mod_Flag: from webapollo, used if gene model was extensively changed (mostly without evidence from gene predictors or Araport11 transcript/protein mappings) in order to rescue the doma$
- Note_Flag: from webapollo, note present in webapollo
- Accession_Name
- Origin: geographic origin country
- Seed_Collection
- Sequencing_Facility
- Population
- Albugo_Phenotype: GS=Green Susceptible, GR=Green Resistant, WCS=Weak Chlorotic Susceptible
- Assembly_Quality
- Expression
- Relict_Flag
- TE_In_Exons: one or more TE(s) predicted in exon(s)
- TE_In_Introns: one or more TE(s) predicted in intron(s)
- TEs_2kb_Downstream: one or more TE(s) predicted in 2kb region downstream of gene
- TEs_2kb_Upstream: one or more TE(s) predicted in 2kb region upstream of gene

## File 'orthogroup_based_metadata.tsv':
- idnew: Reinspected orthogroup ID
- idold: Original orthogroup ID
- status: orthogroup or singleton
- use: binary
- NLRs: number of NLRs contained
- majorclass: major NLR class
- majorsubclass: major NLR subclass
- pairs: number of genes that are in pairs
- putpairs: number of genes that are in putative pairs
- IDs: number of genes with integrated domains

## File 'architecture_based_metadata.tsv'
summarizes domain-architecture based stats and dataset analysis intersections. Below is a brief description of each column content


- Collapsed_Arch: 97 collapsed architectures sorted by reverse size
- Size: Number of transcripts in each collapsed architecture
- Size_ratio: Relative size compared to the total number of NLRs (13,160; excl\. renseq-6909, ALYR and CRUB)
- Arch_Type: Architectures containing any combination of Coil/TIR/RPW8/NB/LRR are canonical\. Architectures containing any other domain are noncanonical
- ArchType_ratio: Relative size compared to the number of transcript in the correspondent Arch_Type (canonical: 12,496; noncanonical: 664; excl. renseq-6909, ALYR and CRUB)
- Transcript: List of transcript identifiers
- Subclass: Higher-order domain categories in which each domain architecture is included
- Combined_Subclasses: Expanded version of Subclasses, including between parenthesis domains that might be included in each respective subclass
- pair_putpair_size: Number of transcripts flagged as pair or putpair
- pair_putpair_ratio: Relative size of paired/putpaired genes in compared to the total number of genes (13,160; excl. renseq-6909, ALYR and CRUB)
- pair_putpair_transcripts: List of transcript identifiers flagged as pair or putpair
- transcripts_assigned_to_OGs: Number of transcripts assigned to Orthogroups
- Number_different_OGs: Number of different orthogroups to which trnscripts with the same collapsed architecture were assigned to
- transcripts_assigned_to_refinedOGs: Number of transcripts assigned to Refined Orthogroups
- Number_different_refinedOGs: Number of different refined orthogroups to which trnscripts with the same collapsed architecture were assigned to
- Collapsed_Arch_in_Col-0: Architectures detected in Araport11 NLRs (1), not detected (0)
- Collapsed_Arch_in_Genus: Architectures detected in Arabidopsis halleri and Arabidopsis lyrata (1); not detected (0)
- Collapsed_Arch_in_Tribe: Architectures detected in Arabidopsis halleri, Arabidopsis lyrata, Camelina sativa, Capsella grandiflora and Capsella rubella (1), not detected (0)
- Collapsed_Arch_in_Family: Architectures detected in Arabidopsis halleri, Arabidopsis lyrata, Camelina sativa, Capsella grandiflora, Capsella rubella, Leavenworthia alabamica, Aethionema arabicum, Thellungiella parvula, Arabis alpina, Sisymbrium irio, Thellungiella halophila, Thellungiella salsuginea, Raphanus sativus, Brassica rapa, Brassica nigra, Brassica napus, Brassica juncea and Brassica oleracea (1), not detected (0)
- Collapsed_Arch_in_Order: Architectures detected in Arabidopsis halleri, Arabidopsis lyrata, Camelina sativa, Capsella grandiflora, Capsella rubella, Leavenworthia alabamica, Aethionema arabicum, Thellungiella parvula, Arabis alpina, Sisymbrium irio, Thellungiella halophila, Thellungiella salsuginea, Raphanus sativus, Brassica rapa, Brassica nigra, Brassica napus, Brassica juncea, Brassica oleracea, Tarenaya hassleriana and Carica papaya (1), not detected (0)

## File 'domain_based_metadata.tsv'
summarizes domain-based stats and dataset analysis intersections\. Below is a brief description of each column content\.

- Domain_ID: 41 domains sorted by revserse size (excl. renseq-6909, ALYR and CRUB)
- size: Number of transcripts featuring the domain
- pair_putpair_size: Number of transcripts flagged as pair or putpair
- pair_putpair_ratio: Relative size of paired/putpaired genes compared to the total number of genes (13,160; excl. renseq-6909, ALYR and CRUB)
- Col-0: Domain detected in Araport11 NLRs (1), not detected (0)
- Genus: Domain detected in Arabidopsis halleri and Arabidopsis lyrata (1); not detected (0)
- Tribe: Domain detected in Arabidopsis halleri, Arabidopsis lyrata, Camelina sativa, Capsella grandiflora and Capsella rubella (1), not detected (0)
- Family: Domain detected in Arabidopsis halleri, Arabidopsis lyrata, Camelina sativa, Capsella grandiflora, Capsella rubella, Leavenworthia alabamica, Aethionema arabicum, Thellungiella parvula, Arabis alpina, Sisymbrium irio, Thellungiella halophila, Thellungiella salsuginea, Raphanus sativus, Brassica rapa, Brassica nigra, Brassica napus, Brassica juncea and Brassica oleracea (1), not detected (0)
- Order: Domain detected in Arabidopsis halleri, Arabidopsis lyrata, Camelina sativa, Capsella grandiflora, Capsella rubella, Leavenworthia alabamica, Aethionema arabicum, Thellungiella parvula, Arabis alpina, Sisymbrium irio, Thellungiella halophila, Thellungiella salsuginea, Raphanus sativus, Brassica rapa, Brassica nigra, Brassica napus, Brassica juncea, Brassica oleracea, Tarenaya hassleriana and Carica papaya (1), not detected (0)