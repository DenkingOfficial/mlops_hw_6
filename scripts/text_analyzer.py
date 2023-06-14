import pickle

TFIDF = "./models/tfidf.pkl"
MODEL = "./models/model.pkl"


def analyze(text):
    tfidf = pickle.load(open(TFIDF, "rb"))
    model = pickle.load(open(MODEL, "rb"))
    return model.predict(tfidf.transform([text]))[0]
