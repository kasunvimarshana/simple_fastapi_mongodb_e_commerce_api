import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib as joblib

class CommentClassifier:
    def __init__(self):
        self.tfidf_vectorizer = TfidfVectorizer(max_features=1000)
        self.rating_model = LogisticRegression()
        self.toxicity_model = LogisticRegression()
        self.train_data_path = "combined_comments.csv"
        self.joblib_path = "trained_comment_classifier.joblib"

    def train(self) -> None:
        data = pd.read_csv(self.train_data_path)
        x_train = data["comment"]
        y_rating_train = data["rating"]
        y_toxicity_train = data["toxicity"]
        x_train_tfidf = self.tfidf_vectorizer.fit_transform(x_train)
        self.rating_model.fit(x_train_tfidf, y_rating_train)
        self.toxicity_model.fit(x_train_tfidf, y_toxicity_train)

        # Evaluate models
        rating_train_predictions = self.rating_model.predict(x_train_tfidf)
        toxicity_train_predictions = self.toxicity_model.predict(x_train_tfidf)

        '''
        # rating_accuracy = (y_rating_train == rating_train_predictions).mean()
        # toxicity_accuracy = (y_toxicity_train == toxicity_train_predictions).mean()
        # print("Rating Model Accuracy:", rating_accuracy)
        # print("Toxicity Model Accuracy:", toxicity_accuracy)
        '''
        print("Rating Model Accuracy:", accuracy_score(y_rating_train, rating_train_predictions))
        print("Toxicity Model Accuracy:", accuracy_score(y_toxicity_train, toxicity_train_predictions))
        print("Rating Model Report:", classification_report(y_rating_train, rating_train_predictions))
        print("Toxicity Model Report:", classification_report(y_toxicity_train, toxicity_train_predictions))
    
    def predict(self, comment: str) -> tuple[int, bool]:
        comment_tfidf = self.tfidf_vectorizer.transform([comment])
        rating_prediction = int(self.rating_model.predict(comment_tfidf)[0])
        toxicity_prediction = bool(self.toxicity_model.predict(comment_tfidf)[0])
        return rating_prediction, toxicity_prediction

    def save(self) -> None:
        joblib.dump((self.tfidf_vectorizer, self.rating_model, self.toxicity_model), self.joblib_path)

    def load(self):
        tfidf_vectorizer, rating_model, toxicity_model = joblib.load(self.joblib_path)
        self.tfidf_vectorizer = tfidf_vectorizer
        self.rating_model = rating_model
        self.toxicity_model = toxicity_model
        return self


__all__ = [
    "CommentClassifier"
]