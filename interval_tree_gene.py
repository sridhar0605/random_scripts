from intervaltree import IntervalTree
from collections import defaultdict

binding_factor = '/data0/sridnona/eye/Mus_musculus/UCSC/mm9/Sequence/WholeGenomeFasta/bind_mitf_1_gene.txt'
genome = dict()

with open('/data0/sridnona/eye/Mus_musculus/UCSC/mm9/Sequence/WholeGenomeFasta/headers', 'r') as rows:
    next(rows)
    for row in rows:
        #print row
        if row.startswith('>'):
            row = row.strip().split('|')
            #print row
            row[1] = row[1].replace('chr', '') if row[1].startswith('chr') else row[1]
            row[0] = row[0].replace('>', '') if row[0].startswith('>') else row[0]
            row[1] = row[1].replace('MT', 'M') if row[1].startswith('MT') else row[1]            
            chrom_name = row[1]
            #print chrom_name
            #row[2] = int(row[2])
            start = int(row[2])
            end = int(row[3])
            #one interval tree per chromosome
            if chrom_name not in genome.keys():
               genome[chrom_name] = IntervalTree()                
                #first time we've encountered this chromosome, create an interval tree                    
                #index the feature
            #if row[6] == "-1":
               start = end
            genome[chrom_name].addi(start-2000, start, {"gene":row[0], "chr":row[1]})
#for key,value in genome.iteritems():
print len(genome) 
 
    #return genome

mast = defaultdict(list)
with open('/data0/sridnona/eye/Mus_musculus/UCSC/mm9/Sequence/WholeGenomeFasta/mastcell_chipseq/GSM1167584_Mitf_mast.bed', 'r') as f:
     for row in f:
	 row = row.strip().split()
	 row[0] = row[0].replace('chr', '') if row[0].startswith('chr') else row[0]
	 row[0] = 'M' if row[0] == 'M' else row[0]
         #row[0] = 'MT' if row[0] == 'M' else row[0]
	 #row[0] = 'M' if row[0] == 'M' else row[0]
	 #print row[0]
         mast[row[0]].append({
         'start':int(row[1]),
         'end':int(row[2])
         })
#for k,v in mast.iteritems():
    #print k, ":", v  

with open(binding_factor, 'w') as f :
     for k,v in mast.iteritems():
         for i in v:
             
         
             gene = genome[k].search(i['start'],i['end'])
             
             
             if gene:
                print gene
                for i in gene:
                    l = (i.data['chr'] + '\t' + i.data['gene'])  
                                        
                
                    f.write(''.join(l)+'\n')