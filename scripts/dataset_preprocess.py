import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pymorphy2
from sklearn.model_selection import train_test_split
import re
from tqdm import tqdm

tqdm.pandas()
nltk.download("wordnet")
nltk.download("punkt")
nltk.download("stopwords")

emoji_pattern = re.compile(
    "["
    "\U0001F600-\U0001F64F"
    "\U0001F300-\U0001F5FF"
    "\U0001F680-\U0001F6FF"
    "\U0001F1E0-\U0001F1FF"
    "\U00002500-\U00002BEF"
    "\U00002702-\U000027B0"
    "\U00002702-\U000027B0"
    "\U000024C2-\U0001F251"
    "\U0001f926-\U0001f937"
    "\U00010000-\U0010ffff"
    "\u2640-\u2642"
    "\u2600-\u2B55"
    "\u200d"
    "\u23cf"
    "\u23e9"
    "\u231a"
    "\ufe0f"
    "\u3030"
    "]+",
    re.UNICODE,
)
url_pattern = re.compile(
    r"((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*"
)
mail_pattern = re.compile(r"^([a-z0-9_\.-]+)@([a-z0-9_\.-]+)\.([a-z\.]{2,6})$")
html_pattern = re.compile(r"<.*?>")
punctuation_pattern = re.compile(r"[^\w\s\d]+")
braces_pattern = re.compile(r"\([^)]*\)")
joined_pattern = re.compile(r"([a-zа-я])([A-ZА-Я])")
digits_pattern = re.compile(r"\d")

stop_words = set(stopwords.words("russian"))
lemmatizer = pymorphy2.MorphAnalyzer()


def clean_comment(comment):
    temp_comment = re.sub(braces_pattern, r"", comment)
    temp_comment = re.sub(emoji_pattern, r"", temp_comment)
    temp_comment = re.sub(url_pattern, r"", temp_comment)
    temp_comment = re.sub(mail_pattern, r"", temp_comment)
    temp_comment = re.sub(html_pattern, r"", temp_comment)
    temp_comment = re.sub(punctuation_pattern, r"", temp_comment)
    temp_comment = re.sub(joined_pattern, r"\1 \2", temp_comment)
    temp_comment = re.sub(digits_pattern, "#", temp_comment)
    temp_comment = temp_comment.removesuffix(" ")
    temp_comment = temp_comment.replace("\xad", "")
    temp_comment = temp_comment.replace("\r", ". ")
    temp_comment = temp_comment.replace("\n", ". ")
    return temp_comment


def tokenize(text):
    text = text.lower()
    text = word_tokenize(text, language="russian")
    text = [word for word in text if word.isalpha() and word not in stop_words]
    return text


def lemmatization(text):
    text = [lemmatizer.normal_forms(word)[0] for word in text]
    return text


def join_tokens(tokens):
    return " ".join(tokens)


if __name__ == "__main__":
    print("Data preprocessing started")
    df = pd.read_csv("./data/dataset.csv", sep="\t")
    print("Cleaning data")
    df["review"] = df["review"].progress_apply(clean_comment)
    print("Tokenization and lemmatization")
    df["Tokens"] = df["review"].progress_apply(tokenize).progress_apply(lemmatization)
    print("Joining tokens")
    df["Processed"] = df["Tokens"].progress_apply(join_tokens)
    print("Final touches")
    df.dropna(inplace=True)
    df = df[df["sentiment"] != "neautral"]
    df_train, df_test = train_test_split(df, test_size=0.3, random_state=978)
    print("Saving data")
    df_train.to_csv("./data/dataset_train_preprocessed.csv", index=False)
    df_test.to_csv("./data/dataset_test_preprocessed.csv", index=False)
    print("Data preprocessing finished")
