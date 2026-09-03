import pandas as pd
import re

file_name = open('kegg_results.txt', 'r')

ENTRY = []
NAME = []
ORTHOLOGY = []
PATHWAY = []
POSITION = []
MOTIF = []
NCBI_ProteinID = []
UniProt = []

pathway_flag = False

for line in file_name.readlines():
    line = line[:-1]
    line = re.sub(' +', ' ', line)
    
    if 'ENTRY' in line:
        ENTRY.append(' '.join(line.split(' ')[1:]))
    
    elif line[0:4]=='NAME':
        NAME.append(' '.join(line.split(' ')[1:]))

    elif 'ORTHOLOGY' in line:
        ORTHOLOGY.append(' '.join(line.split(' ')[1:]))

    elif 'PATHWAY' in line:
        PATHWAY.append(' '.join(line.split(' ')[1:]))
        pathway_flag = True
    
    elif 'POSITION' in line:
        POSITION.append(line.split(' ')[-1])

    elif 'MOTIF' in line:
        MOTIF.append(' '.join(line.split(' ')[1:]))

    elif 'NCBI-ProteinID' in line:
        NCBI_ProteinID.append(line.split(' ')[-1])

    elif 'UniProt' in line:
        UniProt.append(line.split(' ')[-1])
    
    else:
        keywords = ['BRITE', 'POSITION', 'MOTIF', 'NCBI-ProteinID', 'UniProt', 'AASEQ', 'NTSEQ']
        for keyword in keywords:
            if keyword in line:
                pathway_flag = False

    if pathway_flag==True:
        PATHWAY[-1] = PATHWAY[-1] + ';' + ' '.join(line.split(' ')[1:])

    if '///' in line:
        if len(ENTRY) != len(UniProt):
            UniProt.append('-')
        
        if len(ENTRY) != len(ORTHOLOGY):
            ORTHOLOGY.append('-')
        
        if len(ENTRY) != len(PATHWAY):
            PATHWAY.append('-')

        if len(ENTRY) != len(POSITION):
            POSITION.append('-')
        
        if len(ENTRY) != len(MOTIF):
            MOTIF.append('-')

        if len(ENTRY) != len(NCBI_ProteinID):
            NCBI_ProteinID.append('-')


print (len(ENTRY), len(NAME), len(ORTHOLOGY), len(PATHWAY), len(POSITION), len(MOTIF), len(NCBI_ProteinID), len(UniProt))

df = pd.DataFrame({'ENTRY': ENTRY, 'NAME': NAME, 'ORTHOLOGY': ORTHOLOGY, 'PATHWAY': PATHWAY, 'POSITION': POSITION, 'MOTIF': MOTIF, 'NCBI-ProteinID': NCBI_ProteinID, 'UniProt': UniProt})
df.to_csv('parsed_keggrest_results.csv', sep='|', index=False)

