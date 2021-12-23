from clean import *
from readfile import * 
from multiprocessing.pool import Pool

def MultiProcessing_main(size):
    wn.ensure_loaded() 
    citationStringAnnotated = []
    if size == True:
        print('Preprocessing whole columns')
        citationStringAnnotated = df['citationStringAnnotated']
    else:
        print('Preprocessing {} rows'.format(size))
        citationStringAnnotated = df['citationStringAnnotated'].head(size)
    with Pool() as p:
        clean_array = list(tqdm(p.map(pre_processing,citationStringAnnotated), total=size))
    
    print('Completely Done!')
    df_clean = pd.DataFrame(clean_array)
    df_clean.to_csv('multiprocessing_data.csv',index=False,header=False)
