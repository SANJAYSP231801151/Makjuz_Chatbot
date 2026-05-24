import os
from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("GEMINI_API_KEY not found in .env file.")
    exit(1)
genai.configure(api_key=api_key)
try:
    model = genai.GenerativeModel(model_name="models/gemini-1.5-flash-latest")
except Exception as e:
    print("Failed to load model:", e)
    exit(1)
chat = model.start_chat(history=[
    {
        "role": "user",
        "parts": [
            "You are a friendly and helpful customer service assistant for MAKJUZ TECHNOLOGY, "
            "a startup that provides web development, AI integration, and IT consulting services. "
            "Answer questions politely, clearly, and professionally as if you're chatting with customers."
        ]
    }
])
def get_gemini_response(user_input):
    try:
        response = chat.send_message(user_input)
        return response.text
    except Exception as e:
        return f"Error: {e}"
def main():
    print("Welcome to MAKJUZ TECHNOLOGY's Customer Service Chatbot (Powered by Gemini 2.5 Flash)")
    print("Type 'exit' or 'quit' to end the conversation.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Bot: Thank you for chatting. Goodbye! 👋")
            break
        reply = get_gemini_response(user_input)
        print("Bot:", reply, "\n")
if __name__ == "__main__":
    main()
