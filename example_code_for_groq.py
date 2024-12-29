# terminal command to activate venv in windows: .\venv\Scripts\activate
# terminal command to activate venv in mac: source venv/bin/activate
# terminal command to install requirements: pip install -r requirements.txt

import os
import streamlit as st

from groq import Groq

client = Groq(
    api_key=st.secrets["GROQ_API_CHATBOT"],
)

chat_completion = client.chat.completions.create(
    messages=[
        {   
            "role": "user",
            "content": "Usage of git for open soruce",
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)













# from groq import Groq

# client = Groq()
# completion = client.chat.completions.create(
#     model="llama3-8b-8192",
#     messages=[],
#     temperature=1,
#     max_tokens=1024,
#     top_p=1,
#     stream=True,
#     stop=None,
# )

# for chunk in completion:
#     print(chunk.choices[0].delta.content or "", end="")
