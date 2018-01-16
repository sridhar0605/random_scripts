from collections import defaultdict
import csv
# data = """chrom   start   end strand  gene_id gene_name
# 1   4774186 4775699 -   ENSMUSG00000033845  Mrpl15
# 1   4775960 4798536 +   ENSMUSG00000025903  Lypla1
# 1   4831213 4857551 +   ENSMUSG00000025903  Lypla1
# 1   4831213 4857551 +   ENSMUSG00000033813  Tcea1"""
dat = open(r'/Users/sid/PycharmProjects/hope/annotations_try3.txt')
data = dat.read()
result = defaultdict(list)
headers = ""

for i, line in enumerate(data.splitlines()):
    if i == 0:
        headers = line.split()
#         print headers
    else:
        d = dict(zip(headers, line.split()))
#         print d

        key = '%(chrom)s_%(start)s_%(end)s_%(strand)s' % d
        result[key].append(d)

# for val in result.values():
#     print (val)
with open('finalannotationlist.txt', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerow(headers)

    for vals in result.values():
        _finalRow = []

        for h in headers:
            if h not in ['gene_id', 'gene_name']:
                _finalRow.append(vals[0][h])  # regular columns
            else:
                _finalRow.append(','.join([v[h] for v in vals]))  # merge columns

        writer.writerow(_finalRow)
