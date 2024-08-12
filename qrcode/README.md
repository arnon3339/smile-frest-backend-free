
# QR Code Generator for Scientific Quizzes

This project is designed to generate QR codes for scientific quizzes. It connects to a database to create unique QR codes that link to quiz questions or related content. The generated QR codes can be stored and managed within the project for easy access and use.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)

## Introduction

This project provides tools to generate QR codes for scientific quizzes. It connects to a database to retrieve quiz data, generate QR codes, and store the generated QR codes in both image and PDF formats.

## Features

- **QR Code Generation**: Generate QR codes based on data retrieved from a database.
- **Default Batch Size**: By default, the script generates 1,000 QR codes.
- **Customizable Batch Size**: You can specify the number of QR codes to generate using `sys.argv[1]`.
- **Automatic Directory Clearing**: The `images/` directory is cleared on every run. To save old QR codes, back up the contents of this directory before generating new codes.
- **Logo Integration**: Customize QR codes by adding logos.
- **PDF Output**: Generate PDFs containing the QR codes for easy sharing or printing.
- **Image Management**: Organize and manage images associated with the QR codes.

## Installation

To get started with this project, follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone <repository-url>
    cd qrcode
    ```

2. **Install Dependencies**:
    Make sure you have Python installed. Then, install the necessary Python packages:
    ```bash
    pip install -r ../requirements.txt
    ```

3. **Set Up Environment Variables**:
   If the project requires any environment variables, create a `../.env` file in the root directory and add the necessary environment variables.

## Usage

### Running the Main Script

To generate QR codes, navigate to the project directory and run `main.py`:

```bash
python main.py
```

This script will connect to the database, process the quiz data, and generate 1,000 QR codes by default. The QR codes will be saved in the `images/` directory.

**Important:** The `images/` directory is cleared on every run. If you want to keep the previously generated QR codes, back up the contents of the `images/` directory before running the script again.

To specify a different number of QR codes to generate, use the following command:

```bash
python main.py <number_of_qrcodes>
```

For example, to generate 500 QR codes:

```bash
python main.py 500
```

### PDF Generation

To create a PDF containing the generated QR codes, navigate to the `write_pdf/` directory and run the corresponding script:

```bash
cd write_pdf
python main.py
```

The output PDF will be saved in the `write_pdf/output/` directory.

## Project Structure

Here's an overview of the project's structure:

```
.
├── main.py
├── json_data.json
├── logo.png
├── logo2.png
├── logo_black.png
├── logo_orange.png
├── images/
│   ├── [Generated QR code images]
├── data/
│   ├── qids.txt
├── write_pdf/
│   ├── main.py
│   ├── blank.pdf
│   ├── result.pdf
│   ├── input/
│   ├── output/
└── README.md
```

- **main.py**: The main script for generating QR codes.
- **json_data.json**: Contains configuration or other data used by the script.
- **images/**: Directory where generated QR code images are stored.
- **write_pdf/**: Contains scripts and resources for generating PDFs with QR codes.

## Technologies Used

- **Python**: The core language used for QR code generation and script execution.
- **qrcode**: Python library for generating QR codes.
- **Pillow**: Python Imaging Library used for image processing.
- **reportlab**: Python library used for generating PDFs.
