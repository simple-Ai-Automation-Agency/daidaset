# simple DAiDASET

## Introduction

The simple DAiDASET project is a versatile Python application built with FastAPI, designed to harness artificial intelligence for creating, managing, and analyzing JSONL dataset files. It features tools such as create-dataset.py, dataset-chooser.py, and dataset-evaluator.py, which standardize datasets based on predefined domains and category weights, facilitating the generation of assistant responses tailored to specific use cases. With support for input formats like .txt, .csv, .jsonl, and .pdf, the project streamlines data ingestion, allowing users to extract structured information, process prompts and responses, and analyze existing datasets.

A key focus of DAiDASET is fine-tuning Large Language Models (LLMs), such as Google Gemini 2.0 Flash, Phi-3.5, and others by curating data from various sources, tailored to specific tasks and contexts. This approach minimizes biases and improves model performance in real-world applications. Fine-tuning involves training pre-existing models on domain-specific datasets, ensuring they reflect relevant knowledge, tone, and tasks. Additionally, the project incorporates data augmentation techniques to create variations of data points, reducing overfitting and improving model robustness across diverse scenarios.

By combining flexibility, precision, and a focus on quality, the DAiDASET project provides a robust framework for dataset creation and management. Its tools empower users to produce high-quality datasets that enhance AI model accuracy and reliability while addressing the challenges of bias and generalization. This comprehensive solution simplifies the process of preparing datasets for fine-tuning AI models, ensuring optimal performance for Ai applications.

## JSONL File Format

Our scripts work with datasets in JSONL format. Each line in a JSONL file is a valid JSON object. Here's a glimpse of what our dataset might look like:

```jsonl
{"messages": [{"role": "system", "content": "Classify..."}, {"role": "user", "content": "saas..."}, {"role": "assistant", "content": "History"}]}
{"messages": [{"role": "system", "content": "Classify..."}, {"role": "user", "content": "diskussionsrunden..."}, {"role": "assistant", "content": "Retail"}]}
{"messages": [{"role": "system", "content": "Classify..."}, {"role": "user", "content": "polis..."}, {"role": "assistant", "content": "Consumer Electronics"}]}
```
## Installation and Setup

1. **Clone the Repository:**
   ```
   git clone https://github.com/yourusername/data-preparation-for-fine-tuning.git
   cd data-preparation-for-fine-tuning
   ``` 
2. **Dependencies:**
   Python 3.6+ is required. Install dependencies using:
   ```
   pip install pandas rich configparser
   ```
## Configuration

1. **config.ini File:**
   Create this in the root directory. Modify paths and weights to suit your dataset:
   ```ini
   [Paths]
   jsonl_directory = /path/to/jsonl/files
   output_file = /path/to/output/dataset.jsonl

   [Weights]
   category_weights = {
       "Category1": 0.05,
       ...
   }

   [Settings]
   total_examples = 1000000
   ```
   
## Usage

1. **Dataset Preparation (`dataset-chooser.py`):**
   Reads, shuffles, and categorizes JSONL files. Tailor your dataset for specific modeling needs.
   ```
   python dataset-chooser.py
   ```
2. **Dataset Analysis (`dataset-evaluator.py`):**
   Analyzes the prepared dataset, providing insightful metrics and distributions.
   ```
   python dataset-evaluator.py
   ```
![CleanShot 2024-01-01 at 17 52 05@2x](https://github.com/yigitkonur/data-preparation-for-fine-tuning/assets/9989650/ee8bb83e-1ef1-4fb7-a167-ba9098406da6)

#### Use Cases

- **Model Training:** Prepare balanced or weighted datasets for training machine learning models, ensuring diverse representation across categories.
- **Data Analysis:** Gain insights into the composition of your datasets, identifying prevalent themes or gaps in data.
- **Custom Dataset Creation:** Generate datasets tailored to specific research or business needs, focusing on relevant categories.

## Fine-Tuning Models with Homogenized Data

Utilizing `data-preparation-for-fine-tuning`, you can fine-tune machine learning models with data that's been carefully balanced or weighted according to your specifications. This process involves:

1. Defining category weights in `config.ini` to reflect the desired emphasis in your dataset.
2. Running `dataset-chooser.py` to prepare a dataset that adheres to these weights.
3. Using the processed dataset to train models, ensuring the data is representative and aligned with your goals.

This approach is particularly useful in scenarios where certain categories need more representation or when trying to avoid biases inherent in unbalanced datasets.
