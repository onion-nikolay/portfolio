__author__ = 'onion_bass'

from sklearn.externals import joblib
from os.path import join as pjoin


class SentimentClassifier(object):
    def __init__(self):
        self.model = joblib.load(pjoin('data', 'SentimentClassifier.pkl'))
        self.classes_dict = {0: u"отрицательная", 1: u"положительная",
                             -1: "prediction error", -2: ""}

    def predict_text(self, text):
        if text == "":
            return -2
        try:
            _class = self.model.predict([text])[0]
            print(_class)
            return _class
        except:
            raise ValueError("Undefined error!")
            return -1

    def get_prediction_message(self, text):
        class_prediction = self.predict_text(text)
        return self.classes_dict[class_prediction]
