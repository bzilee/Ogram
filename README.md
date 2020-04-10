# Ogram

A Hacking-Script to transform your Telegram account to a Cloud Storage !

## Requirements


## How to install

- Go to https://t.me/omega_gram_bot
- Start the bot by hitting the START button or just write `/start` and then ENTER.
- Mute notification of the bot (Optionnal but recommended, to notreceive notifications for each chunk you're sending)
- Go to your Telegram Settings > Advanced > Automatic media download and deactive it, that will prevent telegram to automatically download a chunk of a file you're uploading !
- You will get in response, your chat_id, you will use it with requests to ogram API to send files.

## How to launch


- Example process output :
```shell script
[+] Decompose started...

[+] -----------
[+] Best divide ratio found !
[+] FILENAME : /home/d4rk3r/Downloads/Telegram Desktop/video_2020-01-07_11-18-13.mp4
[+] FILE-SIZE : 26558844
[+] CHUNK : 50f9e8254ff00d5d56000ed223c68a7c
[+] CHUNK : 9e57dc0bc76564e760764ccbddf33e50
[+] CHUNK : 7519252c544d1f04f9072ae898b7bb20
[+] Decompose done.
[+] -------
[+] ---
[+] Sending chunk :  ../chunks/50f9e8254ff00d5d56000ed223c68a7c
[+] Uploading the payload
[+] file_id :  BQACAgQAAxkDAAMgXpCARCK_dPklGOrmYIS4YWZB0m0AAqQKAAI85IlQN5jxypv_g5EYBA
[+] Fetching the direct link of the chunk file
[+] Local chunk deleted successfully !
[+] ---
[+] Sending chunk :  ../chunks/9e57dc0bc76564e760764ccbddf33e50
[+] Uploading the payload
[+] file_id :  BQACAgQAAxkDAAMhXpCA_l5pZXHhPIlVDbE6dEPn9LkAAqUKAAI85IlQho3fDSRixeYYBA
[+] Fetching the direct link of the chunk file
[+] Local chunk deleted successfully !
[+] ---
[+] Sending chunk :  ../chunks/7519252c544d1f04f9072ae898b7bb20
[+] Uploading the payload
[+] file_id :  BQACAgQAAxkDAAMiXpCBcJbL9cffp0g-0jMshQRwbSMAAqcKAAI85IlQY1v7GZduX3IYBA
[+] Fetching the direct link of the chunk file
[+] Local chunk deleted successfully !
[+] -------------------------------------------------- 
[+] REPORTS !
[+] 3 Succeed, 0 Failed !
[+] -------------------------------------------------- 
[+] Map saved in '../json_maps//m_7cb6c6c955bd01948ce2b0fc218d6d05.json'
[+] json_path:  ../json_maps//m_7cb6c6c955bd01948ce2b0fc218d6d05.json
[+] Start getting the file...
[+] Fetching chunks...
[+] Elapsed_time:  298 seconds
[+] Downloading and saving in   ../chunks/50f9e8254ff00d5d56000ed223c68a7c
[+] Elapsed_time:  141 seconds
[+] Downloading and saving in   ../chunks/9e57dc0bc76564e760764ccbddf33e50
[+] Elapsed_time:  54 seconds
[+] Downloading and saving in   ../chunks/7519252c544d1f04f9072ae898b7bb20
[+] Rebuild started...
[+] Creating the datas dir
[+] Remake done.
[+] md5_sum checking...
[+] Local md5 : 7cb6c6c955bd01948ce2b0fc218d6d05
[+] Remote md5 : 7cb6c6c955bd01948ce2b0fc218d6d05
[+] md5_sum success match !
[+] Your file ../datas/video_2020-01-07_11-18-13.mp4 have been successfully rebuilded !
```

- Example of json_map after all chunks uploaded :
```json
{
    "file": {
        "file_path": "/home/d4rk3r/Downloads/Telegram Desktop/video_2020-01-07_11-18-13.mp4",
        "file_name": "video_2020-01-07_11-18-13.mp4"
    },
    "md5_sum": "7cb6c6c955bd01948ce2b0fc218d6d05",
    "cloud_map": [
        {
            "chunk_id": "BQACAgQAAxkDAAMWXpBgK5Eubxo2IJRsZOmYryz8Hq4AAooKAAI85IlQFUtQU0CJ_oMYBA",
            "chunk_name": "50f9e8254ff00d5d56000ed223c68a7c",
            "tmp_link": "https://api.telegram.org/file/bot1152608995:AAFnj-WNcNaTc6XNLdSuci7s-vcJaJfeAi0/documents/file_11",
            "datetime": "2020-04-10 13:01:49.760797"
        },
        {
            "chunk_id": "BQACAgQAAxkDAAMXXpBgpFt8Ey9JEig2C3fB4pkfigUAAosKAAI85IlQPjEg92MeDgkYBA",
            "chunk_name": "0ae09b670a6d4009ad57e1df57fdfa46",
            "tmp_link": "https://api.telegram.org/file/bot1152608995:AAFnj-WNcNaTc6XNLdSuci7s-vcJaJfeAi0/documents/file_12",
            "datetime": "2020-04-10 13:03:50.592253"
        }
    ],
    "file_map": {
        "0": "50f9e8254ff00d5d56000ed223c68a7c",
        "1": "0ae09b670a6d4009ad57e1df57fdfa46"
    }
}
```
## Author

- Sanix-darker
