# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = 10247139
    API_HASH = "96b46175824223a33737657ab943fd6a"
    BOT_TOKEN = "5306499440:AAHpWLxsP6tFAsxZ7vEx4vqTe1HZsxThn7A"
    name = "gear1000bot"
    SLEEP_THRESHOLD = "60"
    WORKERS = "4"
    BIN_CHANNEL = -1001920297436
    PORT = 8080
    BIND_ADRESS = '0.0.0.0'
    PING_INTERVAL = 1200  # 20 minutes
    OWNER_ID = 1443454117 
    NO_PORT = False
    APP_NAME = None
    OWNER_USERNAME = "Pirate_user"
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = "104.200.18.212/dl"
    HAS_SSL=False
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = "mongodb+srv://720pp:fire@cluster0.ser1dtu.mongodb.net/?retryWrites=true&w=majority"
    UPDATES_CHANNEL = None
    BANNED_CHANNELS = -1001362659779
