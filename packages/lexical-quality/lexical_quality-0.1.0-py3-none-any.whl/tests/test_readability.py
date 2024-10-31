import pytest
from lexical_quality.readability import calculate_readability

def test_calculate_readability():
    text = "This is a simple sentence. Another simple sentence here. Yet another short one."
    score = calculate_readability(text)
    assert score > 0.5, "Expected high readability score for simple text"

    text_with_complex_words = "This is a complex sentence with difficult words. Another sentence with more complex words here. Yet another complex one."
    score_with_complex_words = calculate_readability(text_with_complex_words)
    assert score_with_complex_words < score, "Expected lower readability score for complex text"
