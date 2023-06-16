from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pandas as pd
import pickle


def tfidf_fitter(df_train, df_test):
    X_all = pd.concat([df_train["Processed"], df_test["Processed"]], axis=0)
    tfidf = TfidfVectorizer(min_df=16, ngram_range=(1, 3))
    tfidf.fit(X_all)
    print("TF-IDF fitted")
    return tfidf


def model_train(train_data, target_data):
    X_train, X_val, y_train, y_val = train_test_split(
        train_data, target_data, test_size=0.2, random_state=333
    )
    TF_IDF_SVC_NEW = SVC(C=3, gamma=0.2, random_state=665).fit(X_train, y_train)
    print("Model trained")
    y_pred = TF_IDF_SVC_NEW.predict(X_val)
    print("Metrics on validation set:")
    print(
        f"\tAccuracy: {accuracy_score(y_val, y_pred)}\n",
        f"\tPrecision: {precision_score(y_val, y_pred, pos_label='positive')}\n",
        f"\tRecall: {recall_score(y_val, y_pred, pos_label='positive')}\n",
        f"\tF1-score: {f1_score(y_val, y_pred, pos_label='positive')}\n",
    )
    return TF_IDF_SVC_NEW


if __name__ == "__main__":
    print("Model training started")
    df_train = pd.read_parquet("./data/dataset_train_preprocessed.parquet")
    df_test = pd.read_parquet("./data/dataset_test_preprocessed.parquet")
    tfidf = tfidf_fitter(df_train, df_test)
    pickle.dump(tfidf, open("./models/tfidf.pkl", "wb"))
    train_data = tfidf.transform(df_train["Processed"])
    model = model_train(train_data, df_train["sentiment"])
    pickle.dump(model, open("./models/model.pkl", "wb"))
