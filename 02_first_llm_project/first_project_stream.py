import google.generativeai as genai
import os
import sys

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel('gemini-1.5-flash')

# Start the chat with an initial prompt
chat = model.start_chat()

while True:
    # Prompt the user for input
    user_input = input("You: ")

    # Break the loop if the user wants to exit
    if user_input.lower() in ["/exit", "/quit", "/q", "/bye"]:
        print("Exiting chat.")
        break

    # Send the user's message to the model.
    # Chat history is saved automatically!
    print("Gemini: ", end="", flush=True)
    response = chat.send_message(user_input, stream=True)

    for chunk in response:
        print(chunk.text, end="", flush=True)

    print()  # Print a newline after the full response
