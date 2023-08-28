import requests

def get_user_input():
    return input("Enter your message: ")

def call_chat_gpt(prompt):
    response = requests.post(
        "https://api.openai.com/v1/engines/davinci-codex/completions",
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer YOUR_API_KEY"
        },
        json={
            "prompt": prompt,
            "max_tokens": 60,
            "temperature": 0.7
        }
    )
    return response

def handle_response(response):
    if response.status_code != 200:
        print("Error with API request")
        return None
    data = response.json()
    message = data["choices"][0]["text"]
    print("ChatGPT response: ", message)
    return message

while True:
    user_input = get_user_input()
    response = call_chat_gpt(user_input)
    message = handle_response(response)
    if message is None:
        break
    user_input = input("Would you like to continue? (y/n): ")
    if user_input.lower() not in ["y", "yes"]:
        break