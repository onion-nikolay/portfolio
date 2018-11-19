# -*- coding: utf-8 -*-
__author__ = 'onion_bass'

"""
Run it to create classifier once.
"""

import pandas as pd
from os.path import join as pjoin

from sklearn.externals import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline


def session():
    df = pd.read_csv(pjoin('data', 'reviews0.csv'),
                     names=['rating', 'review'])[1:]
    ratings = [int(value[0]) for value in df.rating.values]
    reviews = df.review.values
    reviews_pos = [reviews[index] for index, rating in enumerate(ratings)
                   if rating > 4]
    reviews_neg = [reviews[index] for index, rating in enumerate(ratings)
                   if rating < 4]
    data_train = reviews_pos + reviews_neg
    labels_train = [1]*len(reviews_pos) + [0]*len(reviews_neg)

    clf = Pipeline([("vectorizer", TfidfVectorizer(ngram_range=(1, 2))),
                   ("classifier", LinearSVC())])

    clf.fit(data_train, labels_train)
    joblib.dump(clf, pjoin('data', 'SentimentClassifier.pkl'))
    return 0


if __name__ == '__main__':
    session()
