import pytest
from lexical_quality.grammar_spelling import check_spelling_grammar

def test_check_spelling_grammar():
    text = "This is a simple sentence. Another simple sentence here. Yet another short one."
    score = check_spelling_grammar(text)
    assert score > 0.5, "Expected perfect score for well-written text"

    text_with_errors = "Ths is a smple sentnce. Anothr smple sentnce hr. Yet anothr short on."
    score_with_errors = check_spelling_grammar(text_with_errors)
    assert score_with_errors < 1.0, "Expected lower score for text with errors"
