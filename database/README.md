
# Scientific Quiz Database Filler

This project is designed to populate a database with quiz questions and answers sourced from Excel files. It is particularly useful for managing scientific quizzes where the questions and answers are stored in spreadsheets and need to be structured for database storage.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Running the Application with Command-Line Arguments](#running-the-application-with-command-line-arguments)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)

## Introduction

This project provides tools to read data from Excel files and store it in a structured format within a database. The project is particularly useful for educational institutions, researchers, and educators who manage quiz questions and answers in Excel and need to transfer this data into a database for easier access and management.

## Features

- **Excel Data Parsing**: Reads and processes quiz questions and answers from Excel files.
- **Database Population**: Fills a database with the parsed data, organizing it into a format suitable for quiz management.
- **Data Backup and Restoration**: Includes functionality to backup and restore quiz data as needed.

## Installation

To get started with this project, follow these steps:

1. **Install Dependencies**:
    Make sure you have Python installed. Then, install the necessary Python packages:
    ```bash
    pip install -r ../requirements.txt
    ```

2. **Set Up Environment Variables**:
   If the project requires any environment variables, create a `../.env` file in the root directory and add the necessary environment variables.

## Usage

### Running the Application with Command-Line Arguments

The `main.py` script can be run with different command-line arguments to perform various operations:

1. **Insert Questions into the Database**:
    ```bash
    python main.py <path-to-excel-file>
    ```
   - Example: `python main.py quiz_yip.xlsx`
   - This command will read questions from the specified Excel file and insert them into the database.

2. **Delete All Questions from the Database**:
    ```bash
    python main.py delquestions
    ```
   - This command will delete all quiz questions from the database.

3. **Delete a Single Question**:
    ```bash
    python main.py delquestion
    ```
   - This command will delete a specific quiz question from the database.

4. **Delete All Questions and Users**:
    ```bash
    python main.py delall
    ```
   - This command will clear all quiz questions and users from the database.

### Custom Modules

- **modules/exel2db.py**: Handles the conversion of Excel data to database entries.
- **modules/json2col.py**: Provides functionality to convert JSON data to specific columns in the database.
- **modules/mod.py**: Contains additional helper functions for data processing.

### Example Data Files

The project includes example Excel files (`quiz_yip.xlsx`, `quiz_yipf.xlsx`) and JSON files that demonstrate the format and structure of the quiz data. These can be modified or replaced with your own data.

## Project Structure

Here's an overview of the project's structure:

```
.
├── main.py
├── modules/
│   ├── __init__.py
│   ├── exel2db.py
│   ├── json2col.py
│   └── mod.py
├── database/
│   ├── quiz_yip.xlsx
│   ├── quiz_yipf.xlsx
│   ├── QA.json
│   ├── QA.xlsx
│   └── [additional data files]
├── requirements.txt
└── README.md
```

- **main.py**: The entry point for running the script to process and store quiz data.
- **modules/**: Contains custom Python modules used for data processing and database interaction.
- **database/**: Contains example data files and backups of the database.

## Technologies Used

- **Python**: The core language used for data processing and script execution.
- **Pandas**: For handling and processing data in Excel and JSON files.
- **OpenPyXL**: For reading and writing Excel files.
- **JSON**: Used for data storage and transfer in some parts of the project.