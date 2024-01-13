 # ChatBot with Rule-Based Responses

## Overview
This project implements a simple rule-based chatbot in Python. The chatbot analyzes user input and selects a response based on predefined rules. The rules are specified in the `main.py` file, and the bot's long responses are stored in the `long_responses.py` file.

## Files

### `main.py`
This file contains the main logic for the chatbot. Here's a brief breakdown of its components:

#### Functions
1. `message_probability(user_message, recognized_words, single_response=False, required_words=[])`: Calculates the probability of a message matching certain criteria. It considers recognized words, required words, and single response conditions.

2. `check_all_messages(message)`: Evaluates all predefined responses and selects the one with the highest probability based on the user's input.

3. `getResponse(user_input)`: Splits the user input, checks for the most probable response, and returns it.

#### Rules and Responses
- The bot responds to greetings such as 'hello,' 'hi,' 'sup,' 'hey,' and 'heyo' with a simple greeting.
- It responds to inquiries about its well-being with "I am doing great, and you?" if the user includes words like 'how,' 'are,' 'you,' and 'doing.'
- Expressions of love or appreciation trigger a "Thank you" response.
- Specific queries about the bot's actions or state trigger corresponding responses.
- Asking about the bot's name triggers a response revealing its name.
- If no match is found, the bot replies with a default unknown response.

### `long_responses.py`
This file stores long responses that the chatbot uses in specific situations.

## Usage
To use the chatbot, run the `main.py` file. The bot will prompt you to input messages, and it will respond based on the predefined rules.

Feel free to customize the rules and responses in the code to suit your preferences or add more functionality to the chatbot.

## Author
M Mohammad Anas 