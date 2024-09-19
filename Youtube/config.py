import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    API_ID = int(os.environ.get("29391335", ))
    API_HASH = os.environ.get("d9755168c2b95f22c87a985c61ad0961", "")
    #Add your channel id. For force Subscribe.
    CHANNEL = os.environ.get("CHANNEL", "")
    #Skip or add your proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = '8080657501:AAHWtrPRnf12pk1eSSMuqlGpiH92RtL0-VE'
