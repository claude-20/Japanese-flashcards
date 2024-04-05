import pytest
from project import Card


@pytest.fixture
def sample_card():
    return Card(
        "あ",
        "a",
        "The basic 'a' sound in Japanese.",
        "あ is often used in words like あめ (ame), which means 'rain' in Japanese.",
    )


def test_card_initialization(sample_card):
    assert sample_card.character == "あ"
    assert sample_card.pronunciation == "a"
    assert sample_card.additional_info == "The basic 'a' sound in Japanese."
    assert (
        sample_card.use_case
        == "あ is often used in words like あめ (ame), which means 'rain' in Japanese."
    )


def test_iscorrect(sample_card):
    assert sample_card.iscorrect("a") == True
    assert sample_card.iscorrect("b") == False
