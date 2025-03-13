# Um chatbot acessando um LLM local (com download e executando na máquina local)

import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def response(message, history):
   #prompt = [{"role":"user", "content": message}]
   inputs = tokenizer(message)
   result = model.generate(input_ids=inputs.input_ids,      max_new_tokens=20)
   return tokenizer.decode(result[0])

gr.ChatInterface(response, type="messages").launch()
