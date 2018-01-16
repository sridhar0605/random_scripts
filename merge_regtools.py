import pandas as pd 

import pandas as pd
sample1 = pd.read_table('MUT-1_2.annotate.csv', sep='\t', index_col=0)["score"]
sample2 = pd.read_table('MUT-2_2.annotate.csv', sep='\t', index_col=0)["score"]
sample3 = pd.read_table('MUT-4_2.annotate.csv', sep='\t', index_col=0)["score"]
sample4 = pd.read_table('MUT-5_2.annotate.csv', sep='\t', index_col=0)["score"]
sample5 = pd.read_table('MUT-6_2.annotate.csv', sep='\t', index_col=0)["score"]
sample6 = pd.read_table('WT-1_2.annotate.csv', sep='\t', index_col=0)["score"]
sample7 = pd.read_table('WT-2_2.annotate.csv', sep='\t', index_col=0)["score"]
sample8 = pd.read_table('WT-3_2.annotate.csv', sep='\t', index_col=0)["score"]
sample9 = pd.read_table('WT-4_2.annotate.csv', sep='\t', index_col=0)["score"]
sample10 = pd.read_table('WT-5_2.annotate.csv', sep='\t', index_col=0)["score"]
#
meta1 = pd.read_table('MUT-1_2.annotate.csv', sep='\t', index_col=0).loc[:,['splice_site','intron_size', 'anchor','genes', 'exons_skipped','transcripts']]
meta2 = pd.read_table('MUT-2_2.annotate.csv', sep='\t', index_col=0).loc[:,['splice_site','intron_size', 'anchor','genes', 'exons_skipped','transcripts']]
meta3 = pd.read_table('MUT-4_2.annotate.csv', sep='\t', index_col=0).loc[:,['splice_site','intron_size', 'anchor','genes', 'exons_skipped','transcripts']]
meta4 = pd.read_table('MUT-5_2.annotate.csv', sep='\t', index_col=0).loc[:,['splice_site','intron_size', 'anchor','genes', 'exons_skipped','transcripts']]
meta5 = pd.read_table('MUT-6_2.annotate.csv', sep='\t', index_col=0).loc[:,['splice_site','intron_size', 'anchor','genes', 'exons_skipped','transcripts']]
meta6 = pd.read_table('WT-1_2.annotate.csv', sep='\t', index_col=0).loc[:,['splice_site','intron_size', 'anchor','genes', 'exons_skipped','transcripts']]
meta7= pd.read_table('WT-2_2.annotate.csv', sep='\t', index_col=0).loc[:,['splice_site','intron_size', 'anchor','genes', 'exons_skipped','transcripts']]
meta8 = pd.read_table('WT-3_2.annotate.csv', sep='\t', index_col=0).loc[:,['splice_site','intron_size', 'anchor','genes', 'exons_skipped','transcripts']]
meta9 = pd.read_table('WT-4_2.annotate.csv', sep='\t', index_col=0).loc[:,['splice_site','intron_size', 'anchor','genes', 'exons_skipped','transcripts']]
meta10 = pd.read_table('WT-5_2.annotate.csv', sep='\t', index_col=0).loc[:,['splice_site','intron_size', 'anchor','genes', 'exons_skipped','transcripts']]

concat =  pd.concat([sample1,sample2,sample3,sample4,sample5,sample6,sample7,sample8,sample9,sample10], axis=1).fillna(0)

concat.columns = ["MUT_V", "MUT1", "MUT2", "MUT4", "MUT3", "WT_V", "WT1", "WT2", "WT3", "WT4"]

meta = pd.concat([meta1,meta2,meta3,meta4,meta5,meta6,meta7,meta8,meta9,meta10])

meta = meta[~meta.index.duplicated(keep="first")]
concat = pd.concat([concat, meta], axis=1)
print(concat.head(5))
concat.to_csv('final_matrix_080717.txt', sep='\t')
