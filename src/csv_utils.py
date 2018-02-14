# csv and data load helpers for our classifier
import re
import pandas as pd
from sklearn.model_selection import train_test_split

def tokenize(review):
    no_punctuation = re.sub(r'[^a-zA-Z0-9\s]', '', review)
    tokens = no_punctuation.lower().split()
    return tokens

def build_vocab_dict(reviews):
    unique_words = set()
    word_map = dict()

    for review in reviews:
        review_words = tokenize(review)
        unique_words.update(review_words)

    for idx, word in enumerate(unique_words):
        word_map[word] = idx

    return word_map

def review_vector(review, vocab, unknown_word_int):
    vector = []
    tokens = tokenize(review)
    for token in tokens:
        if token in vocab:
            vector.append(vocab[token])
        else:
            vector.append(unknown_word_int)
    return vector

def reviews_to_vectors(reviews, vocab):
    vectors = []
    unknown_word_int = len(vocab)

    for review in reviews:
        vector = review_vector(review, vocab, unknown_word_int)
        vectors.append(vector)

    return vectors

def load_data(filename):
    # we expect a file with a sentiment column (our Y) and a text column (our X)
    data = pd.read_csv(filename)
    X = data['text'].values
    y = data['sentiment'].values
    vocab = build_vocab_dict(X)
    X = reviews_to_vectors(X, vocab)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
    return (X_train, y_train), (X_test, y_test), vocab

