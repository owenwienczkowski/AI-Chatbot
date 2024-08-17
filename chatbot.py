# this program introduces chatbots and AI assistants

from openai import OpenAI
from keys import key

client = OpenAI(
    api_key = key
)

end_program = False

while not end_program:
    get_input = input("Enter a prompt: ")
    if get_input.lower() == "goodbye" or get_input.lower() == "exit":
        end_program = True
        print("Have a great day!")
    else:
        system_data = [
            {"role": "system", "content": "You are an assistant that only answers math questions."},
            {"role": "user", "content": get_input}
        ]
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=system_data
        )
        assistant_response = response.choices[0].message.content
        system_data.append({"role": "assistant", "content": assistant_response})
        print("Assistant: " + assistant_response)