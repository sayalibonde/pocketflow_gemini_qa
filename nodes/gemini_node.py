import os
from dotenv import load_dotenv
import google.generativeai as genai
from pocketflow import Node

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use Gemini 2.5 Flash Preview model
model = genai.GenerativeModel(model_name="gemini-2.5-flash-preview-05-20")


class GeminiNode(Node):
    def prep(self, shared):
        return shared.get("input", "")

    def _exec(self, question: str) -> str:
        if not question or not isinstance(question, str):
            return "❌ Please ask something."

        #print("[DEBUG] Sending to Gemini:", question)

        try:
            response = model.generate_content(question)
            reply = response.text.strip() if response and response.text else "⚠️ No reply from Gemini."
            #print("[DEBUG] Gemini replied:", reply)
            return reply
        except Exception as e:
            print("[ERROR]", e)
            return f"❌ Error: {str(e)}"

    def post(self, shared, prep_res, exec_res):
        return exec_res
