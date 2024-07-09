import os
from openai import OpenAI
from dotenv import load_dotenv
import csv

# Load knowledge from .env file
# Knowledge is responsible to feed the llm with private information where 
# Based on the input the model chooses if to use or not the information provided.

load_dotenv()
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
# read knowledge from the knowledge.txt file
with open("knowledge.txt", "r") as file:
    knowledge_content = file.read()

# Demo process procedure
def get_order_status(order_id):
    return f"Order id number {order_id} is being processed."

# Demo human request 
def request_human_representative(name, email, phone):
    with open('contact_requests.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, email, phone])
    return "Your request has been saved. A human representative will contact you soon."

#  Chat bot using open ai.
#  Using the model gpt-4o as it the newest most efficient model with new features. 
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
