import dask.dataframe as dd
from nltk.corpus import wordnet as wn
from tqdm import tqdm
import pandas as pd
import csv
df = dd.read_csv('../1 Billion Citation Dataset, v1 (103).csv')
