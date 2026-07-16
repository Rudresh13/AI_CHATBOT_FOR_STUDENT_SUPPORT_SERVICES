import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def get_response(question):
    prompt = f"""
    You are a Student Support AI chatbot.
    Answer only student-related questions such as:
    - Admission
    - Fees
    - Attendance
    - Hostel
    - Examination
    - Library
    - Placement
    - General College Information

    If the question is unrelated, politely say:
    "Sorry, I can only answer student support queries."

    Student Question:
    {question}
    """

    response = model.generate_content(prompt)
    return response.text
