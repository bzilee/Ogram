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
