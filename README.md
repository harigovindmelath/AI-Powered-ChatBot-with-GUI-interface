# AI-Powered-Chatbot-with-GUI-Interface
This project integrates OpenAI's GPT model (gpt-3.5-turbo-0125) to create an interactive chatbot application. The project features two main components:
1. Backend: Chatbot Class

The chatbot functionality is implemented using OpenAI's API. It processes user inputs and generates responses based on GPT-3.5's natural language processing capabilities.
Features:

  OpenAI API Integration: Leverages OpenAI's chat.completions.create method to interact with the GPT model.
  Dynamic Responses: Processes user queries and generates relevant, human-like responses.
  Scalable Design: The chatbot class is modular and can be easily extended to support additional functionality.

2. Frontend: PyQt6 GUI

A graphical user interface (GUI) is built using PyQt6 to make the chatbot user-friendly and accessible.
Features:

   Chat Area: A QTextEdit widget displays the conversation history between the user and the chatbot.
   Input Field: A QLineEdit widget allows the user to type their queries.
   Send Button: A QPushButton triggers the chatbot to process user input and display responses in the chat area.

GUI Specifications:

  Responsive Design: The window is sized at 700x600 pixels, making it compact and user-friendly.
  Interactive: Allows seamless communication with the chatbot in a real-time environment.

How to Use

Install the required dependencies:

    pip install openai pyqt6

Replace the placeholder API key in the chatbot class with your OpenAI API key.
Run the Python script:

    python chatbot_gui.py

Interact with the chatbot using the GUI.
