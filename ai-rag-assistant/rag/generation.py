from dotenv import load_dotenv
import os
import traceback

from openai import OpenAI
from openai import RateLimitError, AuthenticationError

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

print("API KEY DETECTED:", "Yes" if api_key else "No")

client = OpenAI(api_key=api_key) if api_key else None


def generate_answer(context, question):
    """
    Generates an answer using retrieved document context.
    If OpenAI API is unavailable, falls back to local response.
    """

    prompt = f"""
You are an AI assistant answering questions based on provided documents.

Use ONLY the context below to answer the question.
If the answer is not present in the context, say that the information is not available.

Context:
{context}

Question:
{question}

Answer:
"""

    if client:
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You answer questions based on provided context."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.2
            )

            return response.choices[0].message.content

        except RateLimitError as e:
            print("OpenAI Rate Limit Error:", str(e))
            print(traceback.format_exc())

        except AuthenticationError as e:
            print("OpenAI Authentication Error:", str(e))
            print(traceback.format_exc())

        except Exception as e:
            print("Unexpected OpenAI Error:", str(e))
            print(traceback.format_exc())

    else:
        print("No OPENAI_API_KEY detected. Running in local fallback mode.")

    fallback_response = f"""
Local Mode Activated (OpenAI API unavailable)

Based on the retrieved context, here is relevant information:

{context[:500]}

Your Question:
{question}

To enable full AI answers, set your OpenAI API key using:
export OPENAI_API_KEY=your_api_key_here
"""

    return fallback_response