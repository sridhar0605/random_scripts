#!/usr/bin/python
# author: Sridhar
# email:- sridhar@wuslt.edu

import os
import argparse
import subprocess as sp
import logging
import sys


def main():
    """
    Crispr pipeline - submit jobs to lsf

    """
    parser = argparse.ArgumentParser(description='crispr pipeline')
    parser.add_argument('meta', help='meta data file, \
                        col1: name same as fastq file, \
                        col2: index,\
                        col3: amplicon sequence \
                        col4: guide rna')
    parser.add_argument('-o','--outdir', help='where do you want to write the results')
    parser.add_argument('-i', '--indir', help='where are the fastq files located')

    args = parser.parse_args()
    meta = parse_metainfo(args.meta)
    outdir = args.outdir
    indir = args.indir
    fastqc_dir = outdir + '/fast_qc'
    crispr = outdir + '/crispr'
    map(makedir, [fastqc_dir, crispr])
    for ids in meta:
        print '#Working with\t{}'.format(ids[0])
        prepare_lsf(ids[0], ids[1], ids[2], ids[3], outdir, indir)

logging.basicConfig(filename='crisp.log', level=logging.INFO)
logger = logging.getLogger()

def parse_metainfo(fin):
        with open(fin, 'r') as f:
            next(f)
            l = []
            for line in f:
                lines = line.strip().split('\t')
                samples = lines[0]
                indx = lines[1]
                amp = lines[2].replace(' ', '')
                rna = lines[3]
                l.append([samples, indx, amp, rna])
        return l

def makedir(directory):
    if not os.path.isdir(directory):
        os.mkdir(directory)
        sys.stderr.write('Make direcroty %s\n' %directory)
    return 0

def prepare_lsf(sample, indx, amp, rna, path_out_fastq, path_out_crispr,path_in):
    logger.info('#Writing {} to file \n'.format(sample))
    logger.info('{}_R1\t{}_R2\t{}\t{}\t{}\n'.format(sample, sample, indx, amp, rna))
    with open('try' + '_' + sample + '.sh', 'w+') as outp:
        outp.write("#!/bin/bash\n")
        outp.write("#BSUB -n 1 \n")
        outp.write("#BSUB -L /bin/bash\n")
        outp.write("#BSUB -J " + sample + "\n")
        outp.write("#BSUB -M 16000000 \n")
        outp.write("#BSUB -q long \n")
        outp.write("#BSUB -o " + sample + "_%J.out\n")
        outp.write("#BSUB -e " + sample + "_%J.err\n")
        outp.write("#BSUB -R 'select[mem>32000] rusage[mem=32000]'\n")
        outp.write("fastqc " + path_in + sample + "_R1_001.fastq.gz" + " -o " + path_out_fastq + "\n")
        outp.write("fastqc " + path_in +  sample + "_R2_001.fastq.gz" + " -o " + path_out_fastq + "\n")
        outp.write ("CRISPResso.py --trim_sequences -r1 " + path_in + sample + "_R1_001.fastq.gz" + " -r2 " + path_in +
                    sample + "_R2_001.fastq.gz" + " -a " + amp + " -g " + rna + " -o " + path_out_crispr )
        outp.close()
        sp.call("bsub < " + 'try' + '_' + sample + ".sh", shell=True)
        logger.info('#Submitted {} to cluster\n'.format(sample))
    return



if __name__ == '__main__':
    main()
