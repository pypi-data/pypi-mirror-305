import requests

class Message:
    def __init__(self, role, content):
        self.role = role
        self.content = content

class ChatHistory:
    def __init__(self):
        self.messages = []

    def add_message(self, role, content):
        self.messages.append(Message(role, content))

    def get_messages(self):
        return [{"role": msg.role, "content": msg.content} for msg in self.messages]

    def clear_history(self):
        self.messages = []

class gpt:
    def __init__(self, model_type='gpt-4o', max_tokens=8000, temperature=0.1, system_prompt=""):
        self.chat_history = ChatHistory()
        self.model_type = model_type
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.system_prompt = system_prompt

    def ans(self, content, role = 'user'):
        self.chat_history.add_message(role, content)
        response = self.llm()
        return response

    def llm(self):
        url = "http://193.109.69.92:8000/chat/"
        payload = {
            "model": self.model_type,
            "messages": self.chat_history.get_messages(),
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
            "top_p": 1,
            "frequency_penalty": 0,
            "presence_penalty": 0
        }

        response = requests.post(url, json=payload)

        if response.status_code == 200:
            response_content = response.json()['choices'][0]['message']['content']
            self.chat_history.add_message("assistant", response_content)
            return response_content
        else:
            return f'{response.status_code}: {response.text}'

    def clear_history(self):
        self.chat_history.clear_history()
