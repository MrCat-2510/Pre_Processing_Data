import re
import nltk
import spacy
import string
#Remove_punctuation

PUNCT = string.punctuation + "“”" 
def remove_punctuation(text):
#     return text.translate(str.maketrans("", "", PUNCT))
    newtext = ""
    for char in PUNCT:
        text = text.replace(char, ' ')
    
    for word in text.split():
        newtext+= word + " "
    
    return newtext

#Removal of stopwords:

# nltk.download("stopwords")
from nltk.corpus import stopwords
STOPW = set(stopwords.words("english"))
def remove_stopwords(text):
    return " ".join([word for word in str(text).split() if word not in STOPW])

#Stemming

from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()
def stem_words(text):
    return " ".join([stemmer.stem(word) for word in text.split()])

#Lemmatization

nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
def lemmatize_words(text):
    return " ".join([lemmatizer.lemmatize(word) for word in text.split()])

#Removal of URLs

def remove_urls(text):
    url_pattern = re.compile(r"https?://\S+|www\.\S+")
    return url_pattern.sub(r"", text)

#Removal of HTML Tags

from bs4 import BeautifulSoup
def remove_html(text):
    return BeautifulSoup(text, "lxml").text

#Spelling Correction

from textblob import TextBlob
def correct_spellings(text):
    return str(TextBlob(text).correct())

from string import printable
st = set(printable)
def remove_ascii_letters(text):
    return ''.join([" " if  i not in  st else i for i in text])

def pre_processing(text):
    process_text = text.lower()
    process_text = remove_punctuation(process_text)
    process_text = remove_urls(process_text)
    process_text = remove_html(process_text)
    process_text = correct_spellings(process_text)
    process_text = remove_stopwords(process_text)
    process_text = stem_words(process_text)
    process_text = lemmatize_words(process_text)
    process_text = remove_ascii_letters(process_text)
    return process_text
