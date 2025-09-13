import os
import requests

GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"
GEMINI_API_KEY = "AIzaSyBsfin-yjWUsYIYoKU8NijUa4v0l-mgXZQ" # Set your key in your environment!
def generate_interview_questions(field, difficulty, num_questions):
    prompt = (
        f"Generate {num_questions} unique interview questions for a {field} interview. "
        f"Difficulty: {difficulty}. Return only plain questions, no answers, as a numbered list. this questions are going to be read by a voice assistant so do not use  any special charactors which might break the voice assistant. "
    )
    payload = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }
    headers = {
        "Content-Type": "application/json",
        "x-goog-api-key": GEMINI_API_KEY,
    }
    response = requests.post(GEMINI_URL, json=payload, headers=headers)
    response.raise_for_status()
    content = response.json()
    # For debugging
    print(content)

    # Extract the text string properly
    text = content['candidates'][0]['content']['parts'][0]['text']

    # Split into lines, filter numbered questions (lines starting with digit)
    lines = text.split('\n')
    questions = [line.strip() for line in lines if line and line[0].isdigit()]

    # Remove numbering prefix
    questions = [q.partition('. ')[2] if '. ' in q else q for q in questions]

    return questions
