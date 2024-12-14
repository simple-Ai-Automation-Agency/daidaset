import json
import os
import PyPDF2
import pandas as pd

def extract_pdf_data(pdf_path):
    """Extract text from a PDF file."""
    pdf_data = {"file": pdf_path, "pages": []}
    
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text = page.extract_text() if page.extract_text() else ""
            pdf_data["pages"].append({
                "page": page_num,
                "content": text.strip() if text else "No content"
            })
    
    return pdf_data

def generate_dataset_from_text(input_file):
    """Generate dataset from a text file."""
    dataset = []
    with open(input_file, 'r') as file:
        for line in file:
            entry = {
                "prompt": line.strip(),
                "response": "Your response here"  # Placeholder for generated responses
            }
            dataset.append(entry)
    return dataset

def generate_dataset_from_csv(input_file):
    """Generate dataset from a CSV file."""
    df = pd.read_csv(input_file)
    dataset = []
    
    for index, row in df.iterrows():
        entry = {
            "prompt": row.get("prompt", "No prompt"),
            "response": row.get("response", "No response")
        }
        dataset.append(entry)
    
    return dataset

def generate_dataset_from_jsonl(input_file):
    """Generate dataset from a JSONL file."""
    dataset = []
    with open(input_file, 'r') as file:
        for line in file:
            entry = json.loads(line)
            dataset.append(entry)
    return dataset

def process_multiple_files(input_dir, output_file):
    """Process multiple files (PDFs, text files, CSVs, JSONL) to create a unified dataset."""
    all_data = []

    for filename in os.listdir(input_dir):
        file_path = os.path.join(input_dir, filename)

        if filename.endswith('.pdf'):
            pdf_data = extract_pdf_data(file_path)
            all_data.append(pdf_data)

        elif filename.endswith('.txt'):
            text_data = generate_dataset_from_text(file_path)
            all_data.extend(text_data)

        elif filename.endswith('.csv'):
            csv_data = generate_dataset_from_csv(file_path)
            all_data.extend(csv_data)

        elif filename.endswith('.jsonl'):
            jsonl_data = generate_dataset_from_jsonl(file_path)
            all_data.extend(jsonl_data)

    # Save the unified dataset to JSONL format
    with open(output_file, 'w') as outfile:
        for entry in all_data:
            json.dump(entry, outfile)
            outfile.write('\n')

if __name__ == "__main__":
    input_directory = '/path/to/input/files'  # Directory containing PDFs, text files, CSVs, and JSONLs
    output_filename = '/path/to/output/dataset.jsonl'  # Output file in JSONL format
    process_multiple_files(input_directory, output_filename)
