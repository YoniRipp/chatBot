# README

## Project: E-commerce Conversational Agent

### Objective
Develop a conversational agent (chatbot) to handle customer support queries for an e-commerce platform using OpenAI API. The chatbot can handle multi-turn conversations and provide accurate responses to customer inquiries about order status, return policies, and more.

### Functionalities
1. **Order Status:** When a user asks for the status of an order, the agent asks for the order_id and then responds with the order status.
2. **Request Human Representative:** Gathers contact information for users who want to interact with a person. Saves the information to a CSV file.
3. **Return Policies:** Provides information about the store's return policies, including conditions for returns, non-returnable items, and refund methods.

### Requirements
- Python 3.x
- OpenAI library
- dotenv library

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. **Install the required dependencies:**
   ```bash
   pip install openai python-dotenv
   ```

3. **Create a `.env` file in the project root directory:**
   ```env
   OPENAI_API_KEY="your_openai_api_key"
   ```

4. **Add knowledge file:**
   Ensure `knowledge.txt` is in the same directory as `ebot.py`.
   In this case knowledge includes the given policies.

### Running the Chatbot

1. **Run the chatbot:**
   ```bash
   python ebot.py
   ```

2. **Interact with the chatbot:**
   - Press `1` to get the order status.
   - Press `2` to request a human representative.
   - Press `3` to chat about other information.

### Code Overview

#### ebot.py
```python
import os
from openai import OpenAI
from dotenv import load_dotenv
import csv

# Load knowledge from .env file
load_dotenv()
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Read knowledge from the knowledge.txt file
with open("knowledge.txt", "r") as file:
    knowledge_content = file.read()

def get_order_status(order_id):
    return f"Order id number {order_id} is being processed."

def request_human_representative(name, email, phone):
    with open('contact_requests.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, email, phone])
    return "Your request has been saved. A human representative will contact you soon."

def chatbot_response(user_input):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful customer support."},
            {"role": "system", "content": knowledge_content},
            {"role": "user", "content": user_input}
        ]
    )
    return (completion.choices[0].message.content)

def runBot():
    print("Welcome to our customer support!")
    while True:
        print("Press 1 to get your order status")
        print("Press 2 to request human representative")
        print("Press 3 to chat with both regarding other information")
        user_input = input("You: ")
        if "1" in user_input:
            order_id = input("Chatbot: Please provide your order ID: ")
            print("Chatbot:", get_order_status(order_id))
        elif "2" in user_input:
            name = input("Full Name: ")
            email = input("Email: ")
            phone = input("Phone Number: ")
            print("Chatbot:", request_human_representative(name, email, phone))
        else:
            print("\n""Chatbot: How can I help you?")
            user_input = input("You: ")
            print("Chatbot:", chatbot_response(user_input))
        print()

if __name__ == "__main__":
    runBot()
