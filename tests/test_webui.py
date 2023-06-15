from gradio_client import Client

client = Client("http://127.0.0.1:7860/")


def test_positive():
    result = client.predict("Я люблю программировать", fn_index=0)
    assert result == "positive"


def test_negative():
    result = client.predict("Отстойный код", fn_index=0)
    assert result == "negative"
