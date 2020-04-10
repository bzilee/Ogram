import requests
import json
from app.settings import *


def get_direct_link(file_id):
    """

    :param file_id:
    :return:
    """
    print("[+] Fetching the direct_link the file")

    # Now we fetch the tempory file path
    url2 = "https://api.telegram.org/bot" + TOKEN + "/getFile?file_id=" + file_id
    r2 = requests.get(url2)
    result2 = json.loads(r2.content.decode())

    return "https://api.telegram.org/file/bot" + TOKEN + "/" + result2["result"]["file_path"]


def upload_chunk(chat_id, file_name):
    """
    This method will build the payload to be upload on telegram api

    :param chat_id:
    :param file_name:
    :return:
    """
    print("[+] Sending the file")
    url = "https://api.telegram.org/bot" + TOKEN + "/sendDocument"
    files = {
        'document': open(file_name, 'rb')
    }
    values = {
        'chat_id': chat_id
    }

    r = requests.post(url, files=files, data=values)

    return json.loads(r.content.decode())


def send_chunk(chat_id, file_name):
    """
        This method will send a file to the chat_id specified
    """
    print("[+] Sending chunk : ", file_name)

    # We upload the chunk and get the result as dict
    result = upload_chunk(chat_id, file_name)

    if result["ok"]:
        file_id = result["result"]["document"]["file_id"]
        print("[+] file_id : ", file_id)

        # Now we fetch the tempory file path from file_id
        direct_link = get_direct_link(file_id)
    else:
        direct_link = "[x] Error, Operation failed !"

    return direct_link


# print("direct_link : ", send_chunk("267092256", "/home/d4rk3r/Pictures/Screenshot from 2020-03-14 18-30-02 - 1.png"))

def send_file(file_name):
    """

    :param file_name:
    :return:
    """

    # We split the file First

    # We send the chunks to Telegram
    pass
