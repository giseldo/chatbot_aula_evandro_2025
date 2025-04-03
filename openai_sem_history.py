# Um chatbot acessando a OpenAI sem history

from openai import OpenAI
import gradio as gr
import os     

API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=API_KEY)

def response(message, history):
    output = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "Vc é brasileiro e fala portugues"},      
            {"role": "user", "content": message}
        ], 
        model="gpt-4o-mini")
    return output.choices[0].message.content             

gr.ChatInterface(fn=response).launch()

