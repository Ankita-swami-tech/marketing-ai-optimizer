from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def optimize_content(text):

    prompt = f"""
    Optimize the following marketing content:

    {text}

    Make it:
    - More engaging
    - Clearer
    - Shorter where needed
    - Platform friendly
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    # VERY IMPORTANT: RETURN THE OPTIMIZED CONTENT
    return response.choices[0].message.content
