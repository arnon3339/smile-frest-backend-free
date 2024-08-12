# QR Code PDF Generator

This project generates a PDF file that contains all QR code images in a specified input directory. The PDF is formatted with 3 QR codes per row. The output is a `results.pdf` file located in the root directory, which consolidates all pages created from the QR code images.

## Features

- **Batch Processing**: Processes all QR code images in the specified input directory.
- **PDF Formatting**: Arranges QR codes into a grid with 3 columns per row.
- **Output**: Generates a `results.pdf` file containing all QR codes in the root directory.

## How It Works

1. **Input Directory**: Place all your QR code images in the specified input directory.
2. **Output Directory**: Generated pages with arranged QR codes will be stored in the specified output directory.
3. **Final Output**: The `results.pdf` file is generated in the root directory, containing all the pages from the output directory.

## Usage

1. **Install Required Libraries**: 
   ```bash
   pip install -r ../requirements.txt
   ```
2. Prepare your QR code images and place them in the input directory.
3. Run the script:
   ```bash
   python main.py
   ```
4. The processed PDF will be stored as `results.pdf` in the root directory.

## Requirements

- Python 3.x
- Required Python libraries listed in `requirements.txt` (e.g., `reportlab`, `Pillow`, etc.)

## Example

1. Input Directory: `input/`
2. Output Directory: `output/`
3. Final PDF: `results.pdf`