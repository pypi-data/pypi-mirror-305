import pandas as pd
import json
import lexical_quality.readability as readability
import lexical_quality.grammar_spelling as grammar_spelling
import lexical_quality.coherence as coherence
from cleanlab.classification import CleanLearning
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import numpy as np
import subprocess

def calculate_quality_score(text):
    readability_score = readability.calculate_readability(text)
    grammar_spelling_score = grammar_spelling.check_spelling_grammar(text)
    coherence_score = coherence.calculate_coherence(text)

    # Average all three scores, assuming equal weight
    quality_score = ((readability_score / 100) + grammar_spelling_score + coherence_score) / 3
    return quality_score

def load_texts_from_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data['texts']

def classify_texts_by_quality(texts, threshold=0.60):
    classified_texts = []
    for i, text in enumerate(texts):
        quality_score = calculate_quality_score(text)
        label = 1 if quality_score >= threshold else 0  # 1 = high quality, 0 = low quality
        classified_texts.append((i + 1, text, label, quality_score))
    return classified_texts

def adjust_confidence_based_on_quality(texts, threshold=0.60):
    # Calculate quality scores for the texts
    quality_scores = np.array([calculate_quality_score(text) for text in texts])
    
    # Generate integer labels based on the quality threshold
    labels = np.array([1 if score >= threshold else 0 for score in quality_scores])

    # Vectorize the text data using TF-IDF
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)  # X is a sparse matrix

    # Initialize a Logistic Regression model as the base classifier
    base_classifier = LogisticRegression(max_iter=400)
    
    # Wrap the model with Cleanlab's CleanLearning
    cl = CleanLearning(base_classifier, cv_n_folds=3)

    # Fit the model to find label issues
    cl.fit(X, labels)

    # Find potential label issues
    label_issues = cl.find_label_issues(X, labels)

    # Extract confidence scores for each prediction
    pred_probs = cl.predict_proba(X)

    # Convert label_issues to a list if necessary
    if isinstance(label_issues, (pd.DataFrame, pd.Series)):
        label_issues = label_issues.values.flatten().tolist()
    else:
        label_issues = list(label_issues)  # Ensure it's a list

    # Adjust labels based on quality scores, detected issues, and confidence scores
    adjusted_labels = []
    for i, score in enumerate(quality_scores):
        confidence = np.max(pred_probs[i])  # Get the maximum confidence score for the current prediction
        if label_issues[i]:  # Check if there's a label issue
            # Increase the risk of mislabeling for low quality and low confidence
            if score < threshold and confidence < 0.5:  # Low quality and low confidence
                adjusted_label = 0  # Keep it low quality
            else:
                adjusted_label = 1 if score >= threshold else 0  # Use the original label otherwise
        else:
            # High quality texts should influence the decision based on confidence
            if score >= threshold and confidence > 0.7:  # High quality and high confidence
                adjusted_label = 1  # Keep it high quality
            else:
                adjusted_label = 0  # Otherwise keep it low quality
        adjusted_labels.append(adjusted_label)
    
    return adjusted_labels

def save_results_to_json(classified_texts, adjusted_labels, output_filename='results.json'):
    results = {
        'classified_texts': classified_texts,
        'adjusted_labels': adjusted_labels
    }
    with open(output_filename, 'w') as outfile:
        json.dump(results, outfile)

def main():
    # Load texts from the JSON file
    texts = load_texts_from_json('texts.json')
    
    # Classify texts based on their quality scores
    classified_texts = classify_texts_by_quality(texts, threshold=0.6)
    
    # Print initial classification results
    print("Classified Texts:")
    for index, text, label, score in classified_texts:
        print(f"Text {index} (Score: {score:.2f}, Quality: {'high' if label == 1 else 'low'})")
    
    # Adjust labels based on quality and Cleanlab's findings
    adjusted_labels = adjust_confidence_based_on_quality(texts, threshold=0.6)

    # Print adjusted labels
    print("\nAdjusted Labels based on Quality:")
    for i, (text, label) in enumerate(zip(texts, adjusted_labels)):
        print(f"Text {i + 1} - Adjusted Quality: {'high' if label == 1 else 'low'}")

    # Save results to a JSON file
    save_results_to_json(classified_texts, adjusted_labels)

    # Generate the report by running results.py
    subprocess.run(['python', 'results.py'], check=True)

if __name__ == "__main__":
    main()
