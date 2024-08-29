# Your First LLM Project

**Slides for this page:** [Your First LLM Project Slides](Your%20First%20LLM%20Project%20Slides.pdf)

For your first LLM project we will create a simple terminal interface to chat with an LLM. The final result will look like this:

![](building_llm_systems_1.mp4)

To accomplish this we need the following pieces:
- Get an API key for Gemini
- A way to call the LLM
- A data structure to store the chat history
- A control flow to manage everything

## Get Your Gemini API Key
Before we start building we need to get access to the models we will be using for this course, Google's Gemini 1.5 Flash and Pro. Cloud based LLMs use API keys to authenticate, so you will need an API key first. 

To get a Gemini API key head over to [Google's AI Studio](https://aistudio.google.com/). You will need a Google account to sign into the AI studio, and you must also agree to the legal notice. Once that is done click **Get API Key** at the top left. From there you can create an API key in a new project or choose an existing project. 

> [!note] 
> As of the time of writing billing is not required to set up a free tier API key.

Once you create your API key you can save it either as an environment variable or in a configuration file that is not included in a code repository. 

## Call the LLM
Once we have our API key we can make our first call to Gemini. Google has a Python SDK for interacting with the Gemini API. You can install it with from [PyPI](https://pypi.org/project/google-generativeai/):

```bash
pip install -U google-generativeai
```

Once installed you can import the SDK and add in your API key. Then we can select our model, call the `generate_content` method, and print the results. I put this code in a file called [`first_llm_call.py`](https://github.com).

```python
import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GEMINI_API_KEY"]) # Set API Key

# Set the model name
model = genai.GenerativeModel('gemini-1.5-flash')

# Call the model with a prompt
response = model.generate_content("Who was the first President of Mongolia?")

# Print the results
print(response.text)
```

After running the file you will see this output.

```plaintext
(llm) 02_first_llm_project % python first_llm_call.py

The first President of Mongolia was **Damdin Sükhbaatar**. He was elected on **July 11, 1924**, but sadly, he died only a few months later on **February 20, 1925**, before officially assuming the presidency.

However, due to his role in the Mongolian Revolution and his leadership in establishing the Mongolian People's Republic, he is considered the **founding father of modern Mongolia**.

It is important to note that Mongolia's first **elected president** was **Punsalmaagiin Ochirbat**, who took office in 1990 after the collapse of the communist regime.
```

That's it! You called the Gemini model with a prompt and it returned the result.

## Storing the Chat History
After each question it would be great if the LLM could remember the previous messages in the conversation. That way we don't have to constantly reference things we said before and the conversation can flow more naturally. 

The standard way to store chat history with Python for most flavors of LLMs is a list of dictionaries. In Gemini's case it looks like this:

```python
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(
    history=[
        {"role": "user", "parts": "Hello"},
        {"role": "model", "parts": "Great to meet you. What would you like to know?"},
    ]
)

response = chat.send_message("What is the tallest building in the world?")
print(response.text)
```

Note that there is a `role` and `parts` key for each dictionary. The `role` contains either `user` or `model` depending on who was speaking. The conversation goes from oldest to newest, not including the current message being sent to the model.

To include chat history with the current prompt you can use the `start_chat` method 

> [!note]
> Gemini's chat history structure is different from OpenAI's in that the current user message is not included with the other chat messages. Instead it is sent after the chat history is built using the `send_message` method.

## Building the Control Flow
The goal of our terminal application is to be able to have a conversation with the Gemini model and for it to remember the history as we converse with the model. The easiest way to accomplish this is with a `while` loop to keep the conversation running until we exist. 

Something like this:

```python
chat = model.start_chat()

while True:
    # Prompt the user for input
    user_input = input("You: ")

    # Break the loop if the user wants to exit
    if user_input.lower() == "/bye":
        print("Exiting chat.")
        break

    # Send the user's message to the model. 
    # History is automatically saved to the chat object.
    response = chat.send_message(user_input)
    print("Gemini: " + response.text)
```

With this the chat will continue until the loop is broken with one of the quit commands. The response is retrieved then printed out. The chat history is saved automatically in the `chat` object and passed to the model for each subsequent message.

If you wanted to control the chat history manually you can save each message in a list of dictionaries using the structure above and rebuild the chat with each new message. Why would you want control of the chat history? The main reason is to reduce the number of messages being sent to the model, which will speed up replies and reduce API usage (which is charged by tokens, more on that later).

## Putting it All Together
Now that we’ve gone over how to call the Gemini model, store chat history, and manage the conversation flow, let’s put everything together into a single script. This script will allow you to have a conversation with the Gemini model in your terminal, with the chat history remembered as you go.

Here’s the final version of our chat application. I'll save it in a file called [`first_project.py`](https://github.com).

```python
import google.generativeai as genai
import os
import sys

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel('gemini-1.5-flash')

# Start the chat with no chat history
chat = model.start_chat()

while True:
    # Prompt the user for input
    user_input = input("You: ")

    # Break the loop if the user wants to exit
    if user_input.lower() in ["/exit", "/quit", "/q", "/bye"]:
        print("Exiting chat.")
        break

    # Send the user's message to the model. History is automatically saved.
    response = chat.send_message(user_input)
    print("Gemini: " + response.text)

```

### How It Works:

1. **API Configuration:** We start by configuring the Gemini API with your API key, which is retrieved from an environment variable.
2. **Start a Chat:** We then initiate a new chat session with the start_chat() method. This will automatically handle the chat history, which means you don’t need to manually manage the conversation state unless you want to.
3. **User Input and Control Flow:** The script enters a while loop that continues to prompt the user for input. The loop will only break if the user types "/bye", which will end the conversation and exit the script.
4. **Send and Receive Messages:** Inside the loop, the user’s input is sent to the Gemini model using the send_message() method. The model’s response is then printed out to the terminal.

## Congratulations
That's it, you built your first Python program that interacts with an LLM! Most of the complexity of these deep neural networks has been abstracted away with powerful libraries. This allows us to build great things with very little effort.

**Next Section: [Counting Tokens and Rate Limits](Counting%20Tokens%20and%20Rate%20Limits.md)**