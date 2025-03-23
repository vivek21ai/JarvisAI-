from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)