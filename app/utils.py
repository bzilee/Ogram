import requests
import json
from app.settings import *


def send_file(chat_id, file_name):
    """
        This method will send a file to the chat_id specified
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
    result = json.loads(r.content.decode())
    direct_link = "[x] Operation failed !"
    print("[+] status : ", result["ok"])

    try:
        file_name = result["result"]["document"]["file_name"]
        file_id = result["result"]["document"]["file_id"]
        file_size = result["result"]["document"]["file_size"]

        # thumb = result["result"]["document"]["thumb"]

        print("[+] file_id : ", file_id)
        print("[+] file : ", result["result"]["document"])

        print("[+] Fetching the direct_link the file")

        # Now we fetch the tempory file path
        url2 = "https://api.telegram.org/bot" + TOKEN + "/getFile?file_id=" + file_id
        r2 = requests.get(url2)
        result2 = json.loads(r2.content.decode())

        direct_link = "https://api.telegram.org/file/bot" + TOKEN + "/" + result2["result"]["file_path"]
    except Exception as es:
        print("[x] Failed : ", es)

    return direct_link


# print("direct_link : ", send_file("267092256", "/home/d4rk3r/Pictures/Screenshot from 2020-03-14 18-30-02 - 1.png"))
