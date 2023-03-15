from catboost import Pool
import pandas as pd
import numpy as np
from pymorphy2 import MorphAnalyzer
import re
from functools import lru_cache
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')


m = MorphAnalyzer()
regex = re.compile("[A-Za-z]+")

def Preprocessing(text,title):
    out = { 'title': title,'content': text, 'all_text':title+' '+text}
    df = pd.DataFrame(out, index = np.arange(1), columns = ['title','content','all_text'])

    lemmas = list(map(clean_text, df['all_text']))
    df['lemmas'] = lemmas
    test_pool = Pool(
        df, text_features=['title','all_text','lemmas','content'])
    return test_pool


def clean_text(text):
    tokens = words_only(text)
    lemmas = lemmatize_text(tokens)
    return ' '.join(remove_stopwords(lemmas))


def words_only(text, regex=regex):
    try:
        return regex.findall(text.lower())
    except:
        return []


@lru_cache(maxsize=128)
def lemmatize_word(token, pymorphy=m):
    return pymorphy.parse(token)[0].normal_form

def lemmatize_text(text):
    return [lemmatize_word(w) for w in text]


mystopwords = stopwords.words('english') 
def remove_stopwords(lemmas, stopwords = mystopwords):
    return [w for w in lemmas if not w in stopwords and len(w) > 3]