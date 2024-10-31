import numpy as np
import re

def calculate_coherence(text):
    # Split text into sentences
    sentences = re.split(r'[.!?]', text)
    sentence_lengths = [len(sentence.split()) for sentence in sentences if sentence.strip()]

    if len(sentence_lengths) < 2:
        return 1  # Single sentence, assume coherent

    # Calculate standard deviation of sentence lengths (lower means more coherent)
    std_dev = np.std(sentence_lengths)

    # Invert standard deviation to get coherence score
    coherence_score = 1 / (1 + std_dev)  # Adding 1 to avoid division by zero
    return coherence_score
