# acessando um LLM Local por um programa externo via API

from openai import OpenAI
import gradio as gr
import os     

client = OpenAI(base_url="http://127.0.0.1:1337/v1")

def response(message, history):
    history.append({"role": "user", "content": message})
    output = client.chat.completions.create(
        model="tinyllama-1.1b",
        messages=history)
    return output.choices[0].message.content             

gr.ChatInterface(fn=response, type="messages").launch()
