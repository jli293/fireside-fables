from flask import Blueprint, render_template, request
from .models import Result
from dotenv import load_dotenv
import os
from openai import OpenAI


load_dotenv()

routes = Blueprint('routes', __name__)
OpenAI.api_key = os.getenv('OPENAI_API_KEY')
# completion = openai.Completion()
client = OpenAI()


def summarize(passage, chat_log=None):
    """
    Takes in a query and returns a response from GPT-3.5 Turbo
    :param passage: string
    :param chat_log: string
    :return: string
    """
    prompt = f'{chat_log}Human: {passage}\nCliff Bot:'
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system",
             "content": "You are a helpful assistant designed for summarization tasks and outputs JSON."},
            {"role": "user", "content": passage}
        ]
    )

    # return response.choices[0].message.content
    return response['choices'][0]['message']['content']


@routes.route('/', methods=['GET', 'POST'])
def home():
    return render_template('response_view.html')