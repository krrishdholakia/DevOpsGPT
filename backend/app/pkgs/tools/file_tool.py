import os
import logging
from config import WORKSPACE_PATH

def read_file_content(filename):
    logging.info("read_file_content: %s", filename)
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            result = True
    except FileNotFoundError:
        content = ''
        result = False
    return result, content

def write_file_content(filename, content):
    logging.info("write_file_content: %s", filename)
    directory = os.path.dirname(filename)
    os.makedirs(directory, exist_ok=True)
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
            result = True
    except PermissionError:
        result = False
    return result

def get_ws_path(task_id):
    return os.path.join(WORKSPACE_PATH, task_id)
