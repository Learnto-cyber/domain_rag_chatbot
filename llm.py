import os
from groq import Groq
from dotenv import load_dotenv

from prompt import build_prompt

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_answer(context, question):
    """
    Generate an answer using the retrieved context and user's question.
    """

    prompt = build_prompt(context, question)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
        max_tokens=1024
    )

    return response.choices[0].message.content