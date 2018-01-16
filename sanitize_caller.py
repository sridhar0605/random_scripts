import sys
filename = sys.argv[1]
upn_id = sys.argv[2]
caller = sys.argv [3]

if caller == '10x':
    with open (filename) as f:
        next(f)
        next(f)
        for i in f:
            line = i.strip().split('\t')
            chrom1 = line[0]
            start1 = int(line[1])
            end1 = int(line[2])
            chrom2 = line[3]
            start2 = int(line[4])
            end2 = int(line[5])
            call_id = line[6]
            upn = upn_id

            #at = dict(v.split(";") for v in line[11:])
            for rows in line[11:]:
                rows = rows.strip('=').split(';')
                di = {}
                for i in rows:
                    k,v = i.split('=')
                    di[k] = v
            for k,v in di.iteritems():
                if k == 'TYPE' or k == 'RP_TYPE':
                    print '{}\t{}\t{}\t{}:{}:{}\n{}\t{}\t{}\t{}:{}:{}'.format(chrom1, start1, end1, v.lower(),
                                                                     upn,call_id,chrom2, start2, end2, 
                                                                     v.lower(),upn,call_id)
elif caller == 'manta':
    with open (filename) as f:
        next(f)
        for i in f:
            line = i.strip().split('\t')
            chrom1 = line[0]
            start1 = int(line[1])
            end1 = int(line[2])
            chrom2 = line[3]
            start2 = int(line[4])
            end2 = int(line[5])
            _type = line[10]
            _id = line[6]
            upn = upn_id
            print '{}\t{}\t{}\t{}:{}:{}\n{}\t{}\t{}\t{}:{}:{}'.format(chrom1, start1, end1, _type,
                                                                     upn,_id,chrom2, start2, end2,_type,upn,_id)

elif caller == 'overlap':
    with open (filename) as f:
        for i in f:
            line = i.strip().split('\t')
            chrom1 = line[0]
            start1 = int(line[1])
            end1 = int(line[2])
            chrom2 = line[3]
            start2 = int(line[4])
            end2 = int(line[5])
            call_id = line[6]
            upn = upn_id

            #at = dict(v.split(";") for v in line[11:])
            for rows in line[11:]:
                rows = rows.strip('=').split(';')
                di = {}
                for i in rows:
                    k,v = i.split('=')
                    di[k] = v
            for k,v in di.iteritems():
                if k == 'TYPE' or k == 'RP_TYPE':
                    print '{}\t{}\t{}\t{}:{}:{}\n{}\t{}\t{}\t{}:{}:{}'.format(chrom1, start1, end1, v.lower(),
                                                                     upn,call_id,chrom2, start2, end2, 
                                                                     v.lower(),upn,call_id)


else:
    print 'Unknown caller please check inputs'
