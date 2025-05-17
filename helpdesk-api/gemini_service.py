import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def classify_message(message: str) -> str:
  prompt = (
    f"Classify the user's request strictly as one word only: 'hardware' or 'software'.\n"
    f"Message: \"{message}\"\n"
    f"Respond only with one word: hardware or software."
  )

  try:
    response = client.models.generate_content(
      model="gemini-2.0-flash",
      contents=prompt
    )
    answer = response.text.strip().lower()
  except Exception as e:
    raise RuntimeError(f"Falha na requisição à API Gemini: {e}")

  answer = response.text.strip().lower()

  if "hardware" in answer:
    return "hardware"
  elif "software" in answer:
    return "software"
  else:
    raise ValueError(f"Unrecognized category returned: '{answer}'")