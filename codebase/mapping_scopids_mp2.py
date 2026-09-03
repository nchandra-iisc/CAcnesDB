import os
import pandas as pd
import subprocess as sb
import multiprocessing as mp
import numpy as np
from tqdm import tqdm

fdata=open("combined_TMalign.tsv").readlines()

fscop_dict,cl,cf,sf,fa={},{},{},{},{}
with open("dir.des.scop.txt") as fscop:
    for line in fscop:
        fscop_dict[line]= 0
        if line.split("\t")[1]=="cl":
            cl[line.split("\t")[2]]=line.split("\t")[4].strip()
        if line.split("\t")[1]=="cf":
            cf[line.split("\t")[2]]=line.split("\t")[4].strip()
        if line.split("\t")[1]=="sf":
            sf[line.split("\t")[2]]=line.split("\t")[4].strip()
        if line.split("\t")[1]=="fa":
            fa[line.split("\t")[2]]=line.split("\t")[4].strip()

def map_func(args):
    
    fdata, position = args
    print(f"[{mp.current_process().name}] Received {len(fdata)} lines")
    df=pd.DataFrame(columns=["protein","PDB-ID_with_chain-ID","SCOP1-ID", "class","fold","superfamily","family"])
    for line in tqdm(fdata, desc=f"Worker {position}", position=position, leave=True):
        pdb=line.split("\t")[1].split(".")[0]
        protein=line.split("\t")[0]
        rowid=protein+"-"+pdb
        
        df.loc[rowid,"PDB-ID_with_chain-ID"]=pdb+".pdb"
                df.loc[rowid,"SCOP1-ID"]=i.split("\t")[2]
                df.loc[rowid,"protein"]=protein
                fam=i.split("\t")[2]
                sfam=".".join(i.split("\t")[2].split(".")[:3])
                fold=".".join(i.split("\t")[2].split(".")[:2])
                clas=i.split("\t")[2].split(".")[0]
                descriptors=[fam,sfam,fold,clas]
                indices=['family', 'superfamily', 'fold','class']
                shortform=[fa,sf,cf,cl]
                for d,r,s in zip(descriptors,indices,shortform):
                    #print(d,r,s)
                    df.loc[rowid, r]=s[d]
                    #awk_script = f'{{if ($2=="{s}" && $3=="{d}") print $5}}'
                    #df.loc[rowid, r]=sb.check_output(['awk', '-F', '\t', awk_script, 'SCOP1.tsv'],text=True)
                #df.loc[protein, "family"]=sb.check_output(["awk -F \"\t\" {if ($2=="fa"&& $3==fam) print $5}'"")
                #df.loc[protein, "superfamily"]=os.system(r"awk -F \"\t" '{if ($2=="sf"&& $3==sfam) print $5}'"")
                #print("Completed for ",rowid)
                break
        #break
    return df
    

def main():
    
    #print(cl)
    #df=pd.DataFrame(columns=["protein","PDB-ID_with_chain-ID","SCOP1-ID", "class","fold","superfamily","family"])


        
    num_workers = 20
    chunks = np.array_split(fdata, num_workers)    
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i}: {len(chunk)} lines")

    args = [(chunk.tolist(), i) for i, chunk in enumerate(chunks)]

    with mp.Pool(processes=num_workers) as pool:
            res = pool.map(map_func, args)

    df=pd.concat(res, ignore_index=False)
    df.to_csv("SCOPe_mapping.csv")
    
if __name__ == "__main__":
    main()

