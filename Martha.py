import openai
import gradio

openai.api_key = "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"

# where we customise the model 
messages = [{"role": "system", "content": """You are a multilingual customer care AI assistant named Martha. You reply in the same language of the
              questions asked to you.
              You are polite, considerate and want your customer's experience to be as best as possible."""}]
#helper function to be passed into the Model
def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Martha, The intelligent Customer Care AI")

demo.launch(share=True)