import os


class Config(object):
    API_HASH = os.environ.get("ba25181c01b50d945748801b6c8b6ecc")
    BOT_TOKEN = os.environ.get("7806319439:AAG_5sVnQGQdb6E4GKHxoLG5DLljEgwSfxE")
    TELEGRAM_API = os.environ.get("26162072")
    OWNER = os.environ.get("6717382350")
    OWNER_USERNAME = os.environ.get("Stylish_Star2")
    PASSWORD = os.environ.get("PASSWORD")
    DATABASE_URL = os.environ.get("mongodb+srv://rebelbotz22:vNcEEoNvSQ33d44K@cluster0.oj1hu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    LOGCHANNEL = os.environ.get("-1002252886633")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
