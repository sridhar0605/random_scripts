# _author_= sridhar
#_python2.7
#email: sridhar@wustl.edu


import os
import argparse
import textwrap
from collections import defaultdict
import sys
import csv
import re
import pandas as pd



def main():
    
    '''
         Given bam-readcount output
          produces output is a set of tab
          delimited columns, indicating indels and snvs

    '''
    parser = argparse.ArgumentParser(
		    formatter_class=argparse.RawDescriptionHelpFormatter,
 		    description=textwrap.dedent('''\
              bam-read count parser '''))
    parser.add_argument("infile",
    	      type=str,
              action='store',
              help=textwrap.dedent('''\
              inputfile from bam count ouput'''))
    parser.add_argument("--output","-o",
    	       type=str,
               action='store',
               dest='output',
               help='destination for file out, if not supplied stout')

    args = parser.parse_args()

    parser_readcount(args)




def parser_readcount(args):
  ids = defaultdict(list) # initiate a default dict(list)


  with open(args.infile, 'r') as f:
      reader = csv.reader(f, delimiter='\t')
      for row in reader:
          chrm, key, ref, dp = row[:4]
          #print chrm, key, ref, dp
          for elems in row[4:]:
              elems = elems.split(':')
              #print elems
              
              for value in  elems[1]:
                  if elems[1] != '0':
                    pb = round(float(elems[5]) / float(elems[1]), 2)
                    vaf = round(float(elems[1]) / int(dp),2)
                  else:
                    pb = '0'
                    vaf = '0'
              _bas = (elems[0])
              #print(_bas)
              #for _base in _bas:
                  #print _base
              if _bas.startswith("+") == True and _bas != ref :
                        #print ('inertion:' , _base)
                  _mut = 'ins' 
              elif _bas.startswith("-") == True and _bas != ref:
                  _mut = 'del'
                        #print ('deletion:' , _base)
              elif _bas != ref:
                    _mut = 'snv'
                        #print ('snv:' , _base)
              elif _bas in ref:
                  _mut = 'no-mutation'
                         # print ('no mutation:' , _base)
              else:
                  _mut = 'NA'    
                         # print ('misc:' , _base)

                  #print vaf
              if elems[0] != '=':
                      ids[key].append({
                    'chr': chrm,
                    'ref':ref,
                    'depth' : dp,
                    'base': '(' + elems[0]+ ')',
                    'count': elems[1],
                    'positive_strand': elems[5],
                    'negative_strand': elems[6],
                    'percent_bias': pb,
                    'vaf': vaf,
                    'mutation' : _mut

                    })

  # for key, rows in ids.iteritems():
  #     for row in rows:
  #         print '{}\t{}'.format(key, row)


  with open(args.infile[:-4]+'_parsed_6.csv', 'w+') as f:
        writer = csv.writer(f, delimiter=",")
        keys = ["chr","ref",
                "depth", "count", 
                "base", "positive_strand", "negative_strand", 
                "percent_bias", 
                "vaf", 'mutation']
        writer.writerow(["position"] + keys)
        for k, vl in ids.iteritems():
            for v in vl:
              writer.writerow([k] + [v[key] for key in keys])


if __name__ == '__main__':
    main()
