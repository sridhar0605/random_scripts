import re
with open ('uniq_manta.calls.bedpe') as f:
    next(f)
    next(f)
    for i in f:
        line = i.strip().split('\t')
        chrom1 = line[0]
        start1 = int(line[1])
        end1 = int(line[5])
        #at = dict(v.split(";") for v in line[11:])
        for rows in line[11:]:
            rows = rows.strip('=').split(';')
            di = {}
            for i in rows:
                k,v = i.split('=')
                di[k] = v
        for k,v in di.iteritems():
            if k == 'TYPE' and v != 'UNK':
                print '{}\t{}\t.\t{}\t.\t{}'.format(chrom1, start1, end1, v.lower())
