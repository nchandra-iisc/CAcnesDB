'''
# interproscan command 
# ./interproscan.sh -appl CDD,COILS,Gene3D,HAMAP,MobiDBLite,PANTHER,Pfam,PIRSF,PRINTS,PROSITEPATTERNS,PROSITEPROFILES,SFLD,SMART,SUPERFAMILY,TIGRFAM -i /home/bandana/hh-suite/data/fasta_results.fasta -f tsv -goterms -b ../PPAid_interpro_results/PPAid_interpro_results -pa MetaCyc,Reactome
'''
x = read.csv('PPAid_interpro_results.tsv', sep='\t',stringsAsFactors=F, header=F)
colnames(x) = c('protein_accession', 'sequence_md5_digest', 'sequence_length', 'analysis', 'signature_accession', 'signature_description', 'start_location', 'stop_location', 'e_value', 'status', 'date', 'interpro_annotations_accession', 'interpro_annotation_description', 'GO-annotation', 'pathway_annotation')
y = x[,c(1,3,4,5,6,7,8,9,12,13,14)]

pfam = y[y$analysis == 'Pfam',]
prositepatterns = y[y$analysis == 'ProSitePatterns',]
gene3d = y[y$analysis == 'Gene3D',]
panther = y[y$analysis == 'PANTHER',]
superfamily = y[y$analysis == 'SUPERFAMILY',]
prositeprofiles = y[y$analysis == 'ProSiteProfiles',]
hamap = y[y$analysis == 'Hamap',]
prints = y[y$analysis == 'PRINTS',]
cdd = y[y$analysis == 'CDD',]
tigrfam = y[y$analysis == 'TIGRFAM',]
pirsf = y[y$analysis == 'PIRSF',]
coils = y[y$analysis == 'Coils',]
smart = y[y$analysis == 'SMART',]
mobidblite = y[y$analysis == 'MobiDBLite',]
sfld = y[y$analysis == 'SFLD',]

'''
# Should I filter by e-value?
# The e-values are specific to each individual InterPro member database and therefore cannot be compared directly, or a single threshold applied to them all. This is because some member databases use the e-values for post-processing (e.g. SMART, Panther), others just output it as part of their results but actually use other measures for filtering of results (e.g. Pfam and the Hmmer GA cut-off). Therefore as far as InterProScan is concerned, if a match is in the output then it is a match!

'''
write.table(pfam, './interproscan_pfam.tsv', sep='\t', col.names=T, row.names=F)
write.table(cdd, './interproscan_cdd.tsv', sep='\t', col.names=T, row.names=F)
write.table(coils, './interproscan_coils.tsv', sep='\t', col.names=T, row.names=F)
write.table(gene3d, './interproscan_gene3d.tsv', sep='\t', col.names=T, row.names=F)
write.table(mobidblite, './interproscan_mobidblite.tsv', sep='\t', col.names=T, row.names=F)
write.table(panther, './interproscan_panther.tsv', sep='\t', col.names=T, row.names=F)
write.table(pirsf, './interproscan_pirsf.tsv', col.names=T, row.names=F, sep='\t')
write.table(prints, './interproscan_prints.tsv', sep='\t', col.names=T, row.names=F)
write.table(prositepatterns, './interproscan_prositepatterns.tsv', sep='\t', col.names=T, row.names=F)
write.table(prositeprofiles, './interproscan_prositeprofiles.tsv', sep='\t', col.names=T, row.names=F)
write.table(sfld, './interproscan_sfld.tsv', sep='\t', col.names=T ,row.names=F)
write.table(smart, './interproscan_smart.tsv', sep='\t', col.names=T, row.names=F)
write.table(superfamily, './interproscan_superfamily.tsv', sep='\t', col.names=T, row.names=F)
write.table(tigrfam, './interproscan_tigrfam.tsv', sep='\t', col.names=T, row.names=F)
write.table(hamap, './interproscan_hamap.tsv', sep='\t', col.names=T, row.names=F)
