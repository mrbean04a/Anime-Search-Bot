from os import environ
from pyrogram.client import Client

app = Client(
    "AniPlay",
    api_id= int(environ.get("APP_ID", "22923523")),
    api_hash= environ.get("API_HASH", "d52c7824d0e66903a0724b800a16ce2c"),
    bot_token= environ.get("TOKEN", "6064635296:AAFmn0H_GYaKGitsu6C7Docq4zKwuII_rsU")
)
