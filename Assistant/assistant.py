# first import the required libraries
# Our first goal is to set up the brain of the model, which is ollama here.
# First we will use requesţ library to call the Ollama

import requests
from sys import exit

# Global variable section
MODEL_NAME = "phi3:latest" # From the documentation of the ollama (phi3:latest will be available)
URL = "http://127.0.0.1:11434/api/generate" # API Connection URL to our phi3:latest model running locally

# Function to communicate with the brain
def ask_ollama(user_message):
    sys_prompt = ""
    
    # for role, msg in history:
    #     prompt += f"{role.upper()}: {msg}\n"

    prompt = sys_prompt + f"User: {user_message}\nASSISTANT: "
    res = requests.post(
        URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        }
    )

    response_content_var = res.json()

    # This will be our final response from the ollama server
    return response_content_var["response"].strip()

def main():
    # history = []
    while True:
        try:
            user_message = input("Ask: ")
        except EOFError:
            print("\nBye bye !")
            exit(0)
        except KeyboardInterrupt:
            print("\nBye bye !")
            exit(0)

        print(f"Assistant: {ask_ollama(user_message)}")

        # history.append(f"User: {user_message}")
        # history.append(f"Assistant: {response}")

        # # For optimisation we will only keep last 10 conversation
        # history = history[-10:]

def speak()

if __name__ == "__main__":
    main()