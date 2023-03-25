import openai

openai.api_key = ""

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

print("\nOpenGPT : The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.")

while True:
    ask = input("\nHuman : ")
    if ask == "exit":
        print("Exiting...Thank you")
        break
    else:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=ask,
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=[" Human:", " AI:"]
        )
        print("\nOpenGPT :", response["choices"][0]["text"])
