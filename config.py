import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "25698395")) #optional
API_HASH = getenv("API_HASH", "fe32dc62fb3b986ada525ff09ca1fee9") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6546053871").split()))
OWNER_ID = int(getenv("OWNER_ID", 6546053871))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://missaimeejacobi:aho3zVSi5cB08Gri@agent007.tdgmins.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "6765523076:AAFxW8KJzZMicDlPNjd9YSUFBeM04ksDpFU")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://telegra.ph/file/3c52a01057865f7511168.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER", "4174108603")
LOG_GROUP = getenv("LOG_GROUP", "4174108603")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQBFmi2JXo--Ym4D8CMgt68Az-REDyVk1IUHBVrjGu5rcOAKg0t9P6scdlczv1u5Ikp2bSa5yoKyx9EotXLugfVEpu0t1k-gUHzhyFymttoYR-_wBoh-jf0beQUXKdkgyP2EVu4rq51LE0b1DaOfmtOTDgqIZ-gALd7LDeGNbBN14PWz7G2ENRk1OBsjgPbSWEurJR7Pql4BvJxRG8NlMB4mkHHSGynWDQF6hFHU7nAVCy4ozYk88etFY-UkPp_fZhbz0-KuAGf2EWCaqkH6QLj84wQL38JF9kXFLKqzVPGCFPpvOT4wTpkGL1XxitF_ezY5mgtfu0s04Sh6FU0dcnE0AAAAAYYs2u8A")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
