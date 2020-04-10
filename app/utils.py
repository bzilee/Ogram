import requests
import json
import time
import datetime
from app.settings import *
# We import the Class/module
from app.Split import Split


def seconds_elapsed(last_date):
    """
    This method will return the difference between theese two dates
    :param last_date:
    :return:
    """
    earlier = datetime.datetime.now()
    diff = last_date - earlier
    return diff.seconds


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


def send_chunk(chat_id, chunk_name):
    """
        This method will send a file to the chat_id specified
    """
    print("[+] Sending chunk : ", chunk_name)

    # We upload the chunk and get the result as dict
    result = upload_chunk(chat_id, chunk_name)

    if result["ok"]:
        file_id = result["result"]["document"]["file_id"]
        print("[+] file_id : ", file_id)

        # Now we fetch the tempory file path from file_id
        direct_link = get_direct_link(file_id)
    else:
        file_id = False
        direct_link = "[x] Error, Operation failed !"

    return file_id, direct_link


# print("direct_link : ", send_chunk("267092256", "/home/d4rk3r/Pictures/Screenshot from 2020-03-14 18-30-02 - 1.png"))

def send_file(chat_id, file_name):
    """

    :param chat_id:
    :param file_name:
    :return:
    """

    # We split the file First
    # We instantiate and pass the path of the file we ant to split, the debug mode is just to see logs
    s = Split(chunks_directory="../chunks/")

    # We decompose the file in multiple chunks
    s.decompose(file_name)

    # We can print the map of the file (All file will cost <= 15MB)
    json_map_of_chunks = s.get_map()

    success = []  # chunks send successfully
    failed = []  # chunks failed
    final_map = {"datetime": datetime.datetime.now(), "cloud_map": [], "file_map": json_map_of_chunks}

    for key, val in json_map_of_chunks.items():
        file_id, dr_link = send_chunk(chat_id, s.chunks_directory + val)
        if file_id is False:
            # We append the chunk as a failed
            failed.append({
                "id": key,
                "key": val,
            })
        else:
            success.append({
                "id": key,
                "key": val,
            })
            final_map["cloud_map"].append({
                "chunk_id": file_id,
                "chunk_name": val,
                "tmp_link": dr_link
            })

    print("[+] REPORTS !")
    print("[+] {} Succeed, {} Failed !".format(len(success), len(failed)))
    for elt in failed:
        print("[+] {}: {}".format(elt["id"], elt["key"]))

