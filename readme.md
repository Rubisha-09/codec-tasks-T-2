# Automated Resume Parser

## Description
This project is an automated resume parsing system that extracts candidate name and skills from PDF resumes using NLP techniques.

## Technologies Used
- Python
- Flask
- spaCy
- PDFPlumber

## Features
- Upload resume (PDF)
- Extract candidate name
- Identify skills
- Display extracted data

## How to Run
1. Install dependencies:
   pip install -r requirements.txt

2. Download NLP model:
   python -m spacy download en_core_web_sm

3. Run the application:
   python app.py

4. Upload resume using POST request:
   http://127.0.0.1:5000/upload

## Outcome
An automated resume parser that extracts useful information from resumes.
