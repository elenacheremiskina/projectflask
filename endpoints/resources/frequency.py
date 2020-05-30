import io
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import SnowballStemmer
import numpy as np
import os
from app import app

def frequency(file):
    with io.open(os.path.join(app.config['UPLOAD_FOLDER'], file), 'r', encoding='utf8') as f:
        word_list = f.read()
    tokens = word_tokenize(word_list)
    tokens = [w.lower() for w in tokens]
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in tokens]
    words = [word for word in stripped if word.isalpha()]
    stop_words = set(stopwords.words())
    words = [w for w in words if not w in stop_words]

    stemmer = SnowballStemmer('russian')

    text2 = np.array([stemmer.stem(token) for token in words])
    unique, counts = np.unique(text2, return_counts=True)
    m = dict(zip(unique, counts))
    s = {k: v for k, v in sorted(
        m.items(), key=lambda item: item[1], reverse=True)}
    wordd = list(s.keys())
    number = np.array(list(s.values())).tolist()
    return {'text': wordd[:10], 'count': number[:10]}
