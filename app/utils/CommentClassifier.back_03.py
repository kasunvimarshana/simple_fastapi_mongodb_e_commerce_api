import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib as joblib

class CommentClassifier:
    def __init__(self):
        # Initialize TF-IDF vectorizer and RandomForestClassifier
        self.tfidf_vectorizer = TfidfVectorizer(max_features=1000)
        self.rating_model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.toxicity_model = RandomForestClassifier(n_estimators=100, random_state=42)
        # Paths for data and trained model
        self.train_data_path = "combined_comments.csv"
        self.joblib_path = "trained_comment_classifier.joblib"

    def train(self):
        # Load data
        data = pd.read_csv(self.train_data_path)
        x_train = data["comment"]
        y_rating_train = data["rating"]
        y_toxicity_train = data["toxicity"]
        
        # Feature extraction
        x_train_tfidf = self.tfidf_vectorizer.fit_transform(x_train)
        
        # Split data into train and validation sets
        x_train_split, x_val_split, y_rating_train_split, y_rating_val_split, y_toxicity_train_split, y_toxicity_val_split = train_test_split(x_train_tfidf, y_rating_train, y_toxicity_train, test_size=0.2, random_state=42)
        
        # Train rating model
        self.rating_model.fit(x_train_split, y_rating_train_split)
        
        # Train toxicity model
        self.toxicity_model.fit(x_train_split, y_toxicity_train_split)

        # Evaluate models
        rating_train_predictions = self.rating_model.predict(x_val_split)
        toxicity_train_predictions = self.toxicity_model.predict(x_val_split)

        print("Rating Model Accuracy:", accuracy_score(y_rating_val_split, rating_train_predictions))
        print("Toxicity Model Accuracy:", accuracy_score(y_toxicity_val_split, toxicity_train_predictions))
        print("Rating Model Report:")
        print(classification_report(y_rating_val_split, rating_train_predictions))
        print("Toxicity Model Report:")
        print(classification_report(y_toxicity_val_split, toxicity_train_predictions))

    def predict(self, comment: str) -> tuple[int, bool]:
        comment_tfidf = self.tfidf_vectorizer.transform([comment])
        rating_prediction = int(self.rating_model.predict(comment_tfidf)[0])
        toxicity_prediction = bool(self.toxicity_model.predict(comment_tfidf)[0])
        return rating_prediction, toxicity_prediction

    def save(self):
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