from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_marketing_content(topic, platform):
    prompt = f"""
    Generate high-quality marketing content for:

    Topic: {topic}
    Platform: {platform}

    Requirements:
    - Engaging
    - Trending
    - Human-like
    - Platform optimized
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    # NEW correct return
    return response.choices[0].message.content
