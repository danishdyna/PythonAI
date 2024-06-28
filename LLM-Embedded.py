from ollama import chat
messages = [
  {
    'role': 'user',
    'content': 'Why is the sky blue? Use max 9 words.',
  },
]
print(messages[0]['content'])
response = chat('phi3'   , messages=messages)
print(response['message']['content']) # type: ignore
