from gradio_client import Client
import socket


def get_local_ip_address():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip


ip = f"http://{get_local_ip_address()}:7860"
client = Client(ip)


def test_positive():
    result = client.predict("Я люблю программировать", fn_index=0)
    assert result == "positive"


def test_negative():
    result = client.predict("Отстойный код", fn_index=0)
    assert result == "negative"
