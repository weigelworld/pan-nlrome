## Workflow

1. Orthogroup Generation (Diamond, orthAgogue, MCL): 'nlrome.raw.groups'
2. Paralog Splitting (T-Coffee, FastME, ete3): 'nlrome.splitted.groups'
3. Outlier removal (T-Coffee, FastME, OD-seq): 'nlrome.refined.groups'

**Final Orthogroups: 'nlrome.refined.groups'**

## File Descriptions

### File 'nlrome.raw.groups':

- id.new: Raw orthogroup identifier
- id.old: Same as id.new
- status: orthogroup/singleton
- use: 0/1
- pids: Identifiers of contained proteins

### File 'nlrome.splitted.groups':

- id.new: Splitted orthogroup identifier
- id.old: Original unrefined orthogroup identifier
- status: orthogroup/singleton
- use: 0/1
- pids: Identifiers of contained proteins

### File 'nlrome.refined.groups':

- id.new: Refined orthogroup identifier
- id.old: Original unrefined orthogroup identifier
- status: orthogroup/singleton
- use: 0/1
- pids: Identifiers of contained proteins
