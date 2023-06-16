import pandas as pd


df_train = pd.read_parquet("./data/dataset_train_preprocessed.parquet")
df_train["Tokens"] = df_train["Tokens"].apply(tuple)
df_test = pd.read_parquet("./data/dataset_test_preprocessed.parquet")
df_test["Tokens"] = df_test["Tokens"].apply(tuple)


def test_col_exists():
    name = "Processed"
    assert name in df_train.columns
    assert name in df_test.columns


def test_null_check():
    assert df_train.isnull().any(axis=1).sum() == 0
    assert df_test.isnull().any(axis=1).sum() == 0


def test_duplicate_check():
    assert df_train.duplicated().sum() == 0
    assert df_test.duplicated().sum() == 0


def test_train_class_balance():
    positives = sum(df_train["sentiment"] == "positive")
    negatives = sum(df_train["sentiment"] == "negative")
    total_samples = len(df_train)
    positives_ratio = positives / total_samples
    negatives_ratio = negatives / total_samples
    tolerance = 0.05
    assert abs(positives_ratio - negatives_ratio) <= tolerance
