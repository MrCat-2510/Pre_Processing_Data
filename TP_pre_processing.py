from clean import *
from readfile import * 
from concurrent.futures import ThreadPoolExecutor

def ThreadPool_main(size):
    wn.ensure_loaded() 
    citationStringAnnotated = []
    if size == True:
        print('Preprocessing whole columns')
        citationStringAnnotated = df['citationStringAnnotated']
    else:
        print('Preprocessing {} rows'.format(size))
        citationStringAnnotated = df['citationStringAnnotated'].head(size)
    with ThreadPoolExecutor() as executor:
        quote_array = list(tqdm(executor.map(pre_processing, citationStringAnnotated), total=size))
    
    print('Completely Done!')
    df_clean = pd.DataFrame(quote_array)
    df_clean.to_csv('ThreadPool_data.csv',index=False,header=False)