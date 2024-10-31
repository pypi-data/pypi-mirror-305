import json

def load_results_from_json(input_filename='results.json'):
    with open(input_filename, 'r') as infile:
        results = json.load(infile)
    return results['classified_texts'], results['adjusted_labels']

def generate_report(classified_texts, adjusted_labels, output_filename='report.txt'):
    with open(output_filename, 'w') as report_file:
        report_file.write("# Text Quality Assessment Report\n\n")
        
        report_file.write("## Initial Classification Results\n")
        report_file.write("| Text Index | Score | Initial Quality | Adjusted Quality | Adjusted |\n")
        report_file.write("|------------|-------|----------------|------------------|----------|\n")

        for index, text, label, score in classified_texts:
            initial_quality = 'high' if label == 1 else 'low'
            adjusted_quality = 'high' if adjusted_labels[index - 1] == 1 else 'low'  # index - 1 because index starts at 1
            was_adjusted = 'Yes' if adjusted_quality != initial_quality else 'No'  # Check if the quality was adjusted
            
            # Ensure fixed width for each column using formatted strings
            report_file.write(f"| {index:<11} | {score:>5.2f} | {initial_quality:<14} | {adjusted_quality:<16} | {was_adjusted:<8} |\n")

        report_file.write("\n## Summary\n")
        report_file.write(f"Total Texts Processed: {len(classified_texts)}\n")
        report_file.write(f"Total High-Quality Texts (Adjusted): {sum(adjusted_labels)}\n")
        report_file.write(f"Total Low-Quality Texts (Adjusted): {len(adjusted_labels) - sum(adjusted_labels)}\n")

if __name__ == "__main__":
    classified_texts, adjusted_labels = load_results_from_json()
    generate_report(classified_texts, adjusted_labels)
    print("Report generated successfully!")
