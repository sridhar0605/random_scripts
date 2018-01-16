import sys
import pandas as pd
''' Tidy this please'''

def load_df1(input_file):
    # print (input_file)
    df = pd.DataFrame(pd.read_table(input_file, sep="\t"))
    # print(list(df))
    return df
#def load_df(input_file):
#    df1 = pd.read_csv(input_file, names=["id", "name"])
#    # print(df1)
#    return df1



def perform_operations(df):
    # df = df.sort_values('start', ascending=True)
    # print(df['genes'])
    df.loc[:, 'intron_size'] = df.loc[:, 'end'] - df.loc[:, 'start'] + 1
    # print (df.head(n=5))
    df = df[df.anchor != 'N']
    #df = df.loc[~df.genes.str.contains(',')]
    df.genes = df.genes.str.split(',').str[0]
    # df_sanity = df[df[:, 'genes'].str.split(',').str.len() > 1]
    # df_sanity.to_csv(sys.argv[1][:-4] + '_sanity' + '.csv', sep='\t', index=False)
    # print(df['anchor'])
    # df['intron_size'] = df.loc['end'] - df['start'] + 1
    f = lambda row: '{chrom}:{start}-{end}({strand}):{genes}'.format(**row)
    # df4 = df.astype(str).apply(f,1)
    df4 = df.assign(Unique=df.astype(str).apply(f,1))
    df4.drop(df4.columns[[3,7,9,11,12,13]], axis=1, inplace=True)
    # df.loc[~df4.genes.str.contains(',')]
    df4 = df4[['Unique', 'score', 'splice_site', 'anchor', 'intron_size', 'exons_skipped', 'genes', 'transcripts']]
    # print df4
    df4.to_csv(sys.argv[1][:-4]+'.csv', sep='\t', index=False)
    
    # print(df4)
    return df4

# def merge_stuff(df, df1):
#     # df1 = pd.print (df1)
#     # df1.columns = ["id", "name"]
#     # print(df1)
#     # print (df1)
#     df44 = df.merge(df1, left_on="genes", right_on="name", suffixes=('','_1'))
#     df44 = df44.rename(columns={'id':'gene_id'}).drop(['name_1'], axis=1)
#     df44 = df44.sort_values('gene_id',ascending=True)
#     df44['junction_id'] = df44['gene_id'] + ':E' + df44.groupby('gene_id').cumcount().add(1).astype(str).str.zfill(3)
#     df44.drop(df44.columns[[3,7,9,11,12,13]], axis=1, inplace=True)
#     df44 = df44[['Unique', 'junction_id', 'score', 'splice_site', 'anchor', 'intron_size', 'exons_skipped', 'genes', 'transcripts']]
#     df44.to_csv(sys.argv[1][:-4]+'.csv', sep='\t', index=False)
#     # print(df44)
#     return df44


# def group_and_drop(df):
#     # df44['junction_id'] = df44['gene_id'] + ':E' + df44.groupby('gene_id').cumcount().add(1).astype(str).str.zfill(3)
#     # df44 = df
#     # df44 = df
#     df44 = df
    
#     df = df.drop(df.columns[[3,7,9,11,12,13]], axis=1, inplace=True)
#     print(df)
#     # print(df)
#     return df


# def write_out_csv(df3):
#     df3 = df[['junction_id', 'Unique', 'score', 'splice_site', 'anchor', 'intron_size', 'genes', 'transcripts']]
#     df3.to_csv('foo.csv', index=False)
#     return df3
print "Finished writing to file with out any errors"
# print sys.argv[1]
def main():
    file_1 = sys.argv[1]
 #   file_2 = sys.argv[2]
    df = load_df1(file_1)
 #   df1 = load_df(file_2)
    df4 = perform_operations(df)
    # df44 = merge_stuff(df4, df1)
    # grouped = group_and_drop(df44)
    # write_out_csv(grouped)

if __name__ == '__main__':
    main() 
