import sys
from pathlib import Path
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)
import pickle
import pandas as pd

sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.text_analyzer import analyze

df_test = pd.read_parquet("./data/dataset_test_preprocessed.parquet")
tfidf = pickle.load(open("./models/tfidf.pkl", "rb"))
model = pickle.load(open("./models/model.pkl", "rb"))
test_data = tfidf.transform(df_test["Processed"])
predicted = model.predict(test_data)


def test_accuracy():
    accuracy = accuracy_score(df_test["sentiment"], predicted)
    threshold = 0.80
    assert (
        accuracy >= threshold
    ), f"Expected accuracy >= {threshold}, but got {accuracy}"


def test_precision():
    precision = precision_score(df_test["sentiment"], predicted, pos_label="positive")
    threshold = 0.75
    assert (
        precision >= threshold
    ), f"Expected precision >= {threshold}, but got {precision}"


def test_recall():
    recall = recall_score(df_test["sentiment"], predicted, pos_label="positive")
    threshold = 0.70
    assert recall >= threshold, f"Expected recall >= {threshold}, but got {recall}"


def test_f1_score():
    f1 = f1_score(df_test["sentiment"], predicted, pos_label="positive")
    threshold = 0.70
    assert f1 >= threshold, f"Expected F1-score >= {threshold}, but got {f1}"


def test_results():
    assert analyze("Я люблю программировать") == "positive"
    assert analyze("Отстойный код") == "negative"
