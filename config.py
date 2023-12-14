import os


class Config(object):
    API_HASH = os.environ.get("API_HASH", "294a7bf4488b21609436de1cdd05c316")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6231686503:AAGu1Oa0UsPGveuB8h_vYy8Pu0J5CQhwcuU")
    TELEGRAM_API = os.environ.get("TELEGRAM_API", "25603034")
    OWNER = os.environ.get("OWNER", "5791145987")
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "Anonymous190404")
    SESSION_NAME = os.environ.get("SESSION_NAME", "merge-bot")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "streaamdb")
    PASSWORD = os.environ.get("PASSWORD", "19040456")
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://xajay10997:Xr1p2CNHjIJLrHl8@cluster0.bjsdwy9.mongodb.net/?retryWrites=true&w=majority")
    LOGCHANNEL = os.environ.get("LOGCHANNEL", "-1001953206885")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID","root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = True
    MODES = ["video-video", "video-audio", "video-subtitle","extract-streams"]
    UPSTREAM_REPO = "https://github.com/BLVCK-ANGEL/Merge-Bot"
    UPSTREAM_BRANCH = "main"

    START_TEXT = """
Hi Guys, I am Video Merge Bot!
I can Merge Multiple Videos in One Video. Video Formats should be same.

"""
