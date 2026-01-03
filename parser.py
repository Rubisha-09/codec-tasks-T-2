import pdfplumber
import spacy
from skills import SKILLS

nlp = spacy.load("en_core_web_sm")

def parse_resume(file_path):
    text = ""

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()

    doc = nlp(text)

    name = "Not Found"
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            name = ent.text
            break

    found_skills = []
    for skill in SKILLS:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    return name, found_skills
