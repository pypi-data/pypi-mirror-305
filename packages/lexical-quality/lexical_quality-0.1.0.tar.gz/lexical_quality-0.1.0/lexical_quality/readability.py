from textstat import flesch_reading_ease, flesch_kincaid_grade

def calculate_readability(text):
    # Use Flesch Reading Ease score as readability metric (higher is easier to read)
    return flesch_reading_ease(text)

