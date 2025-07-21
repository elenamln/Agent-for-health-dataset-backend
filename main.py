import os
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from google.generativeai import GenerativeModel, configure
import pandas as pd
from dotenv import load_dotenv

# ✅ Load .env file and configure Gemini
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("GOOGLE_API_KEY is not set in the environment!")

configure(api_key=api_key)  # ✅ This is what you're missing!

# ✅ Now create the model
model = GenerativeModel("models/gemini-1.5-pro")

# ✅ FastAPI setup
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/ask")
async def ask(file: UploadFile = File(...), question: str = Form(...)):
    try:
        print("✅ Received file and question:", question)
        df = pd.read_csv(file.file)
        print(f"📊 Loaded CSV with {len(df)} rows")

        prompt = f"Data:\n{df.head(5).to_csv(index=False)}\n\nQuestion: {question}"
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        print("❌ ERROR:", str(e))
        return {"error": str(e)}
