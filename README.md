
# Scientific Quiz Backend

This repository contains the backend infrastructure for a scientific quiz game. The backend reads data from Excel files to populate a database with quiz questions and generates unique QR codes for each quiz, which can be used to access the quizzes via a URL. The project is built with a focus on scalability and reliability, leveraging a MongoDB database for data storage and management.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)

## Introduction

This backend service is designed to support a scientific quiz game where players can test their knowledge through various quizzes. The service handles reading quiz data from Excel files, managing the questions in a MongoDB database, and generating QR codes that link to each quiz.

## Features

- **Database Population**: Reads quiz data from Excel files and populates the MongoDB database with questions.
- **QR Code Generation**: Generates unique URLs for each quiz and stores them in the database, allowing players to access quizzes via QR codes.

## Installation

To get started with this project, follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/arnon3339/smile-frest-backend-free.git
    cd smile-frest-backend-free
    ```

2. **Set Up Environment Variables**:
   Create a `.env` file in the root directory and add the necessary environment variables:
    ```
    DBUSER=<your-database-username>
    DBPW=<your-database-password>
    DBSTRING=<your-database-connection-string>
    DBCLUSTER=<your-database-cluster-url>
    MONGODB_URI=<your-mongodb-uri>
    ```
## Usage

### Database Management

The `database` sub-module handles the population of quiz questions in the MongoDB database. It reads data from specified Excel files and updates the database with new quiz questions.

### QR Code Generation

The `qrcode` sub-module is responsible for generating QR codes for each quiz. These QR codes contain URLs that link directly to the quizzes, making it easy for players to access them.

### Using `main.py` in Sub-Modules

To run specific tasks or scripts within the sub-modules, navigate into the respective sub-module directory and execute `main.py`. For example:

1. **Database Sub-Module**:
    ```bash
    cd database
    python main.py
    ```

2. **QRCode Sub-Module**:
    ```bash
    cd qrcode
    python main.py
    ```

Each sub-module may have its own `main.py` script for handling specific operations related to that module.


## Project Structure

Here's an overview of the project's structure:

```
.
├── database/
│   ├── models/
│   ├── database/
│   └── main.py/
├── qrcode/
│   ├── data/
    ├── write_pdf/
│   └── main.py
├── .env
├── requirements.txt
└── README.md
```

- **database/**: Handles all operations related to reading Excel data and managing the quiz database.
- **qrcode/**: Contains logic for generating and managing QR codes for quizzes.
- **config/**: Configuration files for setting up the application environment.

## Technologies Used

- **Node.js**: JavaScript runtime environment for server-side programming.
- **Express.js**: Web framework for building APIs.
- **MongoDB**: NoSQL database for storing quiz data.
- **Mongoose**: ODM (Object Data Modeling) library for MongoDB and Node.js.
- **xlsx**: Library for parsing Excel files in Node.js.
- **QRCode**: Library for generating QR codes.
