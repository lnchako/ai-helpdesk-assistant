import streamlit as st
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("AI IT Helpdesk Assistant")

user_input = st.text_input("Describe your IT issue:")

if user_input:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an IT support specialist. Give clear, step-by-step troubleshooting help."},
            {"role": "user", "content": user_input}
        ]
    )

    answer = response.choices[0].message.content
    st.write("### Solution:")
    st.write(answer)