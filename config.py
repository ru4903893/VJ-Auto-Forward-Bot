from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "e10525d8ad0189f8bf7a82a32f538d12")
      API_ID = int(getenv("API_ID", "26107399"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
