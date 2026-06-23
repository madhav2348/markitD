# MarkItDown Converter Web App

A simple web application to convert documents to markdown using Microsoft's MarkItDown library.

## Setup

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the server
```bash
python server.py
```

### 3. Open in browser
Navigate to `http://localhost:5000`

## Usage

1. Select a file (PDF, DOCX, PPTX, HTML, TXT, XLSX, CSV, JSON, XML)
2. Click "Convert" button
3. View the markdown output
4. Copy to clipboard or download as .md file

## Supported Formats

- PDF
- DOCX (Word documents)
- PPTX (PowerPoint presentations)
- HTML
- TXT (Plain text)
- XLSX (Excel spreadsheets)
- CSV
- JSON
- XML

## Features

- File upload and conversion
- Copy converted markdown to clipboard
- Download as .md file
- Clear output
- Simple, no-frills interface

## Requirements

- Python 3.7+
- Flask
- MarkItDown (by Microsoft)
