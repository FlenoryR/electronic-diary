import json
import os


def open_data():
    with open(f'{os.path.dirname(os.path.abspath(__file__))}/data.json') as data:
        content = json.loads(
            data.read()
        )

    return content


def save_data(content):
    with open(f'{os.path.dirname(os.path.abspath(__file__))}/data.json', 'w') as data:
        json.dump(content, data)
