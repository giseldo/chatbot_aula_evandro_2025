import gradio as gr

# Histórico de mensagens
chat_history = []

# Função que processa as mensagens do usuário
def chatbot(message, history):
    # Respostas simples baseadas em palavras-chave
    message = message.lower()
    
    if "olá" in message or "oi" in message or "hello" in message:
        response = "Olá! Como posso ajudar você hoje?"
    elif "como vai" in message or "tudo bem" in message:
        response = "Estou bem, obrigado por perguntar! E você?"
    elif "tchau" in message or "adeus" in message:
        response = "Até mais! Foi um prazer conversar com você."
    elif "ajuda" in message:
        response = "Posso ajudar com informações gerais. O que você gostaria de saber?"
    elif "nome" in message:
        response = "Meu nome é GradioBot. Sou um assistente virtual simples."
    elif "obrigado" in message or "valeu" in message:
        response = "Por nada! Estou aqui para ajudar."
    else:
        response = "Desculpe, não entendi. Pode reformular sua pergunta?"
    
    # Adicionar ao histórico
    chat_history.append((message, response))
    
    return response

# Configuração da interface do Gradio
with gr.Blocks() as demo:
    gr.Markdown("# 🤖 Chatbot Simples")
    gr.Markdown("### Converse com este assistente virtual simples")
    
    chatbot_interface = gr.Chatbot()
    msg = gr.Textbox(placeholder="Digite sua mensagem aqui...", label="Sua mensagem")
    clear = gr.Button("Limpar conversa")
    
    # Eventos
    msg.submit(
        chatbot, 
        [msg, chatbot_interface], 
        [chatbot_interface]
    ).then(
        lambda: "", None, [msg]  # Limpa o campo de texto após envio
    )
    
    clear.click(lambda: None, None, chatbot_interface, queue=False)

# Iniciar o servidor Gradio
if __name__ == "__main__":
    demo.launch()
