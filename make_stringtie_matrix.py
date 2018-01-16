from collections import defaultdict
output_file = 'sude_tpm.txt'
list_files = []
samples = [f.split('/')[-1].replace('.txt', '_tpm') for f in list_files]
sample = defaultdict(list)
frmt = 'TPM'
for f in list_files:
    with open(f) as rows:
        next(rows)
        for row in rows:
            cols = row.strip().split()
            if cols[0].startswith ('ENS') and float(cols[8]) != 0:
                sample[cols[0]].append({
                   'Gene_ID':cols[0],
                   'Gene_Name':cols[1],
                   'FPKM':cols[7],
                   'TPM':cols[8],
                   'sample':f.split('/')[-1].replace('.txt', '_tpm')
                })
with open(output_file, 'w') as f:
    header = ['Gene_ID', 'Gene_Name']
    header.extend(samples)
    f.write('\t'.join(header) + '\n')
    for id, infos in sample.iteritems():
        row = [infos[0]['Gene_ID'], infos[0]['Gene_Name']]
        vals = {}
        sample_vals = []
        for info in infos:
            vals[info['sample']] = info[frmt]
        for smp in samples:
            if smp in vals.keys():
                sample_vals.append(vals[smp])
            else:
                sample_vals.append('0')
        row.extend(sample_vals)
        f.write('\t'.join(map(str, row)) + '\n')
