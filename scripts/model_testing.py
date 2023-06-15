import pandas as pd
from sklearn.metrics import accuracy_score
import pickle

if __name__ == "__main__":
    print("Model testing started")
    df_test = pd.read_parquet("./data/dataset_test_preprocessed.parquet")
    tfidf = pickle.load(open("./models/tfidf.pkl", "rb"))
    test_data = tfidf.transform(df_test["Processed"])
    model = pickle.load(open("./models/model.pkl", "rb"))
    predicted = model.predict(test_data)
    print("Accuracy on test set:", accuracy_score(df_test["sentiment"], predicted))
