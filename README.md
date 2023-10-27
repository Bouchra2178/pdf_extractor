# PDF Data Extractor

This is a Streamlit application designed for extracting data from PDF files. It utilizes Langchain technology for efficient data extraction and provides a user-friendly interface to upload PDF files, extract information, and convert the extracted data into CSV and JSON formats.

## Features
- Upload PDF files for data extraction.
- Extracted data is displayed in a structured manner.
- Convert extracted data to CSV and JSON formats.
- Download the extracted data in CSV or JSON formats.

## Usage
1. Install the required libraries: `streamlit`, `pandas`.
2. Run the Streamlit application using `streamlit run main.py`.
3. Upload your PDF files and click "Extract your data" to start the extraction process.
4. Download the extracted data in CSV or JSON formats using the provided buttons.
## How to Run
To get started, ensure that Python is installed and follow these steps:

1. Install the necessary dependencies by running the command:
    ```bash
    pip install -r requirements.txt
    ```

2. Run the Streamlit application by executing:
    ```bash
    streamlit run main.py
    ```

## Technology Used
The application leverages Langchain technology for efficient data extraction and processing.

## Folder Structure
The project consists of the following main files:

- `main.py`: Contains the Streamlit application code.
- `functions.py`: Includes functions specifically designed for data extraction from PDF files.
