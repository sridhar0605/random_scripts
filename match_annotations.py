#!/bin/python
C = []
with open('/Users/sid/final_matrix_only_anno_0517.txt') as fh:
    fh.readline()
    for line in fh:
        sl = line.strip().split()
        C.append((sl[0], int(sl[1]), int(sl[2]), sl[3]))

A = []
with open('/Users/sid//gene_final_anno.csv') as fh:
    fh.readline()
    for line in fh:
        sl = line.strip().split(',')
        A.append((sl[0], int(sl[1]), int(sl[2]), sl[3], sl[4], sl[5]))
print ('chrom' + '\t' + 'start' + '\t' + 'end' + '\t' + 'strand' + '\t' + 'gene_id' + '\t' + 'gene_name')        
for cchr, cst, cen, cstr in C:
    for achr, ast, aen, _, gid, gname in A:
        if cchr == achr:
            l = sorted([(cst, cen), (ast, aen)])
            if l[1][0] <= l[0][1]:  # Overlap
                st, en = cst, cen
                output = [cchr, st, en, cstr, gid, gname]
                #print ('chrom' + '\t' + 'start' + '\t' + 'end' + '\t' + 'strand' + '\t' + 'gene_id' + '\t' + 'gene_name')
                print('{}\t{}\t{}\t{}\t{}\t{}'.format(*output))
