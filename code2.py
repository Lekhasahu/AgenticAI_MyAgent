import streamlit as st
import requests

API_KEY = "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"

# Model: choose any available on https://openrouter.ai/docs#models
MODEL = "openai/gpt-3.5-turbo"

# OpenRouter endpoint
API_URL = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def ask_openrouter(prompt):
    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()
        answer = response.json()["choices"][0]["message"]["content"]
        return answer.strip()
    except requests.exceptions.HTTPError as err:
        return f"HTTP error: {err}\n{response.text}"
    except Exception as e:
        return f"Error: {e}"

st.set_page_config(page_title="ChatBot using OpenRouter API",page_icon="🤖")
st.title("Hey there, it's Pacifica")
user_input = st.text_input("Hey, Ask me anything you want","")

if user_input:
    with st.spinner("Thinking...please wait"):
        reply = ask_openrouter(user_input)  # ✅ Corrected here
        st.markdown("**🤖Bot:**")
        st.success(reply)


# if __name__ == "__main__":
#     print("ChatBot using OpenRouter API (type 'exit' to quit)\n")
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() in ["exit", "quit"]:
#             break
#         reply = ask_openrouter(user_input)
#         print("Bot:", reply)