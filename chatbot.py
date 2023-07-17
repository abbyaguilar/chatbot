import openai
import gradio as gr

openai.api_key = "<api-key>"

def chat_with_bot(input_text):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=input_text,
            max_tokens=5
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"

def chatbot_interface(user_input):
    bot_reply = chat_with_bot(user_input)
    return "Bot: " + bot_reply

inputs = gr.inputs.Textbox(lines=7, label="User Input")
outputs = gr.outputs.Textbox(label="Bot Reply")

gr.Interface(fn=chatbot_interface, inputs=inputs, outputs=outputs, title="Chatbot", 
             description="Enter your message and get a response from the chatbot.",
             theme="compact").launch()