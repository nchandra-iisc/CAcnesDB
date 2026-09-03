import os
import shutil

def run_command(folder_name): 
    command = '/home/bandana/hh-suite/build/bin/hhblits -i /home/bandana/hh-suite/data/result_1406/hypothetical.fasta -o /home/bandana/hh-suite/data/result_1406/query.hrr -blasttab /home/bandana/hh-suite/data/result_1406/query.txt -n 2 -d /home/bandana/hhpred/UniRef30_2020_06'

    if not (os.path.isdir(F'/home/bandana/hh-suite/data/result_1406/{folder_name}')):
        os.mkdir(F'/home/bandana/hh-suite/data/result_1406/{folder_name}')
    
    if not (os.path.isfile(F'/home/bandana/hh-suite/data/result_1406/{folder_name}/query.txt')):
        os.system(command)

        file_names = ['hypothetical.fasta', 'query.hrr', 'query.txt']

        for file_name in file_names:
            shutil.move(F'/home/bandana/hh-suite/data/result_1406/{file_name}', F'/home/bandana/hh-suite/data/result_1406/{folder_name}/{file_name}')
 
fp = open('../fasta_results.fasta', 'r')
lines = fp.readlines()

fp2 = open('../result_1406/hypothetical.fasta', 'w')
fp2.write(lines[0])
folder_name = lines[0].split(' ')[0][1:-1]

print (folder_name)
count = 0

for line in lines[1:]:
    if(line[0]=='>'):
        print (F'Running hh-blits on {folder_name}. Count {count}')
        count += 1
        fp2.close()
        run_command(folder_name)
        fp2 = open('../result_1406/hypothetical.fasta', 'w')
        folder_name = line.split(' ')[0][1:-1]

    fp2.write(line)

fp2.close()
run_command(folder_name)
print ('Program successfully completed its run!')
