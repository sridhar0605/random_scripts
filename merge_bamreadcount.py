#_author: sridhar
#_python2.7
#email: sridhar@wustl.edu

import pandas as pd
import glob
import argparse
import os
import logging
import sys

def main():
    # argument parser
    parser = argparse.ArgumentParser(
                description='Collect multiple bamreadcount csv files and merge to a single matrix',
                formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("count_dir", help='is an absolute path to the directory which has csv files')

    args = parser.parse_args()
    merge_readcount(args)

def merge_readcount(args):
    logger = getlogger('merge_bamreadcount')
    logger.info('Reading files in path')
    path = args.count_dir
    all_files = glob.glob(os.path.join(path, "*.csv"))
    dfs = pd.DataFrame()
    for file_ in all_files:
        file_df = pd.read_csv(file_,sep=',')
        file_df['file_name'] = os.path.basename(file_)
        dfs = dfs.append(file_df)
    logger.info('Done merging files')
    dfs['group'] = dfs['file_name'].map(lambda x: str(x)[:-4])
    dfs.drop('file_name', axis=1, inplace=True)
    logger.info('Writing merged matrix')
    dfs.to_csv('allMerged_combined.csv', index=False)
    df = pd.read_csv(args.count_dir + 'allMerged_combined.csv')
    logger.info('Calculating bias')
    df['bias'] = df['positive_strand'].div(df['count']).fillna(0)
    logger.info('Transposing matrix')
    _df1 = df.pivot_table(index=['group','position', 'depth'],columns=['base'],values='count').fillna(0)
    logger.info('Writing transposed matrix to file - with counts')
    _df1.to_csv('allMerged_transposed_combined.csv')
    _df2 = df.pivot_table(index=['group','position', 'depth'],columns=['base'],values='bias').fillna(0)
    logger.info('Writing transposed matrix to file - with bias')
    _df2.to_csv('allMerged_transposed_combined_bias.csv')
    logger.info('Process Complete')

#logger fuction can be scaled to any process
#original code borrowed from
#https://github.com/vivek1723/Dmatrix/blob/bdd75b1112b6490f3bda4735b2c6bb3505deca88/logSetup/logSetup.py
def getlogger(logger_name):
  logger = logging.getLogger(logger_name)
  logger.setLevel(logging.DEBUG)

  # create console handler and set level to debug
  ch = logging.StreamHandler(sys.stdout)
  ch.setLevel(logging.DEBUG)

  # add ch to logger
  logger.addHandler(ch)
  
  # create formatter
  formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", "20%y-%m-%d %H:%M:%S")
  
  #add formatter to ch
  ch.setFormatter(formatter)
  
  return logger


if __name__ == '__main__':
    main()
