from flask import Blueprint, render_template, request
from .models import Result
from dotenv import load_dotenv
import os
import time
from openai import OpenAI


load_dotenv()

routes = Blueprint('routes', __name__)
OpenAI.api_key = os.getenv('OPENAI_API_KEY')
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
             "content": "You are a helpful assistant designed that outputs JSON."},
            {"role": "user", "content": passage}
        ]
    )

    return response.choices[0].message.content
    # return response['choices'][0]['message']['content']


def generate_bonfire_story(elements):
    """
    Takes in a list of elements and returns a story from GPT-3.5
    :param elements:
    :return:
    """
    story_prompt = "Create a 150-word bonfire story with the following elements: "

    story_prompt = story_prompt + elements
    story_prompt += ".\n\n"

    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=story_prompt,
        temperature=0.7,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    time.sleep(1)

    return response.choices[0].text.strip()


history_data = []
@routes.route('/', methods=['GET', 'POST'])
def home():
    # for GET request, return response_view template
    if request.method == 'GET':
        query = request.args.get('query')
        if query == "" or query is None:
            return render_template('response_view.html')

        # response = summarize(query)
        response = generate_bonfire_story(query)

        data_list = []
        query_message = Result(time="This Time", message_type="other-message float-right", message=query)
        response_message = Result(time="This Time", message_type="my-message", message=response)

        data_list.append(query_message)
        data_list.append(response_message)

        history_data.append(query_message)
        history_data.append(response_message)

        return render_template('response_view.html', results=data_list)

    # for other requests, return history template
    else:
        return render_template('history.html', results=history_data)
