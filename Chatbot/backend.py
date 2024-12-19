from openai import OpenAI


class chatbot():
    def __init__(self):
        self.client = OpenAI(api_key='api_key')

    def get_response(self, user_input):
        response = self.client.chat.completions.create(
            model='gpt-3.5-turbo-0125',
            messages=[
                {"role": "system", "content": f"f{user_input}"}
            ])

        return response.choices[0].message.content


if __name__ == '__main__':
    chatbot = chatbot()
    response = chatbot.get_response("Tell about kerala")
    print(response)
