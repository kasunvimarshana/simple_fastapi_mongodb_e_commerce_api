import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report, accuracy_score
import joblib as joblib

class CommentClassifier:
    def __init__(self):
        self.tfidf_vectorizer = TfidfVectorizer(ngram_range=(1, 2), max_features=2000)
        self.rating_model = LogisticRegression()
        self.toxicity_model = LogisticRegression()
        self.train_data_path = "combined_comments.csv"
        self.joblib_path = "trained_comment_classifier.joblib"
        self.random_state = 42

    def train(self) -> None:
        data = pd.read_csv(self.train_data_path)
        x_train = data["comment"]
        y_rating_train = data["rating"]
        y_toxicity_train = data["toxicity"]
        
        x_train, x_val, y_rating_train, y_rating_val, y_toxicity_train, y_toxicity_val = \
            train_test_split(x_train, y_rating_train, y_toxicity_train, test_size=0.2, random_state=self.random_state)

        x_train_tfidf = self.tfidf_vectorizer.fit_transform(x_train)
        x_val_tfidf = self.tfidf_vectorizer.transform(x_val)

        param_grid_rating = {'C': [0.1, 1, 10]}
        grid_search_rating = GridSearchCV(LogisticRegression(max_iter=1000, random_state=self.random_state), param_grid_rating, cv=5)
        grid_search_rating.fit(x_train_tfidf, y_rating_train)
        self.rating_model = grid_search_rating.best_estimator_

        param_grid_toxicity = {'C': [0.1, 1, 10]}
        grid_search_toxicity = GridSearchCV(LogisticRegression(max_iter=1000, random_state=self.random_state), param_grid_toxicity, cv=5)
        grid_search_toxicity.fit(x_train_tfidf, y_toxicity_train)
        self.toxicity_model = grid_search_toxicity.best_estimator_

        # Evaluate models
        rating_train_predictions = self.rating_model.predict(x_val_tfidf)
        toxicity_train_predictions = self.toxicity_model.predict(x_val_tfidf)

        # print("Rating Model Evaluation:")
        # print(classification_report(y_rating_val, rating_train_predictions))
        print("Rating Model Accuracy:", accuracy_score(y_rating_val, rating_train_predictions))
        # print("Toxicity Model Evaluation:")
        # print(classification_report(y_toxicity_val, toxicity_train_predictions))
        print("Toxicity Model Accuracy:", accuracy_score(y_toxicity_val, toxicity_train_predictions))
    
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