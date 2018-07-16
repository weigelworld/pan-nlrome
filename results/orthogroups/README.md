## Workflow

1. Orthogroup Generation (Diamond, orthAgogue, MCL)
2. Outlier removal (T-Coffee, FastME, OD-seq)
3. Paralog Splitting (T-Coffee, FastME, ete3)

**Final Orthogroups: 'nlrome.refined.groups'**

## File Descriptions

### File 'nlrome.raw.groups':

- id.new: Raw orthogroup identifier
- id.old: Same as id.new
- status: orthogroup, singleton
- use: [1|2]
- pids: Identifiers of contained proteins

### File 'nlrome.refined.groups':

- id.new: Refined orthogroup identifier
- id.old: Original unrefined orthogroup identifier
- status: orthogroup[refined/unrefined], singleton.[raw|outlier|split]
- use: [1|2]
- pids: Identifiers of contained proteins
