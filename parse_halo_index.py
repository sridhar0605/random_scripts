import os
import argparse
import textwrap

def main():
    '''
         given single column index id for haloplex, 
         get index from master file. 

    '''
    parser = argparse.ArgumentParser(
		    formatter_class=argparse.RawDescriptionHelpFormatter,
 		    description=textwrap.dedent('''\
              Haloplex index parsergiven single column indexid get corresponding index'''))
    parser.add_argument("infile",
    	      type=str,
              action='store',
              help=textwrap.dedent('''\
              inputfile with single column index
              A1 
              A2 
              A10'''))
    parser.add_argument("indexfile",
    	      type=str,
              action='store',
              help=textwrap.dedent('''\
              indexfile with two column index data
              A1  AGCACCTC
              A2  ACGCTCGA
              A10 CGCATACA'''))
    parser.add_argument("--output","-o",
    	       type=str,
               action='store',
               dest='output',
               help='destination for file out, if not supplied stout')
    args = parser.parse_args()

    parseindex(args)
   
def parseindex(args):
	inf = []
	
	with open(args.infile, 'r') as f:
		for line in f:
			lines= line.strip().split('\t')
			inf.append(lines)
	f.close()

	master= []	

	with open(args.indexfile,'r') as f:
		for line in f:
			lines= line.strip().split('\t')
			master.append(lines)
	f.close()
    
	if args.output:
		with open(args.output+'.txt', 'w') as f:
			for i in inf:
				for ids in master:
					if i[0] in ids[0]:
						l = ids[0],ids[1]
						f.write('\t'.join(l) + '\n')
		f.close()
	else:
		with open(args.infile[:-4]+'index.txt', 'w') as f:
			for i in inf:
				for ids in master:
					if i[0] in ids[0]:
						l = ids[0],ids[1]
						f.write('\t'.join(l) + '\n')
    	f.close()
    
	return
     



if __name__ == '__main__':
    main()