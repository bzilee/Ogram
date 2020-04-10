import requests
import json
import time
from os import remove
import datetime
from hashlib import md5
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
    print("[+] Uploading the payload")
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
    print("[+] ---")
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

def get_md5_sum(file_name):
    """
    This method only calcul the md5_sum of a file
    :param file_name:
    :return:
    """
    hasher = md5()
    with open(file_name, 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
    return hasher.hexdigest()


def send_all_chunks(chat_id, chunk_dir, final_map, json_map_of_chunks, delete_chunk=True):
    """

    :param delete_chunk:
    :param chat_id:
    :param chunk_dir:
    :param final_map:
    :param json_map_of_chunks:
    :return:
    """
    success = []  # chunks send successfully
    failed = []  # chunks failed

    for key, val in json_map_of_chunks.items():
        file_id, dr_link = send_chunk(chat_id, chunk_dir + val)
        if file_id is False:
            # We append the chunk as a failed
            failed.append({
                "id": key,
                "key": val
            })
        else:
            success.append({
                "id": key,
                "key": val
            })
            final_map["cloud_map"].append({
                "chunk_id": file_id,
                "chunk_name": val,
                "tmp_link": dr_link,
                "datetime": str(datetime.datetime.now())
            })
            # We delete/remove the chunk file if we are supposed to
            if delete_chunk:
                remove(chunk_dir + val)
                print("[+] Local chunk deleted successfully !")

    print("[+] REPORTS !")
    print("[+] {} Succeed, {} Failed !".format(len(success), len(failed)))
    for elt in failed:
        print("[+] {}: {}".format(elt["id"], elt["key"]))

    return success, failed, final_map


def send_file(chat_id, file_name):
    """

    :param chat_id:
    :param file_name:
    :return:
    """

    # We split the file First
    # We instantiate the Split class by passing the chunk directory
    s = Split(chunks_directory="../chunks/")

    # We decompose the file in multiple chunks
    s.decompose(file_name)

    # We can print the map of the file (All file will cost <= 15MB)
    json_map_of_chunks = s.get_map()
    # We get the md5-sum of the file
    md5_sum = get_md5_sum(file_name)

    # We build our final map
    final_map = {
        "md5_sum": md5_sum,
        "cloud_map": [],
        "file_map": json_map_of_chunks
    }

    success, failed, final_map = send_all_chunks(chat_id, s.chunks_directory, final_map, json_map_of_chunks)

    # We set the map
    s.set_map(final_map)

    # We write the json-map
    s.write_json_map(md5_sum)

    # We print the new map
    print("[+] MAP : ", final_map)


send_file("267092256", "/home/d4rk3r/Downloads/Telegram Desktop/video_2020-01-07_11-18-13.mp4")
