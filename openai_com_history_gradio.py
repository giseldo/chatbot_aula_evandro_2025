# Um chatbot acessando a OpenAI com history

from openai import OpenAI
import gradio as gr
import os     

API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=API_KEY)

def response(message, history):
    history.append({"role": "user", "content": message})
    output = client.chat.completions.create(
        messages=history, 
        model="gpt-4o-mini")
    return output.choices[0].message.content             

gr.ChatInterface(fn=response, type="messages").launch()

