import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv(dotenv_path=".env")

# Get Gemini API Key
API_KEY = os.getenv("GEMINI_API_KEY")
print("API KEY =", os.getenv("GEMINI_API_KEY"))

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found. Please add it in the .env file.")

# Configure Gemini
genai.configure(api_key=API_KEY)

# Load Gemini Model
model = genai.GenerativeModel("gemini-3.5-flash")


def get_ai_response(user_message):
    """
    Generate AI response for student support queries.
    """

    prompt = f"""
You are an AI Student Support Chatbot.

Your job is to answer only student-related questions.

You can answer questions about:
- Admission
- Fees
- Attendance
- Hostel
- Examination
- Library
- Scholarship
- Placement
- Courses
- Faculty
- Timetable
- General college information

If the user asks anything unrelated to student support,
politely reply:

"Sorry, I can only answer student support related questions."

Student Question:
{user_message}
"""

    try:
        response = model.generate_content(prompt)

        if hasattr(response, "text") and response.text:
            return response.text

        return "Sorry, I couldn't generate a response."

    except Exception as e:
        return f"Error: {str(e)}"
