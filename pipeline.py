import re
import pickle
import os.path
import pandas as pd
from constants import MODEL_FILE
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split


def create_model():
    data = pd.read_csv("fit_data/test.csv", sep="\t")
    data["Товар"] = data["Товар"].apply(lambda x: x.lower())
    data["Товар"] = data["Товар"].apply((lambda x: re.sub("[.,!@0-9]", "", x)))

    X_train, X_test, y_train, y_test = train_test_split(data["Товар"].values,
                                                        data["Категория"].values,
                                                        test_size=0.2, random_state=42)

    vectorizer = TfidfVectorizer(min_df=2, max_features=None,
                                 token_pattern=r"\w+",
                                 strip_accents="unicode",
                                 analyzer="word",
                                 ngram_range=(1, 2),
                                 use_idf=1, smooth_idf=1,
                                 sublinear_tf=1)
    clf = LogisticRegression(C=1000, max_iter=1000)

    pipeline = make_pipeline(vectorizer, clf)
    pipeline.fit(X_train, y_train)

    y_pred = pipeline.predict(X_test)
    print("ACCURACY :", accuracy_score(y_pred, y_test))
    print("F1 :", f1_score(y_pred, y_test, average="macro"))

    with open(MODEL_FILE, "wb") as f:
        pickle.dump(pipeline, f)


if not os.path.exists(MODEL_FILE):
    create_model()


with open(MODEL_FILE, "rb") as f:
    pipeline = pickle.load(f)
