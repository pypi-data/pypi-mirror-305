import pytest
from lexical_quality.coherence import calculate_coherence

def test_calculate_coherence():
    # Text with consistent sentence lengths
    text = "This is a simple sentence. Another simple sentence here. Yet another short one."
    score = calculate_coherence(text)
    assert score > 0.5, "Expected high coherence score for consistent sentence lengths"

    # Text with varied sentence lengths
    text_with_varied_lengths = "This is. Another sentence with more words for a sentece that is long. A very short one."
    score_with_varied_lengths = calculate_coherence(text_with_varied_lengths)
    assert score_with_varied_lengths < score, "Expected lower coherence score for varied sentence lengths"
