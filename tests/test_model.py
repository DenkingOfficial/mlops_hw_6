import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.text_analyzer import analyze


def test_metrics():
    pass


def test_results():
    assert analyze("Я люблю программировать") == "positive"
    assert analyze("Отстойный код") == "negative"
