# Week 1 - Terminal Chat Application

## Objective:

The goal of this assignment is to get hands-on experience with building a simple terminal-based chat application using Python. You will integrate this chat application with the Gemini API to stream text responses back to the user. This will lay the foundation for understanding how to build interactive, LLM-powered systems.
## Requirements:

Your task is to create a Python-based terminal chat application that meets the following criteria:
### 1. Streaming Text Responses:

The application should stream text responses from the Gemini API back to the user in real-time. This will simulate a natural conversation flow, similar to chatbots and interactive systems.

### 2. Help Menu:

Users should be able to access a help menu at any time by typing /help. The help menu should provide the following information:
- Instructions on how to use the application.
- A list of available commands, including /quit to exit the application.
- Any other relevant information the user might need.
### 3. User Input Handling:

- The application should handle various user inputs gracefully. This includes providing appropriate feedback when the user enters an invalid command or input.
- If the user types /quit, the application should end the chat session and exit gracefully.
### 4. Logging:

The application should log each user interaction (timestamped) to a text file. This includes logging user inputs and the corresponding responses from Gemini. Ensure that the log file is accessible and well-organized for future reference.
## Deliverables:
A single executable Python file that conforms to the requirements above. Submit assignments on Moodle.
## Evaluation Criteria:
Your submission will be evaluated based on the following criteria:
- **Functionality:** Does the chat application meet all the specified requirements? Does it integrate correctly with the Gemini API and stream text responses effectively?
- **Code Quality:** Is your code well-organized, readable, and properly commented? Have you followed Python best practices?
- **User Experience:** Is the application intuitive and user-friendly? Does the help menu provide clear and useful information?
- **Logging:** Is the logging mechanism correctly implemented, and does it provide meaningful and organized output?