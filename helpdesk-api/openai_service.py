import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def classify_message(message: str) -> str:
    prompt = (
      f"Classify the user's request strictly as one word only: 'hardware' or 'software'.\n"
      f"Message: \"{message}\"\n"
      f"Respond only with one word: hardware or software."
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=10,
            temperature=0
        )
    except Exception as e:
        raise RuntimeError(f"OpenAI API request failed: {e}")

    answer = response.choices[0].message.content.strip().lower()

    if "hardware" in answer:
        return "hardware"
    elif "software" in answer:
        return "software"
    else:
        raise ValueError(f"Unrecognized category returned: '{answer}'")